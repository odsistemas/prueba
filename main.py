from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Hola Odsistemas!!",
                    font_size=60,

                    pos_hint={"center_x": 0.5, "center_y": 0.5},

                ),

                MDRectangleFlatButton(
                    text="Hola Odsistemas 2!!",
                    font_size=60,

                    pos_hint={"center_x": 0.5, "center_y": 0.3},
                    md_bg_color="#1D641D",

                )


            )
        )


Main().run()
