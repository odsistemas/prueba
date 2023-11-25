from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDScreen:

    MDRaisedButton:
        id: button
        text: "Activa Menú Principal"
        pos_hint: {"center_x": .5, "center_y": .5}
        font_size:40
        on_release: app.menu.open()
    
    MDFlatButton:
        text: "Ing. Oscar Díaz Sistemas"
        font_size:40
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": .5, "center_y": .8}
        
        '''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [

            {
                "text": f"Archivo",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Archivo": self.menu_callback(x),
            },

            {
                "text": f"Listados",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Listados": self.menu_callback(x),
            },
            {
                "text": f"Procesos",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Procesos": self.menu_callback(x),
            },
            {
                "text": f"Fin",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Fin": self.menu_callback(x),
            }



        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
        )

    def menu_callback(self, text_item):
        if text_item == "Fin":
            quit()

    def build(self):
        return self.screen


Test().run()
