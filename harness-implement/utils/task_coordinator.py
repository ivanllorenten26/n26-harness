#!/usr/bin/env python3
"""
Task Coordinator para Harness Long-Running Agents

Coordina la ejecución de tasks paralelos respetando dependencias
y optimizando para implementación incremental.
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

class TaskCoordinator:
    """
    Coordinador de tasks para implementación paralela con dependencias.

    Maneja el workflow de tasks siguiendo la metodología de Anthropic
    para long-running agents.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = project_root
        self.feature_list_path = os.path.join(project_root, ".claude", "feature_list.json")

    def load_feature_list(self) -> Dict:
        """Carga la lista de features/tasks del proyecto."""
        if not os.path.exists(self.feature_list_path):
            raise FileNotFoundError("feature_list.json not found. Run /harness-plan first.")

        with open(self.feature_list_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_feature_list(self, feature_list: Dict) -> None:
        """Guarda la lista de features/tasks actualizada."""
        with open(self.feature_list_path, 'w', encoding='utf-8') as f:
            json.dump(feature_list, f, indent=2, ensure_ascii=False)

    def get_available_tasks(self) -> List[Dict]:
        """
        Obtiene tasks que están listos para ejecutar (dependencias satisfechas).

        Returns:
            Lista de tasks que pueden ejecutarse en paralelo
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        available_tasks = []
        completed_task_ids = {task['id'] for task in tasks if task.get('passes', False)}

        for task in tasks:
            # Skip si ya está completado
            if task.get('passes', False):
                continue

            # Skip si ya está en progreso (implementado por otro agente)
            if task.get('status') == 'in_progress':
                continue

            # Verificar dependencias
            dependencies = task.get('dependencies', [])
            dependencies_satisfied = all(dep_id in completed_task_ids for dep_id in dependencies)

            if dependencies_satisfied:
                available_tasks.append(task)

        return available_tasks

    def get_parallel_groups(self) -> List[Dict]:
        """
        Obtiene los grupos de tasks que pueden ejecutarse en paralelo.

        Returns:
            Lista de grupos con tasks paralelos
        """
        feature_list = self.load_feature_list()
        return feature_list.get('parallel_execution', {}).get('groups', [])

    def get_next_task_for_agent(self, agent_type: str) -> Optional[Dict]:
        """
        Obtiene el siguiente task más prioritario para un agente específico.

        Args:
            agent_type: Tipo de agente (frontend, backend, data, devops)

        Returns:
            Task más prioritario para el agente, o None si no hay disponibles
        """
        available_tasks = self.get_available_tasks()

        # Filtrar por agente asignado
        agent_tasks = [task for task in available_tasks
                      if task.get('agent_assigned') == agent_type]

        if not agent_tasks:
            return None

        # Ordenar por prioridad (menor número = mayor prioridad)
        agent_tasks.sort(key=lambda t: (t.get('priority', 5), t.get('estimated_complexity', 'medium')))

        return agent_tasks[0]

    def get_next_available_task(self) -> Optional[Dict]:
        """
        Obtiene el siguiente task disponible de mayor prioridad (cualquier agente).

        Returns:
            Task de mayor prioridad disponible
        """
        available_tasks = self.get_available_tasks()

        if not available_tasks:
            return None

        # Ordenar por prioridad
        available_tasks.sort(key=lambda t: (t.get('priority', 5), t.get('estimated_complexity', 'medium')))

        return available_tasks[0]

    def mark_task_in_progress(self, task_id: str) -> bool:
        """
        Marca un task como en progreso.

        Args:
            task_id: ID del task

        Returns:
            True si se marcó exitosamente
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        for task in tasks:
            if task.get('id') == task_id:
                task['status'] = 'in_progress'
                task['started_at'] = datetime.now().isoformat()
                self.save_feature_list(feature_list)
                return True

        return False

    def mark_task_completed(self, task_id: str, implementation_notes: Optional[str] = None) -> bool:
        """
        Marca un task como completado.

        Args:
            task_id: ID del task
            implementation_notes: Notas opcionales de la implementación

        Returns:
            True si se marcó exitosamente
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        for task in tasks:
            if task.get('id') == task_id:
                task['passes'] = True
                task['status'] = 'completed'
                task['implemented_at'] = datetime.now().isoformat()
                if implementation_notes:
                    task['implementation_notes'] = implementation_notes
                self.save_feature_list(feature_list)
                return True

        return False

    def mark_task_failed(self, task_id: str, error_message: str) -> bool:
        """
        Marca un task como fallido.

        Args:
            task_id: ID del task
            error_message: Mensaje de error

        Returns:
            True si se marcó exitosamente
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        for task in tasks:
            if task.get('id') == task_id:
                task['status'] = 'failed'
                task['error_message'] = error_message
                task['failed_at'] = datetime.now().isoformat()
                self.save_feature_list(feature_list)
                return True

        return False

    def get_project_progress(self) -> Dict:
        """
        Obtiene el progreso general del proyecto.

        Returns:
            Dict con estadísticas de progreso
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        total_tasks = len(tasks)
        completed_tasks = len([t for t in tasks if t.get('passes', False)])
        in_progress_tasks = len([t for t in tasks if t.get('status') == 'in_progress'])
        failed_tasks = len([t for t in tasks if t.get('status') == 'failed'])

        progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

        # Progreso por categoría
        categories = {}
        for task in tasks:
            category = task.get('category', 'other')
            if category not in categories:
                categories[category] = {'total': 0, 'completed': 0}
            categories[category]['total'] += 1
            if task.get('passes', False):
                categories[category]['completed'] += 1

        # Progreso por agente
        agents = {}
        for task in tasks:
            agent = task.get('agent_assigned', 'unknown')
            if agent not in agents:
                agents[agent] = {'total': 0, 'completed': 0}
            agents[agent]['total'] += 1
            if task.get('passes', False):
                agents[agent]['completed'] += 1

        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'in_progress_tasks': in_progress_tasks,
            'failed_tasks': failed_tasks,
            'pending_tasks': total_tasks - completed_tasks - in_progress_tasks - failed_tasks,
            'progress_percentage': round(progress_percentage, 1),
            'categories': categories,
            'agents': agents,
            'project_ready': progress_percentage >= 80  # 80% completion threshold
        }

    def can_execute_parallel_tasks(self) -> bool:
        """
        Verifica si hay tasks que pueden ejecutarse en paralelo.

        Returns:
            True si hay múltiples tasks disponibles para diferentes agentes
        """
        available_tasks = self.get_available_tasks()

        # Agrupar por agente
        agent_tasks = {}
        for task in available_tasks:
            agent = task.get('agent_assigned', 'general')
            if agent not in agent_tasks:
                agent_tasks[agent] = []
            agent_tasks[agent].append(task)

        # Si hay tasks para al menos 2 agentes diferentes, pueden ejecutarse en paralelo
        return len([agent for agent, tasks in agent_tasks.items() if len(tasks) > 0]) >= 2

    def get_blocked_tasks(self) -> List[Dict]:
        """
        Obtiene tasks que están bloqueados por dependencias no satisfechas.

        Returns:
            Lista de tasks bloqueados con información de dependencias
        """
        feature_list = self.load_feature_list()
        tasks = feature_list.get('features', [])

        completed_task_ids = {task['id'] for task in tasks if task.get('passes', False)}
        blocked_tasks = []

        for task in tasks:
            if task.get('passes', False) or task.get('status') == 'in_progress':
                continue

            dependencies = task.get('dependencies', [])
            unsatisfied_deps = [dep for dep in dependencies if dep not in completed_task_ids]

            if unsatisfied_deps:
                blocked_tasks.append({
                    'task': task,
                    'unsatisfied_dependencies': unsatisfied_deps
                })

        return blocked_tasks

    def suggest_next_actions(self) -> Dict:
        """
        Sugiere las próximas acciones basadas en el estado actual.

        Returns:
            Dict con sugerencias de acciones
        """
        available_tasks = self.get_available_tasks()
        progress = self.get_project_progress()
        blocked_tasks = self.get_blocked_tasks()

        suggestions = {
            'can_continue': len(available_tasks) > 0,
            'parallel_execution_possible': self.can_execute_parallel_tasks(),
            'recommended_action': '',
            'available_tasks': len(available_tasks),
            'blocked_tasks': len(blocked_tasks),
            'progress_percentage': progress['progress_percentage']
        }

        if len(available_tasks) == 0:
            if progress['progress_percentage'] >= 100:
                suggestions['recommended_action'] = 'project_complete'
            elif len(blocked_tasks) > 0:
                suggestions['recommended_action'] = 'resolve_dependencies'
            else:
                suggestions['recommended_action'] = 'check_failed_tasks'
        elif self.can_execute_parallel_tasks():
            suggestions['recommended_action'] = 'execute_parallel'
        else:
            suggestions['recommended_action'] = 'execute_sequential'

        return suggestions

# Funciones utilitarias para uso desde skills
def get_next_task(agent_type: Optional[str] = None, project_root: str = ".") -> Optional[Dict]:
    """
    Obtiene el próximo task para ejecutar.

    Args:
        agent_type: Tipo de agente específico, o None para cualquier agente
        project_root: Directorio raíz del proyecto

    Returns:
        Próximo task a ejecutar
    """
    coordinator = TaskCoordinator(project_root)

    if agent_type:
        return coordinator.get_next_task_for_agent(agent_type)
    else:
        return coordinator.get_next_available_task()

def update_task_status(task_id: str, status: str, notes: Optional[str] = None,
                      project_root: str = ".") -> bool:
    """
    Actualiza el estado de un task.

    Args:
        task_id: ID del task
        status: Nuevo estado (in_progress, completed, failed)
        notes: Notas opcionales
        project_root: Directorio raíz del proyecto

    Returns:
        True si se actualizó exitosamente
    """
    coordinator = TaskCoordinator(project_root)

    if status == 'in_progress':
        return coordinator.mark_task_in_progress(task_id)
    elif status == 'completed':
        return coordinator.mark_task_completed(task_id, notes)
    elif status == 'failed':
        return coordinator.mark_task_failed(task_id, notes or "Task failed")
    else:
        return False

def show_progress(project_root: str = ".") -> None:
    """Muestra el progreso actual del proyecto."""
    coordinator = TaskCoordinator(project_root)
    progress = coordinator.get_project_progress()

    print(f"📊 Progreso del Proyecto: {progress['progress_percentage']}%")
    print(f"   ✅ Completadas: {progress['completed_tasks']}")
    print(f"   🔄 En progreso: {progress['in_progress_tasks']}")
    print(f"   ❌ Fallidas: {progress['failed_tasks']}")
    print(f"   ⏳ Pendientes: {progress['pending_tasks']}")
    print()

    if progress['categories']:
        print("📁 Progreso por categoría:")
        for category, stats in progress['categories'].items():
            percentage = (stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"   {category}: {stats['completed']}/{stats['total']} ({percentage:.0f}%)")
        print()

    if progress['agents']:
        print("👥 Progreso por agente:")
        for agent, stats in progress['agents'].items():
            percentage = (stats['completed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"   {agent}: {stats['completed']}/{stats['total']} ({percentage:.0f}%)")

if __name__ == "__main__":
    # CLI interface para testing
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "next":
            agent_type = sys.argv[2] if len(sys.argv) > 2 else None
            task = get_next_task(agent_type)
            if task:
                print(json.dumps(task, indent=2, ensure_ascii=False))
            else:
                print("No available tasks")

        elif command == "progress":
            show_progress()

        elif command == "update":
            if len(sys.argv) < 4:
                print("Usage: task-coordinator.py update TASK_ID STATUS [NOTES]")
                sys.exit(1)
            task_id = sys.argv[2]
            status = sys.argv[3]
            notes = sys.argv[4] if len(sys.argv) > 4 else None
            success = update_task_status(task_id, status, notes)
            print(f"Task {task_id} -> {status}: {'✅' if success else '❌'}")

        else:
            print("Available commands: next, progress, update")
    else:
        show_progress()