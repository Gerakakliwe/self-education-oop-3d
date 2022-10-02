import os
from database import (
    create_table,
    insert_data
)
from parser import (
    Parser3ds,
    ParserFbx,
    ParserCollada
)
from renderer import (
    RendererConsole,
    RendererDirectx,
    RendererOpengl
)


def validate_parameters(file_extension, render_type):
    try:
        if file_extension == '.3ds':
            parser = Parser3ds()
        elif file_extension == '.fbx':
            parser = ParserFbx()
        elif file_extension == '.collada':
            parser = ParserCollada()
        else:
            raise ValueError("UNKNOWN FILE EXTENSION, only .3ds, .fbx and .collada are possible")

        if render_type == 'console':
            renderer = RendererConsole()
        elif render_type == 'directx':
            renderer = RendererDirectx()
        elif render_type == 'opengl':
            renderer = RendererOpengl()
        else:
            raise ValueError("UNKNOWN RENDERER TYPE, only console, directx and opengl are possible")

        return parser, renderer

    except ValueError as ve:
        print(ve)
        exit()


if __name__ == "__main__":
    create_table('database.db', 'data')
    while True:
        file, render_type = input("Input file and render type\n").split()
        file_name, file_extension = os.path.splitext(file)

        parser, renderer = validate_parameters(file_extension, render_type)

        model = parser.parse_file(file_name)
        renderer.render_model(model)
        insert_data('database.db', 'data', (model, render_type))
        print("--------------------------")
