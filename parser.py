import json


class ParserInterface:
    def parse_file(self, file_name: str):
        pass


class Parser3ds(ParserInterface):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)

        print_parsed_info(model)
        return model


class ParserFbx(ParserInterface):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)

        print_parsed_info(model)
        return model


class ParserCollada(ParserInterface):
    def parse_file(self, file_name: str):
        with open(file_name, 'r') as f:
            model = json.load(f)

        print_parsed_info(model)
        return model


def print_parsed_info(model):
    print(f"Model name - {model.get('name')}")
    print(f"Materials used - {model.get('materials')}")
    print(f"Color - {model.get('color')}")
