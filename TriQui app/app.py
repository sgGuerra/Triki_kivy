"""
To Do :
1. Pintar las 9 casillas
2. Pintar X al presionar el boton
3. Pintar X o la O alternadamente
4. Convertir el juego en 4 en raya (tablero de 10 x 10)
5. Detectar el ganador
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TrikiApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turno: bool = False 
        self.seleccion_x: list =  []
        self.seleccion_o: list =  []


    def build(self):
        tablero = BoxLayout(orientation = 'horizontal')
        
        
        for i in range(3):
            columnas = BoxLayout(orientation = 'vertical')
            tablero.add_widget( columnas)
            
            for j in range(3):
            
                casilla = Button(font_size = '50', text= f"{i,j}")
                columnas.add_widget(casilla)

                casilla.bind(on_press = self.seleccionar)

        return tablero

    def seleccionar( self, sender):
        print(f"Presionaste la casilla #{sender.text}")
        if self.turno:
            sender.text = 'X'
        else:
            sender.text = 'O'
        
        self.turno = not self.turno




if __name__ == '__main__':
    TrikiApp().run()