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
        return f"Model {model.get('name')} parsed by {model.get('parser')} was successfully rendered by ConsoleRenderer"


class RendererDirectx(RendererInterface, metaclass=RendererMeta):
    def render_model(self, model):
        return f"Model {model.get('name')} parsed by {model.get('parser')} was successfully rendered by DirectxRenderer"


class RendererOpengl(RendererInterface, metaclass=RendererMeta):
    def render_model(self, model):
        return f"Model {model.get('name')} parsed by {model.get('parser')} was successfully rendered by OpenglRenderer"
