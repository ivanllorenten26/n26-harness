#!/usr/bin/env python3
"""
Claude.md Generator para Harness System

Sistema que genera archivos claude.md personalizados basados en:
- Auto-detección del proyecto (project-detector.py)
- Templates específicos por tecnología
- Información del PDR si está disponible
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Importar project detector
try:
    from .project_detector import detect_project
except ImportError:
    try:
        from project_detector import detect_project
    except ImportError:
        def detect_project(path="."):
            return {"languages": {}, "frameworks": {}, "architecture": {}}


class ClaudeMdGenerator:
    """
    Generador de archivos claude.md con templates inteligentes.
    """

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path).resolve()
        self.templates_path = Path(__file__).parent.parent / "templates" / "claude-md"

    def generate_claude_md(self, pdr_content: Optional[str] = None) -> str:
        """
        Genera claude.md completo para el proyecto actual.

        Args:
            pdr_content: Contenido del PDR si está disponible

        Returns:
            Contenido completo del claude.md generado
        """
        print("🔍 Analyzing project for claude.md generation...")

        # 1. Auto-detectar proyecto
        project_analysis = detect_project(str(self.project_path))

        # 2. Seleccionar template apropiado
        template_name = self._select_template(project_analysis)

        # 3. Cargar template
        template_content = self._load_template(template_name)

        # 4. Extraer información del PDR si está disponible
        pdr_info = self._extract_pdr_info(pdr_content) if pdr_content else {}

        # 5. Preparar variables para reemplazo
        template_vars = self._prepare_template_variables(project_analysis, pdr_info)

        # 6. Reemplazar variables en template
        generated_content = self._replace_template_variables(template_content, template_vars)

        print(f"✅ claude.md generated using template: {template_name}")
        return generated_content

    def _select_template(self, project_analysis: Dict[str, Any]) -> str:
        """
        Selecciona el template apropiado basado en la detección del proyecto.
        """
        languages = project_analysis.get("languages", {})
        frameworks = project_analysis.get("frameworks", {})

        # TypeScript + Remix
        if "typescript" in languages and "remix" in frameworks:
            return "typescript-remix-template.md"

        # Python + FastAPI
        elif "python" in languages and "fastapi" in frameworks:
            return "python-fastapi-template.md"

        # Kotlin + Spring Boot
        elif "kotlin" in languages and "spring-boot" in frameworks:
            return "kotlin-spring-template.md"

        # Otras combinaciones TypeScript
        elif "typescript" in languages:
            return "typescript-remix-template.md"  # Default para TypeScript

        # Otras combinaciones Python
        elif "python" in languages:
            return "python-fastapi-template.md"  # Default para Python

        # Otras combinaciones Kotlin
        elif "kotlin" in languages:
            return "kotlin-spring-template.md"  # Default para Kotlin

        # Fallback al template base
        else:
            return "base-template.md"

    def _load_template(self, template_name: str) -> str:
        """
        Carga el contenido del template especificado.
        """
        template_path = self.templates_path / template_name

        if not template_path.exists():
            print(f"⚠️  Template {template_name} not found, using base template")
            template_path = self.templates_path / "base-template.md"

        if not template_path.exists():
            raise FileNotFoundError(f"Base template not found at {template_path}")

        return template_path.read_text(encoding='utf-8')

    def _extract_pdr_info(self, pdr_content: str) -> Dict[str, Any]:
        """
        Extrae información relevante del PDR para claude.md.
        """
        pdr_info = {}

        # Extraer título del proyecto
        title_match = re.search(r"^# (.+)$", pdr_content, re.MULTILINE)
        if title_match:
            pdr_info["project_name"] = title_match.group(1).strip()

        # Extraer descripción del proyecto
        desc_match = re.search(r"## (?:Descripción|Description|Overview)(.*?)(?=\n## |\Z)", pdr_content, re.DOTALL | re.IGNORECASE)
        if desc_match:
            pdr_info["project_description"] = desc_match.group(1).strip()

        # Extraer funcionalidades principales
        features_match = re.search(r"## (?:Funcionalidades|Features|Requirements)(.*?)(?=\n## |\Z)", pdr_content, re.DOTALL | re.IGNORECASE)
        if features_match:
            features_text = features_match.group(1)
            # Extraer bullet points
            features = re.findall(r"^[-*] (.+)$", features_text, re.MULTILINE)
            pdr_info["main_features"] = features[:5]  # Top 5 features

        # Extraer stack tecnológico si está especificado
        tech_match = re.search(r"## (?:Stack|Tecnología|Technology)(.*?)(?=\n## |\Z)", pdr_content, re.DOTALL | re.IGNORECASE)
        if tech_match:
            pdr_info["tech_requirements"] = tech_match.group(1).strip()

        return pdr_info

    def _prepare_template_variables(self, project_analysis: Dict[str, Any], pdr_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara variables para reemplazo en el template.
        """
        variables = {
            # Información básica del proyecto
            "PROJECT_NAME": pdr_info.get("project_name", self.project_path.name),
            "CURRENT_DATE": datetime.now().strftime("%Y-%m-%d"),

            # Detección automática
            "DETECTED_LANGUAGE": self._get_primary_language(project_analysis),
            "DETECTED_FRAMEWORK": self._get_primary_framework(project_analysis),
            "LANGUAGE_VERSION": self._get_language_version(project_analysis),

            # Tipo de proyecto
            "IS_API_PROJECT": self._is_api_project(project_analysis),
            "IS_FULLSTACK_PROJECT": self._is_fullstack_project(project_analysis),

            # Variables específicas por tecnología
            **self._get_tech_specific_variables(project_analysis, pdr_info)
        }

        return variables

    def _get_primary_language(self, project_analysis: Dict[str, Any]) -> str:
        """Obtiene el lenguaje principal detectado."""
        languages = project_analysis.get("languages", {})

        # Ordenar por confianza
        sorted_langs = sorted(languages.items(), key=lambda x: x[1].get("confidence", 0), reverse=True)

        if sorted_langs:
            return sorted_langs[0][0].title()

        return "Unknown"

    def _get_primary_framework(self, project_analysis: Dict[str, Any]) -> str:
        """Obtiene el framework principal detectado."""
        frameworks = project_analysis.get("frameworks", {})

        # Ordenar por confianza
        sorted_frameworks = sorted(frameworks.items(), key=lambda x: x[1].get("confidence", 0), reverse=True)

        if sorted_frameworks:
            return sorted_frameworks[0][0].title()

        return "Unknown"

    def _get_language_version(self, project_analysis: Dict[str, Any]) -> str:
        """Obtiene la versión del lenguaje principal."""
        languages = project_analysis.get("languages", {})
        primary_lang = self._get_primary_language(project_analysis).lower()

        if primary_lang in languages:
            return languages[primary_lang].get("version", "Unknown")

        return "Unknown"

    def _is_api_project(self, project_analysis: Dict[str, Any]) -> bool:
        """Determina si es un proyecto de API."""
        frameworks = project_analysis.get("frameworks", {})
        api_frameworks = ["fastapi", "express", "spring-boot", "nestjs", "flask", "django"]

        return any(fw in frameworks for fw in api_frameworks)

    def _is_fullstack_project(self, project_analysis: Dict[str, Any]) -> bool:
        """Determina si es un proyecto fullstack."""
        frameworks = project_analysis.get("frameworks", {})
        fullstack_frameworks = ["remix", "nextjs", "django", "nuxtjs"]

        return any(fw in frameworks for fw in fullstack_frameworks)

    def _get_tech_specific_variables(self, project_analysis: Dict[str, Any], pdr_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Obtiene variables específicas según la tecnología detectada.
        """
        variables = {}
        frameworks = project_analysis.get("frameworks", {})

        # TypeScript específico
        if "typescript" in project_analysis.get("languages", {}):
            variables.update({
                "TYPESCRIPT_VERSION": project_analysis.get("languages", {}).get("typescript", {}).get("version", "Unknown"),
                "PACKAGE_MANAGER": project_analysis.get("languages", {}).get("typescript", {}).get("package_manager", "npm")
            })

        # Remix específico
        if "remix" in frameworks:
            variables.update({
                "REMIX_VERSION": frameworks.get("remix", {}).get("version", "Unknown"),
                "MAIN_RESOURCE": self._extract_main_resource_from_pdr(pdr_info)
            })

        # FastAPI específico
        if "fastapi" in frameworks:
            variables.update({
                "FASTAPI_VERSION": frameworks.get("fastapi", {}).get("version", "Unknown"),
                "PYTHON_VERSION": project_analysis.get("languages", {}).get("python", {}).get("version", "Unknown")
            })

        # Spring Boot específico
        if "spring-boot" in frameworks:
            variables.update({
                "SPRING_BOOT_VERSION": frameworks.get("spring-boot", {}).get("version", "Unknown"),
                "KOTLIN_VERSION": project_analysis.get("languages", {}).get("kotlin", {}).get("version", "Unknown")
            })

        return variables

    def _extract_main_resource_from_pdr(self, pdr_info: Dict[str, Any]) -> str:
        """
        Extrae el recurso principal del PDR (ej: 'users', 'products', 'orders').
        """
        # Buscar en las features principales
        main_features = pdr_info.get("main_features", [])

        for feature in main_features:
            # Buscar patrones como "gestión de usuarios", "CRUD de productos"
            resource_match = re.search(r"(?:gestión|CRUD|manag\w+|creat\w+|handl\w+)\s+(?:de\s+)?(\w+)", feature.lower())
            if resource_match:
                resource = resource_match.group(1)
                # Pluralizar si es necesario
                if not resource.endswith('s'):
                    resource += 's'
                return resource

        # Fallback basado en el nombre del proyecto
        project_name = pdr_info.get("project_name", "items").lower()
        if "user" in project_name:
            return "users"
        elif "product" in project_name:
            return "products"
        elif "order" in project_name:
            return "orders"

        return "items"  # Fallback genérico

    def _replace_template_variables(self, template_content: str, variables: Dict[str, Any]) -> str:
        """
        Reemplaza variables en el template usando sintaxis {{VARIABLE}}.
        """
        result = template_content

        for var_name, var_value in variables.items():
            # Reemplazar {{VARIABLE}}
            placeholder = f"{{{{{var_name}}}}}"
            result = result.replace(placeholder, str(var_value))

        # Limpiar variables no reemplazadas (dejar como placeholder para usuario)
        result = re.sub(r'\{\{(\w+)\}\}', r'[\1]', result)

        return result


def generate_claude_md_for_project(project_path: str = ".", pdr_content: Optional[str] = None) -> str:
    """
    Función utilitaria para generar claude.md desde skills.

    Args:
        project_path: Path del proyecto
        pdr_content: Contenido del PDR si está disponible

    Returns:
        Contenido del claude.md generado
    """
    generator = ClaudeMdGenerator(project_path)
    return generator.generate_claude_md(pdr_content)


if __name__ == "__main__":
    # Test del generador
    import sys

    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    pdr_file = sys.argv[2] if len(sys.argv) > 2 else None

    pdr_content = None
    if pdr_file and Path(pdr_file).exists():
        pdr_content = Path(pdr_file).read_text()

    try:
        content = generate_claude_md_for_project(project_path, pdr_content)
        print("Generated claude.md:")
        print("=" * 50)
        print(content)
    except Exception as e:
        print(f"❌ Error generating claude.md: {e}")
        sys.exit(1)