class ParserInterface:
    def parse_file(self, file_name: str):
        pass


class Parser3ds(ParserInterface):
    def parse_file(self, file_name: str):
        print(f"File {file_name} was successfully parsed by 3dsParser")
        model = 'model_' + file_name
        return model


class ParserFbx(ParserInterface):
    def parse_file(self, file_name: str):
        print(f"File {file_name} was successfully parsed by FbxParser")
        model = 'model_' + file_name
        return model


class ParserCollada(ParserInterface):
    def parse_file(self, file_name: str):
        print(f"File {file_name} was successfully parsed by ColladaParser")
        model = 'model_' + file_name
        return model
