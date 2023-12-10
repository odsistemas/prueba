from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

KV = """
ScreenManager:
    DemoPage:
    
    ClientsTable:


<DemoPage>:
    MDLabel:
        text:"Búsqueda de artículos"
        bold:True
        
        pos_hint:{"center_x": 0.9, "center_y": 0.95}
       
    MDTextField:
        id:'cajatexto'
        hint_text:"Ingrese detalle a buscar"
        mode:"rectangle"
        required:True
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        
        
    MDRaisedButton:
        text: " Listar "
        size_hint: 0.5, 0.06
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
       
            
            
<ClientsTable>:
    name: 'Clientstable'
 
    MDRaisedButton:
        text: " Fin "
        size_hint: 0.5, 0.06
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        on_press: app.stop()
            
 
 
 
 """


class ClientsTable(Screen):
    def load_table(self):
        layout = AnchorLayout()

        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.55, 'center_x': 0.5},
            size_hint=(0.9, 0.75),
            use_pagination=True,
            check=True,
            rows_num=10,
            column_data=[
                ("No.", dp(30)),
                ("Descripcion", dp(60)),
                ("Precio", dp(30)),
            ],
            row_data=[
                (f"{i + 1}", "Descripcion "+f"{i + 1}", "999.99")
                for i in range(50)], )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class DemoPage(Screen):
    pass


sm = ScreenManager()

sm.add_widget(DemoPage(name='demopage'))
sm.add_widget(ClientsTable(name='Clientstable'))


class Main(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(KV)
        return screen


if __name__ == "__main__":
    Main().run()
