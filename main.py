# Program to explain how to create tabbed panel App in kivy

# import kivy module
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.scatter import Scatter
from kivy.uix.recycleview import RecycleView
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# to use this must have to import it

# Floatlayout allows us to place the elements
# relatively based on the current window
# size and height especially in mobiles

# Create Tabbed class
# Define the Recycleview class which is created in .kv file


class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': 'Código de artículo:' +
                      str(x) + '\nDescripcion:Artículo '+str(x)+"\nPrecio:"+str(x+100)} for x in range(2)]


class Tab(TabbedPanel):
    def procesando(self):
        self.ids.lprocesando.text = "Procesando artículos..."

    def salida(self):
        exit()

    def recarga(self):
        def __init__(self, **kwargs):
            super(ExampleViewer, self).__init__(**kwargs)
            self.data = [{'text': 'Código de artículo:' +
                          str(x) + '\nDescripcion:Artículo '+str(x)+"\nPrecio:"+str(x+100)} for x in range(30)]
        self.ids.lprocesando.text = "anda..."
# create App class


class MainApp(App):
    def build(self):

        return Tab()


# run the App
if __name__ == '__main__':
    MainApp().run()
