from main import validate_parameters
from parser import Parser3ds
from renderer import RendererConsole
import unittest


class TestMainMethods(unittest.TestCase):

    def test_validate_parameters_should_succeed(self):
        actual_parser, actual_renderer = validate_parameters('.3ds', 'console')
        expected_parser, expected_renderer = Parser3ds(), RendererConsole()
        self.assertEqual((actual_parser, actual_renderer), (expected_parser, expected_renderer))

    def test_validate_parameters_unsupported_file_extension_should_fail(self):
        with self.assertRaises(ValueError) as thrown_exception:
            validate_parameters('.unsupported', 'console')

        self.assertEqual("UNKNOWN FILE EXTENSION, only .3ds, .fbx and .collada are possible",
                         thrown_exception.exception.args[0])

    def test_validate_parameters_unsupported_renderer_should_fail(self):
        with self.assertRaises(ValueError) as thrown_exception:
            validate_parameters('.fbx', 'unsupported')

        self.assertEqual("UNKNOWN RENDERER TYPE, only console, directx and opengl are possible",
                         thrown_exception.exception.args[0])
