from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#07111F")


class IGRISApp(App):
    def build(self):
        principal = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        titulo = Label(
            text="[b]I G R I S[/b]",
            markup=True,
            font_size="36sp",
            color=get_color_from_hex("#00E5FF"),
            size_hint=(1, 0.18)
        )

        nucleo = Label(
            text="◉",
            font_size="100sp",
            color=get_color_from_hex("#00E5FF"),
            size_hint=(1, 0.35)
        )

        self.estado = Label(
            text="SISTEMA INICIADO",
            font_size="16sp",
            color=get_color_from_hex("#00E5FF")
        )

        self.conversacion = Label(
            text="Saludos. Soy IGRIS.\nEstoy preparado para comenzar.",
            font_size="17sp",
            halign="center",
            valign="middle"
        )
        self.conversacion.bind(
            size=lambda obj, size: setattr(obj, "text_size", size)
        )

        self.entrada = TextInput(
            hint_text="Escribe un mensaje...",
            multiline=False,
            size_hint=(1, 0.12)
        )

        boton = Button(
            text="ENVIAR",
            size_hint=(1, 0.12),
            background_normal="",
            background_color=get_color_from_hex("#007C91")
        )
        boton.bind(on_press=self.enviar)

        principal.add_widget(titulo)
        principal.add_widget(nucleo)
        principal.add_widget(self.estado)
        principal.add_widget(self.conversacion)
        principal.add_widget(self.entrada)
        principal.add_widget(boton)

        return principal

    def enviar(self, instancia):
        mensaje = self.entrada.text.strip()

        if mensaje:
            self.conversacion.text = "Mensaje recibido:\n" + mensaje
            self.entrada.text = ""
            self.estado.text = "INTERFAZ FUNCIONANDO"


if __name__ == "__main__":
    IGRISApp().run()
