import os
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


if __name__ == "__main__":
    rendered_models = []
    while True:
        file, render_type = input("Input file and render type\n").split()
        print('--------')
        file_name, file_extension = os.path.splitext(file)
        parser, renderer = validate_parameters(file_extension, render_type)
        print(f"Parser id - {id(parser)}, Renderer id - {id(renderer)}")
        model = parser.parse_file('input_files/' + file_name + file_extension)
        print('--------')
        rendered_model = renderer.render_model(model)
        print(rendered_model)
        rendered_models.append([model, render_type])
        print('Rendered models list:')
        for item in rendered_models:
            print(item)
        print("--------------------------")
