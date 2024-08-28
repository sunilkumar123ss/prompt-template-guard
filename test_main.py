import unittest
# Load this project's module explicitly, including when invoked from repository root.
import importlib.util as _import_util
from pathlib import Path as _Path
import sys as _sys
_spec = _import_util.spec_from_file_location(
    "sunil_agents_" + _Path(__file__).parent.name, _Path(__file__).with_name("main.py"))
_main = _import_util.module_from_spec(_spec)
_sys.modules[_spec.name] = _main
_spec.loader.exec_module(_main)
render_prompt = _main.render_prompt

class TemplateTests(unittest.TestCase):
    def test_simple_fields_and_escaped_braces(self):
        self.assertEqual(render_prompt("{{x}} {question}",{"question":"hello"},{"question"}),"{x} hello")

