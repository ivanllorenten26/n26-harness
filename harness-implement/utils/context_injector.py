#!/usr/bin/env python3
"""
Context Injector para Harness Long-Running Agents

Sistema CRÍTICO que inyecta contexto arquitectónico YAML a agentes especializados
para mantener coherencia durante implementación paralela.
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Importar project detector para integración
try:
    from .project_detector import detect_project
except ImportError:
    # Fallback para cuando se ejecute directamente
    try:
        from project_detector import detect_project
    except ImportError:
        def detect_project(path="."):
            return {"languages": {}, "frameworks": {}, "architecture": {}}

class ContextInjector:
    """
    Inyector de contexto arquitectónico para agentes especializados.

    Carga documentos YAML de arquitectura y los inyecta como contexto
    a agentes para mantener coherencia durante implementación paralela.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.architecture_root = self.project_root / ".harness/arquitectura"
        self._architecture_cache = {}

    def load_global_architecture(self) -> Dict[str, Any]:
        """
        Carga toda la arquitectura global desde YAML files.

        Returns:
            Dict con toda la arquitectura global cargada
        """
        if 'global' in self._architecture_cache:
            return self._architecture_cache['global']

        global_arch = {}
        global_path = self.architecture_root / "global"

        if not global_path.exists():
            raise FileNotFoundError(f"Global architecture not found: {global_path}")

        # Cargar todos los YAMLs globales
        yaml_files = {
            'stack_decisions': 'stack-decisions.yaml',
            'coding_standards': 'coding-standards.yaml',
            'api_contracts': 'api-contracts.yaml',
            'database_schema': 'database-schema.yaml'
        }

        for key, filename in yaml_files.items():
            file_path = global_path / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    global_arch[key] = yaml.safe_load(f)
            else:
                print(f"⚠️ Warning: {filename} not found, skipping")

        self._architecture_cache['global'] = global_arch
        return global_arch

    def load_cross_cutting_concerns(self) -> Dict[str, Any]:
        """
        Carga cross-cutting concerns desde YAML files.

        Returns:
            Dict con cross-cutting concerns cargados
        """
        if 'cross_cutting' in self._architecture_cache:
            return self._architecture_cache['cross_cutting']

        cross_cutting = {}
        cross_cutting_path = self.architecture_root / "cross-cutting"

        if not cross_cutting_path.exists():
            print("⚠️ Warning: Cross-cutting concerns not found")
            return {}

        yaml_files = {
            'error_handling': 'error-handling.yaml',
            'logging': 'logging.yaml',
            'testing_strategy': 'testing-strategy.yaml'
        }

        for key, filename in yaml_files.items():
            file_path = cross_cutting_path / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    cross_cutting[key] = yaml.safe_load(f)

        self._architecture_cache['cross_cutting'] = cross_cutting
        return cross_cutting

    def load_feature_architecture(self, feature_name: str) -> Dict[str, Any]:
        """
        Carga arquitectura específica de una feature.

        Args:
            feature_name: Nombre de la feature

        Returns:
            Dict con arquitectura específica de la feature
        """
        cache_key = f'feature_{feature_name}'
        if cache_key in self._architecture_cache:
            return self._architecture_cache[cache_key]

        feature_arch = {}
        feature_path = self.architecture_root / "features" / feature_name

        if not feature_path.exists():
            # Feature no tiene arquitectura específica, retornar vacío
            return {}

        yaml_files = {
            'architecture': 'architecture.yaml',
            'api_spec': 'api-spec.yaml',
            'components': 'components.yaml'
        }

        for key, filename in yaml_files.items():
            file_path = feature_path / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    feature_arch[key] = yaml.safe_load(f)

        self._architecture_cache[cache_key] = feature_arch
        return feature_arch

    def get_task_context(self, task_id: str) -> Dict[str, Any]:
        """
        Obtiene contexto específico para un task desde feature_list.json.

        Args:
            task_id: ID del task

        Returns:
            Dict con detalles del task
        """
        feature_list_path = self.project_root / ".claude" / "feature_list.json"

        if not feature_list_path.exists():
            raise FileNotFoundError("feature_list.json not found")

        with open(feature_list_path, 'r', encoding='utf-8') as f:
            feature_list = json.load(f)

        # Buscar el task específico
        for feature in feature_list.get('features', []):
            if feature.get('id') == task_id:
                return feature

        raise ValueError(f"Task {task_id} not found in feature_list.json")

    def inject_context_for_agent(self, agent_type: str, task_id: str,
                                feature_name: Optional[str] = None,
                                auto_detect: bool = True) -> Dict[str, Any]:
        """
        MÉTODO PRINCIPAL: Inyecta contexto completo para un agente específico.

        Args:
            agent_type: Tipo de agente (frontend, backend, data, devops)
            task_id: ID del task que va a ejecutar
            feature_name: Nombre de la feature (opcional)

        Returns:
            Dict con contexto completo inyectado para el agente
        """
        print(f"🔌 Inyectando contexto para {agent_type} agent (task: {task_id})")

        # 1. Cargar arquitectura global (SIEMPRE)
        global_arch = self.load_global_architecture()

        # 2. Cargar cross-cutting concerns (SIEMPRE)
        cross_cutting = self.load_cross_cutting_concerns()

        # 3. Cargar feature architecture si se especifica
        feature_arch = {}
        if feature_name:
            feature_arch = self.load_feature_architecture(feature_name)

        # 4. Obtener detalles del task
        task_context = self.get_task_context(task_id)

        # 4.5. AUTO-DETECCIÓN: Analizar proyecto actual si está habilitado
        project_analysis = {}
        if auto_detect:
            try:
                project_analysis = detect_project(str(self.project_root))
                print(f"   🔍 Auto-detection complete: {len(project_analysis.get('languages', {}))} languages")
            except Exception as e:
                print(f"   ⚠️ Auto-detection failed: {e}")

        # 4.6. CLAUDE.MD: Cargar contexto específico del proyecto
        project_context = self._load_claude_md_context()

        # 5. Filtrar contexto relevante según tipo de agente
        relevant_context = self._filter_context_for_agent(
            agent_type, global_arch, cross_cutting, feature_arch, task_context, project_analysis
        )

        # 6. Estructura final de contexto
        injected_context = {
            'agent_type': agent_type,
            'task_id': task_id,
            'task_details': task_context,
            'global_architecture': relevant_context['global'],
            'cross_cutting_concerns': relevant_context['cross_cutting'],
            'feature_architecture': feature_arch,
            'project_info': self._get_project_info(),
            'project_analysis': project_analysis,  # AUTO-DETECCIÓN: Análisis automático del proyecto
            'project_context': project_context,    # CLAUDE.MD: Contexto específico del proyecto
            'clean_architecture_patterns': self._get_clean_architecture_context(agent_type, project_analysis),
            'methodology': {
                'type': 'anthropic-long-running-agents',
                'incremental_progress': True,
                'context_injection': True,
                'testing_required': True,
                'commit_pattern': 'feature-complete',
                'architecture_pattern': 'clean_hexagonal'
            }
        }

        print(f"   ✅ Contexto inyectado: {len(str(injected_context))} caracteres")
        return injected_context

    def _filter_context_for_agent(self, agent_type: str, global_arch: Dict,
                                 cross_cutting: Dict, feature_arch: Dict,
                                 task_context: Dict, project_analysis: Dict = None) -> Dict[str, Any]:
        """
        Filtra el contexto según el tipo de agente para enviar solo lo relevante.

        Esto reduce tokens y mejora la eficiencia del contexto.
        """
        filtered = {
            'global': {},
            'cross_cutting': cross_cutting  # Cross-cutting siempre relevante
        }

        if agent_type == 'frontend':
            # Frontend necesita: UI patterns, frontend stack, API contracts
            filtered['global'] = {
                'stack_decisions': {
                    'frontend': global_arch.get('stack_decisions', {}).get('frontend', {}),
                    'project_type': global_arch.get('stack_decisions', {}).get('project_type')
                },
                'coding_standards': {
                    'naming_conventions': global_arch.get('coding_standards', {}).get('naming_conventions', {}),
                    'project_structure': global_arch.get('coding_standards', {}).get('project_structure', {}).get('frontend', {}),
                    'git_workflow': global_arch.get('coding_standards', {}).get('git_workflow', {})
                },
                'api_contracts': global_arch.get('api_contracts', {})  # Para consumir APIs
            }

        elif agent_type == 'backend':
            # Backend necesita: Backend stack, database schema, API contracts
            filtered['global'] = {
                'stack_decisions': {
                    'backend': global_arch.get('stack_decisions', {}).get('backend', {}),
                    'infrastructure': global_arch.get('stack_decisions', {}).get('infrastructure', {}),
                    'project_type': global_arch.get('stack_decisions', {}).get('project_type')
                },
                'coding_standards': {
                    'naming_conventions': global_arch.get('coding_standards', {}).get('naming_conventions', {}),
                    'project_structure': global_arch.get('coding_standards', {}).get('project_structure', {}).get('backend', {}),
                    'git_workflow': global_arch.get('coding_standards', {}).get('git_workflow', {})
                },
                'api_contracts': global_arch.get('api_contracts', {}),
                'database_schema': global_arch.get('database_schema', {})
            }

        elif agent_type == 'data':
            # Data agent necesita: Database schema, data stack, infrastructure
            filtered['global'] = {
                'stack_decisions': global_arch.get('stack_decisions', {}),
                'coding_standards': global_arch.get('coding_standards', {}),
                'database_schema': global_arch.get('database_schema', {})
            }

        elif agent_type == 'devops':
            # DevOps necesita: Infrastructure, deployment, todo el stack
            filtered['global'] = global_arch  # DevOps ve todo

        else:
            # Agente genérico ve todo
            filtered['global'] = global_arch

        return filtered

    def _get_project_info(self) -> Dict[str, Any]:
        """Obtiene información básica del proyecto."""
        try:
            with open(self.project_root / ".claude" / "project_config.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _load_claude_md_context(self) -> Dict[str, Any]:
        """
        Carga contexto específico del proyecto desde claude.md

        Returns:
            Dict con contexto del proyecto o None si no existe claude.md
        """
        claude_md_path = self.project_root / "claude.md"

        if not claude_md_path.exists():
            return {"project_context": None, "claude_md_available": False}

        try:
            content = claude_md_path.read_text(encoding='utf-8')
            parsed = self._parse_claude_md_content(content)

            print(f"   📋 claude.md loaded: {len(parsed)} sections parsed")

            return {
                "project_context": {
                    "business_domain": parsed.get("business_domain"),
                    "business_rules": parsed.get("business_rules"),
                    "tech_decisions": parsed.get("tech_decisions"),
                    "critical_endpoints": parsed.get("endpoints"),
                    "team_context": parsed.get("team"),
                    "performance_targets": parsed.get("performance"),
                    "security_requirements": parsed.get("security"),
                    "monitoring_requirements": parsed.get("monitoring"),
                    "external_integrations": parsed.get("integrations"),
                    "project_specific_patterns": parsed.get("patterns"),
                    "naming_conventions": parsed.get("naming_conventions")
                },
                "claude_md_available": True,
                "claude_md_last_updated": parsed.get("last_updated")
            }
        except Exception as e:
            print(f"   ⚠️ Warning: Could not parse claude.md: {e}")
            return {"project_context": None, "claude_md_available": False, "error": str(e)}

    def _parse_claude_md_content(self, content: str) -> Dict[str, Any]:
        """
        Parser básico de markdown para extraer información estructurada de claude.md

        Args:
            content: Contenido completo del archivo claude.md

        Returns:
            Dict con información estructurada extraída
        """
        parsed = {}

        # 1. DOMINIO DE NEGOCIO
        business_domain = self._extract_section_content(content, r"## 🎯 Contexto del Proyecto")
        if business_domain:
            parsed["business_domain"] = {
                "description": self._extract_bullet_point(business_domain, "Qué hace"),
                "target_users": self._extract_bullet_point(business_domain, "Usuarios objetivo"),
                "unique_value": self._extract_bullet_point(business_domain, "Valor único")
            }

            # Reglas de negocio
            rules_section = self._extract_subsection(business_domain, "### Reglas de Negocio Críticas")
            if rules_section:
                parsed["business_rules"] = self._extract_bullet_points(rules_section)

        # 2. DECISIONES TECNOLÓGICAS
        tech_section = self._extract_section_content(content, r"## 🏗️ Arquitectura de ESTE Proyecto")
        if tech_section:
            stack_info = self._extract_subsection(tech_section, "### Stack Tecnológico Elegido")
            decisions_info = self._extract_subsection(tech_section, "### Decisiones Arquitectónicas Específicas")

            parsed["tech_decisions"] = {
                "language": self._extract_bullet_point(stack_info, "Lenguaje") if stack_info else None,
                "framework": self._extract_bullet_point(stack_info, "Framework") if stack_info else None,
                "database": self._extract_bullet_point(stack_info, "Base de datos") if stack_info else None,
                "deployment": self._extract_bullet_point(stack_info, "Deploy") if stack_info else None,
                "authentication": self._extract_bullet_point(decisions_info, "Autenticación") if decisions_info else None,
                "cache_strategy": self._extract_bullet_point(decisions_info, "Estado/Cache") if decisions_info else None,
                "storage": self._extract_bullet_point(decisions_info, "Storage") if decisions_info else None
            }

        # 3. ENDPOINTS/RUTAS CRÍTICAS
        config_section = self._extract_section_content(content, r"## 🔧 Configuración Específica")
        if config_section:
            endpoints_info = self._extract_subsection(config_section, "### Endpoints/Rutas Críticas")
            if endpoints_info:
                parsed["endpoints"] = self._extract_code_blocks(endpoints_info)

        # 4. CONTEXTO DEL EQUIPO
        team_section = self._extract_section_content(content, r"## 👥 Contexto del Equipo")
        if team_section:
            parsed["team"] = {
                "responsibilities": self._extract_subsection(team_section, "### Responsabilidades"),
                "workflow": self._extract_subsection(team_section, "### Flujo de Trabajo")
            }

        # 5. CONSIDERACIONES ESPECIALES
        special_section = self._extract_section_content(content, r"## 🚨 Consideraciones Especiales")
        if special_section:
            parsed["performance"] = self._extract_subsection(special_section, "### Performance Crítica")
            parsed["security"] = self._extract_subsection(special_section, "### Seguridad Específica")
            parsed["monitoring"] = self._extract_subsection(special_section, "### Monitoreo y Alertas")

        # 6. PATRONES ESPECÍFICOS (si hay sección de Claude Code)
        claude_section = self._extract_section_content(content, r"## 🎯.*Claude Code")
        if claude_section:
            parsed["patterns"] = self._extract_code_blocks(claude_section)
            parsed["naming_conventions"] = self._extract_subsection(claude_section, "### Convenciones de Naming")

        # 7. FECHA DE ÚLTIMA ACTUALIZACIÓN
        timestamp_match = re.search(r"Última actualización: (.+)", content)
        if timestamp_match:
            parsed["last_updated"] = timestamp_match.group(1).strip()

        return parsed

    def _extract_section_content(self, content: str, section_pattern: str) -> Optional[str]:
        """Extrae contenido de una sección específica"""
        pattern = f"{section_pattern}(.*?)(?=\n## |$)"
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_subsection(self, section_content: str, subsection_pattern: str) -> Optional[str]:
        """Extrae contenido de una subsección específica"""
        pattern = f"{subsection_pattern}(.*?)(?=\n### |\n## |$)"
        match = re.search(pattern, section_content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_bullet_point(self, content: str, bullet_text: str) -> Optional[str]:
        """Extrae el valor de un bullet point específico"""
        pattern = f"\\*\\*{re.escape(bullet_text)}\\*\\*:?\\s*(.+)"
        match = re.search(pattern, content)
        return match.group(1).strip() if match else None

    def _extract_bullet_points(self, content: str) -> List[str]:
        """Extrae todos los bullet points de una sección"""
        pattern = r"^- (.+)$"
        matches = re.findall(pattern, content, re.MULTILINE)
        return [match.strip() for match in matches]

    def _extract_code_blocks(self, content: str) -> List[str]:
        """Extrae bloques de código de una sección"""
        pattern = r"```[\w]*\n?(.*?)```"
        matches = re.findall(pattern, content, re.DOTALL)
        return [match.strip() for match in matches]

    def validate_architecture_completeness(self) -> Dict[str, bool]:
        """
        Valida que toda la arquitectura necesaria esté presente.

        Returns:
            Dict indicando qué componentes están disponibles
        """
        validation = {
            'global_architecture': False,
            'cross_cutting_concerns': False,
            'project_config': False,
            'feature_list': False
        }

        # Validar arquitectura global
        global_path = self.architecture_root / "global"
        required_global = ['stack-decisions.yaml', 'coding-standards.yaml',
                          'api-contracts.yaml', 'database-schema.yaml']

        if global_path.exists():
            existing = [f.name for f in global_path.glob('*.yaml')]
            validation['global_architecture'] = all(f in existing for f in required_global)

        # Validar cross-cutting concerns
        cross_cutting_path = self.architecture_root / "cross-cutting"
        if cross_cutting_path.exists():
            validation['cross_cutting_concerns'] = len(list(cross_cutting_path.glob('*.yaml'))) > 0

        # Validar archivos de proyecto
        validation['project_config'] = (self.project_root / ".claude" / "project_config.json").exists()
        validation['feature_list'] = (self.project_root / ".claude" / "feature_list.json").exists()

        return validation

    def _get_clean_architecture_context(self, agent_type: str, project_analysis: Dict = None) -> Dict[str, Any]:
        """
        NUEVO: Genera contexto específico de Clean Architecture para el agente.

        Args:
            agent_type: Tipo de agente
            project_analysis: Análisis del proyecto actual

        Returns:
            Dict con patrones y guidelines de Clean Architecture
        """
        # Contexto base de Clean Architecture
        clean_context = {
            'architecture_type': 'clean_hexagonal',
            'layers': {
                'domain': {
                    'description': 'Core business logic, entities, value objects, domain services',
                    'dependencies': [],
                    'constraints': [
                        'No framework dependencies',
                        'No I/O operations',
                        'Pure business logic only',
                        'Technology agnostic'
                    ],
                    'patterns': ['entities', 'value_objects', 'domain_services', 'domain_events']
                },
                'application': {
                    'description': 'Use cases, commands, queries, application services, ports',
                    'dependencies': ['domain'],
                    'constraints': [
                        'Orchestrates domain objects',
                        'Defines ports for infrastructure',
                        'No direct infrastructure dependencies'
                    ],
                    'patterns': ['use_cases', 'commands', 'queries', 'ports', 'dto']
                },
                'infrastructure': {
                    'description': 'Adapters, repositories, external services, frameworks',
                    'dependencies': ['domain', 'application'],
                    'constraints': [
                        'Implements ports from application layer',
                        'Contains framework-specific code',
                        'Handles I/O operations'
                    ],
                    'patterns': ['adapters', 'repositories', 'external_services', 'database_models']
                },
                'presentation': {
                    'description': 'Controllers, DTOs, validation, routing, middleware',
                    'dependencies': ['domain', 'application'],
                    'constraints': [
                        'Handles HTTP/API concerns',
                        'Input validation and serialization',
                        'Framework-specific presentation logic',
                        'No direct domain manipulation'
                    ],
                    'patterns': ['controllers', 'dto', 'validation', 'routing', 'middleware']
                }
            }
        }

        # Contexto específico por tipo de agente
        if agent_type == 'frontend':
            # Frontend principalmente trabaja en presentation layer
            clean_context['focus_layers'] = ['presentation']
            clean_context['agent_guidelines'] = [
                'Implement controllers that delegate to application use cases',
                'Create DTOs for data transfer between layers',
                'Handle input validation at presentation boundary',
                'Keep UI logic separate from business logic'
            ]
            if project_analysis and 'remix' in project_analysis.get('frameworks', {}):
                clean_context['framework_integration'] = {
                    'remix': {
                        'loaders': 'Handle data fetching, call application use cases',
                        'actions': 'Handle form submissions, call application commands',
                        'components': 'Pure presentation logic, receive props from loaders',
                        'error_boundaries': 'Handle presentation-layer errors'
                    }
                }

        elif agent_type == 'backend':
            # Backend trabaja principalmente en application e infrastructure
            clean_context['focus_layers'] = ['application', 'infrastructure']
            clean_context['agent_guidelines'] = [
                'Implement use cases that orchestrate domain objects',
                'Define ports (interfaces) in application layer',
                'Implement adapters in infrastructure layer',
                'Keep business logic in domain layer'
            ]
            if project_analysis:
                frameworks = project_analysis.get('frameworks', {})
                if 'fastapi' in frameworks:
                    clean_context['framework_integration'] = {
                        'fastapi': {
                            'dependencies': 'Use for dependency injection of use cases',
                            'routers': 'Thin controllers that call use cases',
                            'middleware': 'Cross-cutting concerns (auth, logging)',
                            'background_tasks': 'Async use case execution'
                        }
                    }
                elif 'spring-boot' in frameworks:
                    clean_context['framework_integration'] = {
                        'spring-boot': {
                            'services': 'Application services implementing use cases',
                            'repositories': 'Data access ports and adapters',
                            'controllers': 'Presentation layer handling HTTP',
                            'configuration': 'Dependency injection configuration'
                        }
                    }

        elif agent_type == 'data':
            # Data agent se enfoca en infrastructure (repositories, adapters)
            clean_context['focus_layers'] = ['infrastructure']
            clean_context['agent_guidelines'] = [
                'Implement repository interfaces defined in application layer',
                'Create database adapters that implement ports',
                'Handle data mapping between domain and database models',
                'Ensure database operations don\'t leak into business logic'
            ]

        elif agent_type == 'devops':
            # DevOps maneja toda la infraestructura
            clean_context['focus_layers'] = ['infrastructure']
            clean_context['agent_guidelines'] = [
                'Configure deployment for layered architecture',
                'Set up monitoring for each architectural layer',
                'Ensure proper separation of concerns in deployment',
                'Configure testing strategies for each layer'
            ]

        # Añadir lenguajes específicos si están detectados
        if project_analysis:
            detected_langs = project_analysis.get('languages', {})
            clean_context['language_patterns'] = {}

            if 'typescript' in detected_langs:
                clean_context['language_patterns']['typescript'] = {
                    'naming_conventions': {
                        'entities': 'PascalCase classes',
                        'use_cases': 'PascalCase with UseCase suffix',
                        'repositories': 'PascalCase with Repository suffix',
                        'interfaces': 'I prefix for ports'
                    },
                    'directory_structure': {
                        'domain': 'src/domain/',
                        'application': 'src/application/',
                        'infrastructure': 'src/infrastructure/',
                        'presentation': 'src/presentation/'
                    }
                }

            if 'python' in detected_langs:
                clean_context['language_patterns']['python'] = {
                    'naming_conventions': {
                        'entities': 'PascalCase classes',
                        'use_cases': 'snake_case with _use_case suffix',
                        'repositories': 'PascalCase with Repository suffix',
                        'interfaces': 'Abstract base classes'
                    },
                    'directory_structure': {
                        'domain': 'app/domain/',
                        'application': 'app/application/',
                        'infrastructure': 'app/infrastructure/',
                        'presentation': 'app/api/'
                    }
                }

            if 'kotlin' in detected_langs:
                clean_context['language_patterns']['kotlin'] = {
                    'naming_conventions': {
                        'entities': 'PascalCase classes',
                        'use_cases': 'PascalCase with UseCase suffix',
                        'repositories': 'PascalCase with Repository interface',
                        'services': 'PascalCase with Service suffix'
                    },
                    'directory_structure': {
                        'domain': 'src/main/kotlin/domain/',
                        'application': 'src/main/kotlin/application/',
                        'infrastructure': 'src/main/kotlin/infrastructure/',
                        'presentation': 'src/main/kotlin/presentation/'
                    }
                }

        return clean_context

# Función utilitaria para uso directo desde skills
def inject_context(agent_type: str, task_id: str, feature_name: Optional[str] = None,
                  project_root: str = ".") -> Dict[str, Any]:
    """
    Función utilitaria para inyectar contexto desde skills.

    Args:
        agent_type: Tipo de agente
        task_id: ID del task
        feature_name: Nombre de la feature (opcional)
        project_root: Directorio raíz del proyecto

    Returns:
        Dict con contexto inyectado
    """
    injector = ContextInjector(project_root)
    return injector.inject_context_for_agent(agent_type, task_id, feature_name)

# Función para validar arquitectura desde skills
def validate_architecture(project_root: str = ".") -> bool:
    """
    Valida que la arquitectura esté completa antes de implementación.

    Returns:
        True si la arquitectura está lista para implementación
    """
    injector = ContextInjector(project_root)
    validation = injector.validate_architecture_completeness()

    missing = [component for component, available in validation.items() if not available]

    if missing:
        print(f"❌ Arquitectura incompleta. Faltantes: {', '.join(missing)}")
        print("   Ejecuta '/harness-plan' para generar arquitectura completa")
        return False

    print("✅ Arquitectura completa y lista para implementación")
    return True

if __name__ == "__main__":
    # Test del sistema de inyección
    if len(sys.argv) > 1:
        agent_type = sys.argv[1]
        task_id = sys.argv[2] if len(sys.argv) > 2 else "TEST-001"

        try:
            injector = ContextInjector()
            context = injector.inject_context_for_agent(agent_type, task_id)
            print(json.dumps(context, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        # Validar arquitectura
        is_valid = validate_architecture()
        sys.exit(0 if is_valid else 1)