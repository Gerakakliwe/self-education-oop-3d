from renderer import (
    RendererConsole,
    RendererDirectx,
    RendererOpengl
)
import unittest

EXPECTED_INPUT = {
    "name": "test_name",
    "materials": ["test"],
    "color": ["0", "0", "0"],
    "parser": "test_parser"
}


class TestRendererMethods(unittest.TestCase):

    def test_RendererConsole(self):
        renderer = RendererConsole()
        actual_renderer_message = renderer.render_model(EXPECTED_INPUT)
        expected_renderer_message = "Model test_name parsed by test_parser was successfully rendered by ConsoleRenderer"
        self.assertEqual(actual_renderer_message, expected_renderer_message)

    def test_RendererDirectx(self):
        renderer = RendererDirectx()
        actual_renderer_message = renderer.render_model(EXPECTED_INPUT)
        expected_renderer_message = "Model test_name parsed by test_parser was successfully rendered by DirectxRenderer"
        self.assertEqual(actual_renderer_message, expected_renderer_message)

    def test_RendererOpengl(self):
        renderer = RendererOpengl()
        actual_renderer_message = renderer.render_model(EXPECTED_INPUT)
        expected_renderer_message = "Model test_name parsed by test_parser was successfully rendered by OpenglRenderer"
        self.assertEqual(actual_renderer_message, expected_renderer_message)
