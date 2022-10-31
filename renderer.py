class RendererInterface:
    def render_model(self, model):
        pass

class RendererMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class RendererConsole(RendererInterface, metaclass=RendererMeta):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by ConsoleRenderer")


class RendererDirectx(RendererInterface, metaclass=RendererMeta):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by DirectXRenderer")


class RendererOpengl(RendererInterface, metaclass=RendererMeta):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by OpenglRenderer")
