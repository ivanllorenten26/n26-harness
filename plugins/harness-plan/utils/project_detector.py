#!/usr/bin/env python3
"""
Universal Project Detection Engine para Polyglot Harness System

Sistema que analiza cualquier codebase y determina:
- Lenguajes de programación y versiones
- Frameworks y librerías en uso
- Patrones arquitectónicos actuales
- Sistemas de base de datos y ORMs
- Herramientas de testing y build

Compatible con: TypeScript, Python, Kotlin
Frameworks: Remix, FastAPI, Spring Boot
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import re
import subprocess

class ProjectDetector:
    """
    Motor de detección universal que analiza proyectos para determinar
    stack tecnológico y arquitectura existente.
    """

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path).resolve()
        self.detection_results = {}

        # Directorios del harness system que deben ser ignorados
        self.harness_directories = {'.claude', '.harness'}

    def _get_project_files(self, pattern: str) -> List[Path]:
        """
        Obtiene archivos del proyecto excluyendo directorios del harness.

        Args:
            pattern: Patrón glob para buscar archivos

        Returns:
            Lista de archivos que pertenecen al proyecto real
        """
        all_files = list(self.project_path.rglob(pattern))

        # Filtrar archivos que estén dentro de directorios del harness
        project_files = []
        for file_path in all_files:
            # Verificar si el archivo está dentro de algún directorio del harness
            is_harness_file = any(
                harness_dir in file_path.parts
                for harness_dir in self.harness_directories
            )

            if not is_harness_file:
                project_files.append(file_path)

        return project_files

    def analyze_project(self) -> Dict[str, Any]:
        """
        Análisis completo del proyecto.

        Returns:
            Dict con toda la información detectada
        """
        print(f"🔍 Analyzing project: {self.project_path}")

        # 1. Detectar lenguajes
        languages = self._detect_languages()

        # 2. Detectar frameworks
        frameworks = self._detect_frameworks(languages)

        # 3. Detectar arquitectura existente
        architecture = self._analyze_architecture()

        # 4. Detectar database y ORM
        database_info = self._detect_database_systems()

        # 5. Detectar testing frameworks
        testing_info = self._detect_testing_frameworks()

        # 6. Detectar build systems
        build_info = self._detect_build_systems()

        # 7. Generar score de arquitectura
        architecture_score = self._calculate_architecture_score(architecture)

        self.detection_results = {
            'project_path': str(self.project_path),
            'languages': languages,
            'frameworks': frameworks,
            'architecture': architecture,
            'architecture_score': architecture_score,
            'database': database_info,
            'testing': testing_info,
            'build': build_info,
            'supported_harness': self._check_harness_compatibility(),
            'recommendations': self._generate_recommendations(languages, frameworks, architecture),
            'confidence': self._calculate_overall_confidence()
        }

        print(f"✅ Analysis complete. Score: {architecture_score}/100")
        return self.detection_results

    def _detect_languages(self) -> Dict[str, Any]:
        """Detecta lenguajes de programación y versiones."""
        languages = {}

        # TypeScript/JavaScript
        if self._file_exists('package.json'):
            package_json = self._load_json('package.json')
            if package_json:
                # Verificar si es TypeScript
                ts_files = self._get_project_files('*.ts')
                tsx_files = self._get_project_files('*.tsx')
                has_typescript = (
                    self._file_exists('tsconfig.json') or
                    'typescript' in package_json.get('dependencies', {}) or
                    'typescript' in package_json.get('devDependencies', {}) or
                    len(ts_files) > 0 or
                    len(tsx_files) > 0
                )

                if has_typescript:
                    languages['typescript'] = {
                        'detected': True,
                        'confidence': 0.9,
                        'version': self._detect_typescript_version(),
                        'evidence': ['package.json', 'tsconfig.json', '*.ts files'],
                        'package_manager': self._detect_package_manager()
                    }
                else:
                    languages['javascript'] = {
                        'detected': True,
                        'confidence': 0.8,
                        'version': self._detect_node_version(),
                        'evidence': ['package.json', '*.js files'],
                        'package_manager': self._detect_package_manager()
                    }

        # Python
        python_files = self._get_project_files('*.py')
        if python_files or self._file_exists('requirements.txt') or self._file_exists('pyproject.toml'):
            languages['python'] = {
                'detected': True,
                'confidence': 0.9 if len(python_files) > 5 else 0.7,
                'version': self._detect_python_version(),
                'evidence': self._get_python_evidence(),
                'package_manager': self._detect_python_package_manager()
            }

        # Kotlin
        kotlin_files = self._get_project_files('*.kt')
        if kotlin_files or self._file_exists('build.gradle.kts') or self._has_gradle_kotlin():
            languages['kotlin'] = {
                'detected': True,
                'confidence': 0.9 if len(kotlin_files) > 3 else 0.6,
                'version': self._detect_kotlin_version(),
                'evidence': self._get_kotlin_evidence(),
                'build_tool': self._detect_kotlin_build_tool()
            }

        return languages

    def _detect_frameworks(self, languages: Dict[str, Any]) -> Dict[str, Any]:
        """Detecta frameworks específicos para cada lenguaje."""
        frameworks = {}

        # TypeScript/JavaScript Frameworks
        if 'typescript' in languages or 'javascript' in languages:
            frameworks.update(self._detect_typescript_frameworks())

        # Python Frameworks
        if 'python' in languages:
            frameworks.update(self._detect_python_frameworks())

        # Kotlin Frameworks
        if 'kotlin' in languages:
            frameworks.update(self._detect_kotlin_frameworks())

        return frameworks

    def _detect_typescript_frameworks(self) -> Dict[str, Any]:
        """Detecta frameworks TypeScript específicos."""
        frameworks = {}

        package_json = self._load_json('package.json')
        if not package_json:
            return frameworks

        deps = {**package_json.get('dependencies', {}), **package_json.get('devDependencies', {})}

        # Remix
        if '@remix-run/node' in deps or '@remix-run/react' in deps:
            frameworks['remix'] = {
                'detected': True,
                'confidence': 0.95,
                'version': deps.get('@remix-run/node', deps.get('@remix-run/react')),
                'evidence': ['@remix-run dependencies', 'app/ directory'],
                'type': 'fullstack-react'
            }

        # Express
        elif 'express' in deps:
            frameworks['express'] = {
                'detected': True,
                'confidence': 0.9,
                'version': deps.get('express'),
                'evidence': ['express dependency'],
                'type': 'api-server'
            }

        # NestJS
        elif '@nestjs/core' in deps:
            frameworks['nestjs'] = {
                'detected': True,
                'confidence': 0.95,
                'version': deps.get('@nestjs/core'),
                'evidence': ['@nestjs dependencies', 'decorators'],
                'type': 'enterprise-api'
            }

        # Next.js
        elif 'next' in deps:
            frameworks['nextjs'] = {
                'detected': True,
                'confidence': 0.9,
                'version': deps.get('next'),
                'evidence': ['next dependency', 'pages/ or app/ directory'],
                'type': 'fullstack-react'
            }

        return frameworks

    def _detect_python_frameworks(self) -> Dict[str, Any]:
        """Detecta frameworks Python específicos."""
        frameworks = {}

        # Leer requirements.txt
        requirements = self._get_python_requirements()

        # FastAPI
        if 'fastapi' in requirements:
            frameworks['fastapi'] = {
                'detected': True,
                'confidence': 0.95,
                'version': requirements.get('fastapi', 'unknown'),
                'evidence': ['fastapi in requirements', 'async/await patterns'],
                'type': 'async-api'
            }

        # Django
        elif 'django' in requirements:
            frameworks['django'] = {
                'detected': True,
                'confidence': 0.9,
                'version': requirements.get('django'),
                'evidence': ['django in requirements', 'manage.py'],
                'type': 'fullstack-web'
            }

        # Flask
        elif 'flask' in requirements:
            frameworks['flask'] = {
                'detected': True,
                'confidence': 0.85,
                'version': requirements.get('flask'),
                'evidence': ['flask in requirements'],
                'type': 'micro-web'
            }

        return frameworks

    def _detect_kotlin_frameworks(self) -> Dict[str, Any]:
        """Detecta frameworks Kotlin específicos."""
        frameworks = {}

        # Spring Boot
        if self._has_spring_boot():
            frameworks['spring-boot'] = {
                'detected': True,
                'confidence': 0.95,
                'version': self._get_spring_boot_version(),
                'evidence': ['spring-boot dependencies', '@SpringBootApplication'],
                'type': 'enterprise-api'
            }

        return frameworks

    def _analyze_architecture(self) -> Dict[str, Any]:
        """Analiza la arquitectura existente del proyecto."""
        architecture = {
            'pattern': 'unknown',
            'layers': [],
            'compliance_score': 0,
            'issues': [],
            'suggestions': []
        }

        # Detectar estructura de directorios
        dir_structure = self._analyze_directory_structure()

        # Detectar patrones Clean/Hexagonal
        clean_patterns = self._detect_clean_architecture_patterns()

        # Detectar layered architecture
        layered_patterns = self._detect_layered_patterns()

        # Determinar patrón principal
        if clean_patterns['score'] > 0.7:
            architecture['pattern'] = 'clean'
            architecture['compliance_score'] = int(clean_patterns['score'] * 100)
            architecture['layers'] = clean_patterns['layers']
        elif layered_patterns['score'] > 0.6:
            architecture['pattern'] = 'layered'
            architecture['compliance_score'] = int(layered_patterns['score'] * 100)
            architecture['layers'] = layered_patterns['layers']
        else:
            architecture['pattern'] = 'monolithic'
            architecture['compliance_score'] = 30

        return architecture

    def _detect_clean_architecture_patterns(self) -> Dict[str, Any]:
        """Detecta patrones de Clean Architecture."""
        score = 0.0
        layers = []
        evidence = []

        # Buscar directorios típicos de Clean Architecture (excluyendo harness)
        clean_dirs = {
            'domain': ['domain/', 'core/', 'entities/', 'business/'],
            'application': ['application/', 'use-cases/', 'services/', 'usecases/'],
            'infrastructure': ['infrastructure/', 'adapters/', 'repositories/', 'external/'],
            'presentation': ['presentation/', 'controllers/', 'api/', 'web/', 'ui/']
        }

        for layer, possible_dirs in clean_dirs.items():
            for dir_name in possible_dirs:
                # Buscar directorios pero excluyendo los del harness
                matching_dirs = []
                for item in self.project_path.rglob(dir_name):
                    if item.is_dir():
                        # Verificar si está dentro de directorios del harness
                        is_harness_dir = any(
                            harness_dir in item.parts
                            for harness_dir in self.harness_directories
                        )
                        if not is_harness_dir:
                            matching_dirs.append(item)

                if matching_dirs:
                    layers.append(layer)
                    evidence.append(f'{dir_name} directory found')
                    score += 0.25
                    break

        # Buscar archivos con nombres típicos (excluyendo harness)
        clean_files = [
            ('*Entity*.py', '*Entity*.ts', '*Entity*.kt'),
            ('*Repository*.py', '*Repository*.ts', '*Repository*.kt'),
            ('*UseCase*.py', '*UseCase*.ts', '*UseCase*.kt'),
            ('*Controller*.py', '*Controller*.ts', '*Controller*.kt')
        ]

        for file_patterns in clean_files:
            for pattern in file_patterns:
                matching_files = self._get_project_files(pattern)
                if matching_files:
                    score += 0.05
                    evidence.append(f'{pattern} files found')
                    break

        return {
            'score': min(score, 1.0),
            'layers': layers,
            'evidence': evidence
        }

    def _detect_layered_patterns(self) -> Dict[str, Any]:
        """Detecta patrones de arquitectura por capas."""
        score = 0.0
        layers = []

        # Patrones típicos de MVC/layered
        mvc_dirs = ['models/', 'views/', 'controllers/', 'routes/', 'middleware/']

        for dir_name in mvc_dirs:
            if any(self.project_path.rglob(dir_name)):
                layers.append(dir_name.rstrip('/'))
                score += 0.2

        return {
            'score': min(score, 1.0),
            'layers': layers
        }

    def _detect_database_systems(self) -> Dict[str, Any]:
        """Detecta sistemas de base de datos y ORMs."""
        database_info = {
            'databases': [],
            'orms': [],
            'confidence': 0.0
        }

        # Buscar dependencias de base de datos
        package_json = self._load_json('package.json')
        if package_json:
            deps = {**package_json.get('dependencies', {}), **package_json.get('devDependencies', {})}

            # PostgreSQL
            if 'pg' in deps or 'postgres' in deps:
                database_info['databases'].append('postgresql')
                database_info['confidence'] += 0.3

            # ORMs TypeScript
            if 'prisma' in deps:
                database_info['orms'].append('prisma')
                database_info['confidence'] += 0.3
            elif 'typeorm' in deps:
                database_info['orms'].append('typeorm')
                database_info['confidence'] += 0.3

        # Python requirements
        requirements = self._get_python_requirements()
        if 'sqlalchemy' in requirements:
            database_info['orms'].append('sqlalchemy')
            database_info['confidence'] += 0.3
        if 'psycopg2' in requirements or 'asyncpg' in requirements:
            database_info['databases'].append('postgresql')
            database_info['confidence'] += 0.3

        return database_info

    def _detect_testing_frameworks(self) -> Dict[str, Any]:
        """Detecta frameworks de testing."""
        testing_info = {
            'frameworks': [],
            'confidence': 0.0
        }

        # TypeScript testing
        package_json = self._load_json('package.json')
        if package_json:
            deps = {**package_json.get('dependencies', {}), **package_json.get('devDependencies', {})}

            if 'jest' in deps:
                testing_info['frameworks'].append('jest')
                testing_info['confidence'] += 0.3
            if 'vitest' in deps:
                testing_info['frameworks'].append('vitest')
                testing_info['confidence'] += 0.3

        # Python testing
        requirements = self._get_python_requirements()
        if 'pytest' in requirements:
            testing_info['frameworks'].append('pytest')
            testing_info['confidence'] += 0.3

        return testing_info

    def _detect_build_systems(self) -> Dict[str, Any]:
        """Detecta sistemas de build."""
        build_info = {
            'tools': [],
            'confidence': 0.0
        }

        # Node.js build tools
        if self._file_exists('package.json'):
            build_info['tools'].append('npm')
            build_info['confidence'] += 0.2

            package_json = self._load_json('package.json')
            if package_json:
                deps = {**package_json.get('dependencies', {}), **package_json.get('devDependencies', {})}

                if 'vite' in deps:
                    build_info['tools'].append('vite')
                    build_info['confidence'] += 0.3
                if 'webpack' in deps:
                    build_info['tools'].append('webpack')
                    build_info['confidence'] += 0.3

        # Python build tools
        if self._file_exists('pyproject.toml'):
            build_info['tools'].append('poetry')
            build_info['confidence'] += 0.3

        return build_info

    def _calculate_architecture_score(self, architecture: Dict[str, Any]) -> int:
        """Calcula score general de arquitectura (0-100)."""
        base_score = architecture.get('compliance_score', 0)

        # Bonificaciones por buenas prácticas
        bonus = 0

        # Tests presentes
        if self._has_tests():
            bonus += 10

        # Configuración de linting
        if self._has_linting_config():
            bonus += 5

        # Documentación presente
        if self._has_documentation():
            bonus += 5

        # CI/CD configurado
        if self._has_ci_cd():
            bonus += 10

        return min(base_score + bonus, 100)

    def _check_harness_compatibility(self) -> Dict[str, Any]:
        """Verifica compatibilidad con harness system."""
        compatibility = {
            'supported_languages': [],
            'supported_frameworks': [],
            'can_apply_clean_architecture': False,
            'migration_complexity': 'unknown'
        }

        # Verificar lenguajes soportados
        supported_langs = ['typescript', 'python', 'kotlin']
        for lang in supported_langs:
            if lang in self.detection_results.get('languages', {}):
                compatibility['supported_languages'].append(lang)

        # Verificar frameworks soportados
        supported_frameworks = ['remix', 'fastapi', 'spring-boot']
        for fw in supported_frameworks:
            if fw in self.detection_results.get('frameworks', {}):
                compatibility['supported_frameworks'].append(fw)

        # Evaluar posibilidad de aplicar Clean Architecture
        current_architecture = self.detection_results.get('architecture', {})
        if current_architecture.get('compliance_score', 0) > 50:
            compatibility['can_apply_clean_architecture'] = True
            compatibility['migration_complexity'] = 'low'
        elif len(compatibility['supported_languages']) > 0:
            compatibility['can_apply_clean_architecture'] = True
            compatibility['migration_complexity'] = 'medium'
        else:
            compatibility['migration_complexity'] = 'high'

        return compatibility

    # Métodos auxiliares
    def _file_exists(self, filename: str) -> bool:
        """Verifica si un archivo existe."""
        return (self.project_path / filename).exists()

    def _load_json(self, filename: str) -> Optional[Dict]:
        """Carga archivo JSON."""
        try:
            with open(self.project_path / filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def _detect_package_manager(self) -> str:
        """Detecta package manager (npm, yarn, pnpm)."""
        if self._file_exists('yarn.lock'):
            return 'yarn'
        elif self._file_exists('pnpm-lock.yaml'):
            return 'pnpm'
        elif self._file_exists('package-lock.json'):
            return 'npm'
        else:
            return 'npm'

    def _detect_typescript_version(self) -> str:
        """Detecta versión de TypeScript."""
        package_json = self._load_json('package.json')
        if package_json:
            deps = {**package_json.get('dependencies', {}), **package_json.get('devDependencies', {})}
            return deps.get('typescript', 'unknown')
        return 'unknown'

    def _detect_python_version(self) -> str:
        """Detecta versión de Python."""
        try:
            result = subprocess.run(['python', '--version'], capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return 'unknown'

    def _get_python_evidence(self) -> List[str]:
        """Obtiene evidencia de proyecto Python."""
        evidence = []
        if self._file_exists('requirements.txt'):
            evidence.append('requirements.txt')
        if self._file_exists('pyproject.toml'):
            evidence.append('pyproject.toml')
        if self._file_exists('Pipfile'):
            evidence.append('Pipfile')

        # Solo contar archivos Python del proyecto real
        python_files = self._get_project_files('*.py')
        if python_files:
            evidence.append(f'{len(python_files)} *.py files')

        return evidence

    def _detect_python_package_manager(self) -> str:
        """Detecta package manager Python."""
        if self._file_exists('Pipfile'):
            return 'pipenv'
        elif self._file_exists('poetry.lock'):
            return 'poetry'
        elif self._file_exists('requirements.txt'):
            return 'pip'
        else:
            return 'pip'

    def _get_python_requirements(self) -> Dict[str, str]:
        """Obtiene requirements de Python."""
        requirements = {}

        if self._file_exists('requirements.txt'):
            try:
                with open(self.project_path / 'requirements.txt', 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            if '==' in line:
                                name, version = line.split('==')[0:2]
                                requirements[name.strip()] = version.strip()
                            else:
                                requirements[line.split('>=')[0].split('>')[0].strip()] = 'unknown'
            except:
                pass

        return requirements

    def _get_kotlin_evidence(self) -> List[str]:
        """Obtiene evidencia de proyecto Kotlin."""
        evidence = []
        if self._file_exists('build.gradle.kts'):
            evidence.append('build.gradle.kts')
        if self._file_exists('build.gradle'):
            evidence.append('build.gradle')

        # Solo contar archivos Kotlin del proyecto real
        kotlin_files = self._get_project_files('*.kt')
        if kotlin_files:
            evidence.append(f'{len(kotlin_files)} *.kt files')

        return evidence

    def _has_gradle_kotlin(self) -> bool:
        """Verifica si usa Gradle con Kotlin."""
        if self._file_exists('build.gradle') or self._file_exists('build.gradle.kts'):
            return True
        return False

    def _detect_kotlin_version(self) -> str:
        """Detecta versión de Kotlin."""
        # TODO: Implementar detección de versión de Kotlin
        return 'unknown'

    def _detect_kotlin_build_tool(self) -> str:
        """Detecta build tool de Kotlin."""
        if self._file_exists('build.gradle.kts') or self._file_exists('build.gradle'):
            return 'gradle'
        elif self._file_exists('pom.xml'):
            return 'maven'
        else:
            return 'gradle'

    def _has_spring_boot(self) -> bool:
        """Verifica si usa Spring Boot."""
        # Buscar en build.gradle o pom.xml
        if self._file_exists('build.gradle') or self._file_exists('build.gradle.kts'):
            try:
                content = (self.project_path / 'build.gradle').read_text()
                return 'spring-boot' in content
            except:
                pass
        return False

    def _get_spring_boot_version(self) -> str:
        """Obtiene versión de Spring Boot."""
        # TODO: Implementar detección de versión Spring Boot
        return 'unknown'

    def _analyze_directory_structure(self) -> Dict[str, Any]:
        """Analiza estructura de directorios."""
        dirs = []
        for item in self.project_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                dirs.append(item.name)
        return {'directories': dirs}

    def _has_tests(self) -> bool:
        """Verifica si tiene tests."""
        test_patterns = ['test/', 'tests/', '__tests__/', '*.test.*', '*.spec.*']
        for pattern in test_patterns:
            if pattern.endswith('/'):
                # Para directorios, usar lógica similar a Clean Architecture
                matching_dirs = []
                for item in self.project_path.rglob(pattern.rstrip('/')):
                    if item.is_dir():
                        is_harness_dir = any(
                            harness_dir in item.parts
                            for harness_dir in self.harness_directories
                        )
                        if not is_harness_dir:
                            matching_dirs.append(item)
                if matching_dirs:
                    return True
            else:
                # Para archivos, usar el método de filtrado
                matching_files = self._get_project_files(pattern)
                if matching_files:
                    return True
        return False

    def _has_linting_config(self) -> bool:
        """Verifica configuración de linting."""
        lint_files = ['.eslintrc', '.eslintrc.json', '.pylintrc', 'pyproject.toml', 'tslint.json']
        return any(self._file_exists(f) for f in lint_files)

    def _has_documentation(self) -> bool:
        """Verifica documentación."""
        doc_files = ['README.md', 'README.rst', 'docs/', 'documentation/']
        return any(self._file_exists(f) for f in doc_files)

    def _has_ci_cd(self) -> bool:
        """Verifica configuración CI/CD."""
        ci_files = ['.github/workflows/', '.gitlab-ci.yml', 'Jenkinsfile', '.circleci/']
        return any(self._file_exists(f) for f in ci_files)

    def _generate_recommendations(self, languages: Dict, frameworks: Dict, architecture: Dict) -> List[str]:
        """Genera recomendaciones para mejorar el proyecto."""
        recommendations = []

        # Recomendaciones de arquitectura
        if architecture.get('compliance_score', 0) < 70:
            recommendations.append("Consider refactoring to Clean Architecture pattern")

        # Recomendaciones de testing
        if not self._has_tests():
            recommendations.append("Add comprehensive test suite")

        # Recomendaciones de linting
        if not self._has_linting_config():
            recommendations.append("Configure linting and code formatting")

        return recommendations

    def _calculate_overall_confidence(self) -> float:
        """Calcula confianza general de la detección."""
        confidences = []

        # Confianza de lenguajes
        for lang_info in self.detection_results.get('languages', {}).values():
            if isinstance(lang_info, dict):
                confidences.append(lang_info.get('confidence', 0))

        # Confianza de frameworks
        for fw_info in self.detection_results.get('frameworks', {}).values():
            if isinstance(fw_info, dict):
                confidences.append(fw_info.get('confidence', 0))

        if confidences:
            return sum(confidences) / len(confidences)
        else:
            return 0.5


def detect_project(project_path: str = ".") -> Dict[str, Any]:
    """
    Función utilitaria para detectar proyecto desde skills.

    Args:
        project_path: Path del proyecto a analizar

    Returns:
        Dict con toda la información detectada
    """
    detector = ProjectDetector(project_path)
    return detector.analyze_project()


if __name__ == "__main__":
    # Test del detector
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "."
    results = detect_project(path)

    print("\n" + "="*50)
    print("PROJECT ANALYSIS RESULTS")
    print("="*50)
    print(json.dumps(results, indent=2, ensure_ascii=False))