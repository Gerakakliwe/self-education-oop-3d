class RendererInterface:
    def render_model(self, model):
        pass


class RendererConsole(RendererInterface):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by ConsoleRenderer")


class RendererDirectx(RendererInterface):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by DirectXRenderer")


class RendererOpengl(RendererInterface):
    def render_model(self, model):
        print(f"Model {model} was successfully rendered by OpenglRenderer")
