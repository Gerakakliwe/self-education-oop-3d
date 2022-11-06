import json


class ParserInterface:
    def parse_file(self, file_name: str):
        pass


class ParserMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Parser3ds(ParserInterface, metaclass=ParserMeta):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)
            model['parser'] = 'Parser3ds'

        print_parsed_info(model)
        return model


class ParserFbx(ParserInterface, metaclass=ParserMeta):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)
            model['parser'] = 'ParserFbx'

        print_parsed_info(model)
        return model


class ParserCollada(ParserInterface, metaclass=ParserMeta):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)
            model['parser'] = 'ParserCollada'

        print_parsed_info(model)
        return model


def print_parsed_info(model):
    print(
        f"Model name - {model.get('name')}, Materials used - {model.get('materials')}, Color - {model.get('color')}, Parser - {model.get('parser')}")
