from parser import (
    Parser3ds,
    ParserFbx,
    ParserCollada
)
import unittest

EXPECTED_OUTPUT_FBX = {
    "name": "test",
    "materials": ["test"],
    "color": ["0", "0", "0"],
    "parser": "ParserFbx"
}

EXPECTED_OUTPUT_3DS = {
    "name": "test",
    "materials": ["test"],
    "color": ["0", "0", "0"],
    "parser": "Parser3ds"
}

EXPECTED_OUTPUT_COLLADA = {
    "name": "test",
    "materials": ["test"],
    "color": ["0", "0", "0"],
    "parser": "ParserCollada"
}


class TestParserMethods(unittest.TestCase):

    def test_ParserFbx(self):
        parser = ParserFbx()
        model = parser.parse_file('test.fbx')
        self.assertEqual(model, EXPECTED_OUTPUT_FBX)

    def test_Parser3ds(self):
        parser = Parser3ds()
        model = parser.parse_file('test.fbx')
        self.assertEqual(model, EXPECTED_OUTPUT_3DS)

    def test_ParserCollada(self):
        parser = ParserCollada()
        model = parser.parse_file('test.fbx')
        self.assertEqual(model, EXPECTED_OUTPUT_COLLADA)
