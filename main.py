from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


class MainApp(MDApp):

    def cambia_texto(self):
        # self.root.ids.cajatexto.text = "aaaaa"
        self.root.ids.listado.text = self.root.ids.cajatexto.text

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return (


            MDScreen(


                MDLabel(
                    text="Búsqueda de artículos",
                    bold=True,
                    font_style="H6",
                    pos_hint={"center_x": 0.9, "center_y": 0.95},

                ),

                MDTextField(
                    id='cajatexto',
                    hint_text="Ingrese detalle a buscar",
                    mode="rectangle",
                    required=True,
                    helper_text_mode="on_error",
                    size_hint_x=.8,
                    pos_hint={"center_x": 0.5, "center_y": 0.85},
                    line_color_normal="green"

                ),

                MDRectangleFlatButton(
                    icon="archive",
                    text="  Archivos ",
                    pos_hint={"center_x": 0.5, "center_y": 0.2},
                    font_size=70,
                    md_bg_color="#674EF1",

                ),
                MDRectangleFlatButton(
                    id='listado',
                    icon="list-box",
                    text="  Listados ",
                    pos_hint={"center_x": 0.5, "center_y": 0.4},
                    font_size=70,
                    md_bg_color="#4EF1A2",
                ),
                MDRectangleFlatButton(
                    icon="run",
                    text=" Procesos ",
                    pos_hint={"center_x": 0.5, "center_y": 0.6},
                    font_size=70,
                    md_bg_color="#478C6B",
                    on_press=lambda r: self.cambia_texto()
                )
            )
        )


if __name__ == '__main__':
    MainApp().run()
