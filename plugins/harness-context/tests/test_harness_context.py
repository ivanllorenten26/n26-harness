#!/usr/bin/env python3
"""
Test Suite para harness-context skill

Valida:
- Project detector integration
- Claude.md template generation
- Markdown parsing
- Template system
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Any

# Add the skill utils to path
skill_path = Path(__file__).parent.parent
utils_path = skill_path / "utils"
sys.path.insert(0, str(utils_path))

try:
    from claude_md_generator import ClaudeMdGenerator
    from project_detector import detect_project
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    sys.exit(1)


class HarnessContextTester:
    """
    Test suite para harness-context skill functionality.
    """

    def __init__(self):
        self.test_results = []
        self.temp_dir = None

    def run_all_tests(self) -> bool:
        """
        Ejecuta todos los tests del skill harness-context.

        Returns:
            True si todos los tests pasan, False si alguno falla
        """
        print("🧪 Starting Harness-Context Test Suite...")
        print("=" * 50)

        # Crear directorio temporal para tests
        self.temp_dir = Path(tempfile.mkdtemp(prefix="harness_context_test_"))
        print(f"📁 Test directory: {self.temp_dir}")

        try:
            # Test 1: Template Loading
            self._test_template_loading()

            # Test 2: Project Detection
            self._test_project_detection()

            # Test 3: Claude.md Generation
            self._test_claude_md_generation()

            # Test 4: Template Selection
            self._test_template_selection()

            # Test 5: Validation System
            self._test_validation_system()

            # Reporte final
            self._print_test_results()

            return all(test["passed"] for test in self.test_results)

        finally:
            # Limpiar directorio temporal
            if self.temp_dir and self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                print(f"🧹 Cleaned up test directory")

    def _log_test(self, test_name: str, passed: bool, details: str = ""):
        """Registra el resultado de un test."""
        self.test_results.append({
            "name": test_name,
            "passed": passed,
            "details": details
        })

        status = "✅" if passed else "❌"
        print(f"{status} {test_name}: {'PASS' if passed else 'FAIL'}")
        if details:
            print(f"   {details}")

    def _test_template_loading(self):
        """Test 1: Verificar que los templates claude.md se cargan correctamente."""
        print("\n🔍 Testing Claude.md Template Loading...")

        try:
            generator = ClaudeMdGenerator()

            # Verificar que los templates existen
            templates_dir = skill_path / "templates"
            expected_templates = [
                "base-template.md",
                "typescript-remix-template.md",
                "python-fastapi-template.md",
                "kotlin-spring-template.md"
            ]

            missing_templates = []
            for template in expected_templates:
                if not (templates_dir / template).exists():
                    missing_templates.append(template)

            if missing_templates:
                self._log_test("Template Loading", False, f"Missing templates: {missing_templates}")
            else:
                self._log_test("Template Loading", True, f"All {len(expected_templates)} templates found")

        except Exception as e:
            self._log_test("Template Loading", False, f"Exception: {str(e)}")

    def _test_project_detection(self):
        """Test 2: Verificar project detection para diferentes tecnologías."""
        print("\n🔍 Testing Project Detection...")

        test_projects = {
            "remix": {
                "package.json": '{"dependencies": {"@remix-run/node": "^1.0.0"}}',
                "expected": {"framework": "remix", "language": "typescript"}
            },
            "fastapi": {
                "requirements.txt": "fastapi==0.68.0\nuvicorn==0.15.0",
                "main.py": "from fastapi import FastAPI\napp = FastAPI()",
                "expected": {"framework": "fastapi", "language": "python"}
            },
            "spring-boot": {
                "pom.xml": """<?xml version="1.0"?>
                <project>
                    <dependencies>
                        <dependency>
                            <groupId>org.springframework.boot</groupId>
                            <artifactId>spring-boot-starter-web</artifactId>
                        </dependency>
                    </dependencies>
                </project>""",
                "expected": {"framework": "spring-boot", "language": "kotlin"}
            }
        }

        for project_type, config in test_projects.items():
            try:
                # Crear proyecto de test
                project_dir = self.temp_dir / project_type
                project_dir.mkdir()

                for filename, content in config.items():
                    if filename != "expected":
                        (project_dir / filename).write_text(content)

                # Detectar proyecto
                result = detect_project(str(project_dir))

                # Verificar detección
                expected = config["expected"]
                if all(result.get(k) == v for k, v in expected.items()):
                    self._log_test(f"Project Detection - {project_type}", True)
                else:
                    self._log_test(f"Project Detection - {project_type}", False, f"Expected {expected}, got {result}")

            except Exception as e:
                self._log_test(f"Project Detection - {project_type}", False, f"Exception: {str(e)}")

    def _test_claude_md_generation(self):
        """Test 3: Verificar generación de claude.md para diferentes proyectos."""
        print("\n🔍 Testing Claude.md Generation...")

        try:
            generator = ClaudeMdGenerator()

            # Test con proyecto Remix
            project_dir = self.temp_dir / "remix_test"
            project_dir.mkdir()
            (project_dir / "package.json").write_text('{"dependencies": {"@remix-run/node": "^1.0.0"}}')

            # Generar claude.md
            result = generator.generate_claude_md(str(project_dir))

            if result and "success" in result and result["success"]:
                # Verificar que se creó el archivo
                claude_md_path = project_dir / "claude.md"
                if claude_md_path.exists():
                    content = claude_md_path.read_text()
                    if "# Project Context" in content and "## Tech Stack" in content:
                        self._log_test("Claude.md Generation", True, "Valid claude.md generated")
                    else:
                        self._log_test("Claude.md Generation", False, "Generated claude.md missing required sections")
                else:
                    self._log_test("Claude.md Generation", False, "claude.md file not created")
            else:
                self._log_test("Claude.md Generation", False, f"Generation failed: {result}")

        except Exception as e:
            self._log_test("Claude.md Generation", False, f"Exception: {str(e)}")

    def _test_template_selection(self):
        """Test 4: Verificar selección correcta de templates."""
        print("\n🔍 Testing Template Selection...")

        test_cases = [
            {"framework": "remix", "language": "typescript", "expected": "typescript-remix-template.md"},
            {"framework": "fastapi", "language": "python", "expected": "python-fastapi-template.md"},
            {"framework": "spring-boot", "language": "kotlin", "expected": "kotlin-spring-template.md"},
            {"framework": "unknown", "language": "unknown", "expected": "base-template.md"}
        ]

        try:
            generator = ClaudeMdGenerator()

            for case in test_cases:
                selected_template = generator._select_template(case["framework"], case["language"])
                if case["expected"] in selected_template:
                    self._log_test(f"Template Selection - {case['framework']}", True)
                else:
                    self._log_test(f"Template Selection - {case['framework']}", False,
                                 f"Expected {case['expected']}, got {selected_template}")

        except Exception as e:
            self._log_test("Template Selection", False, f"Exception: {str(e)}")

    def _test_validation_system(self):
        """Test 5: Verificar sistema de validación de claude.md."""
        print("\n🔍 Testing Validation System...")

        # Crear claude.md válido
        valid_claude_md = """# Project Context

## Business Domain
Test project for validation

## Tech Stack
- Framework: Remix
- Language: TypeScript
- Database: SQLite

## Architecture Patterns
Clean Architecture

## Team Context
Solo developer
"""

        # Crear claude.md inválido
        invalid_claude_md = """# Incomplete File
Missing required sections.
"""

        try:
            generator = ClaudeMdGenerator()

            # Test archivo válido
            valid_path = self.temp_dir / "valid_claude.md"
            valid_path.write_text(valid_claude_md)

            valid_result = generator.validate_claude_md(str(valid_path))
            if valid_result.get("valid", False):
                self._log_test("Validation - Valid File", True)
            else:
                self._log_test("Validation - Valid File", False, f"Valid file failed validation: {valid_result}")

            # Test archivo inválido
            invalid_path = self.temp_dir / "invalid_claude.md"
            invalid_path.write_text(invalid_claude_md)

            invalid_result = generator.validate_claude_md(str(invalid_path))
            if not invalid_result.get("valid", True):  # Debe ser False
                self._log_test("Validation - Invalid File", True)
            else:
                self._log_test("Validation - Invalid File", False, "Invalid file passed validation")

        except Exception as e:
            self._log_test("Validation System", False, f"Exception: {str(e)}")

    def _print_test_results(self):
        """Imprime resumen final de tests."""
        print("\n" + "=" * 50)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 50)

        passed = sum(1 for test in self.test_results if test["passed"])
        total = len(self.test_results)

        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")

        if total - passed > 0:
            print("\n❌ FAILED TESTS:")
            for test in self.test_results:
                if not test["passed"]:
                    print(f"   - {test['name']}: {test['details']}")

        print(f"\n{'🎉 ALL TESTS PASSED!' if passed == total else '⚠️  SOME TESTS FAILED'}")


def main():
    """Función principal para ejecutar los tests."""
    tester = HarnessContextTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()