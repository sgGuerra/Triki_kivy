from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class TriQuiApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turno: bool = False 
        self.seleccion_x: list =  []
        self.seleccion_o: list =  []
        self.contador_x: int = 0
        self.contador_o: int = 0
    
    def build(self):
        
        # Layout principal vertical
        fondo = BoxLayout(orientation='vertical')
        
        # Contenedor de contadores (ocupa 10% de la altura)
        base = BoxLayout(
            orientation='horizontal', 
            size_hint=(1, 0.1),      
            pos_hint={"center_x": 0.5}
        )
        
        # Contadores
        contador_x = Label(text=f'Contador X = {self.contador_x}', size_hint=(0.5, 1))
        contador_o = Label(text=f'Contador O = {self.contador_o}', size_hint=(0.5, 1))
        base.add_widget(contador_x)
        base.add_widget(contador_o)
        
        # Tablero (ocupa 90% de la altura)
        self.tablero = GridLayout(cols=3, size_hint=(1, 0.9))
        
        # Agregar widgets al layout principal
        fondo.add_widget(base)
        fondo.add_widget(self.tablero)
        
        opciones = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, 0.1))
        reiniciar = Button(text='Reiniciar', size_hint=(0.3, 0.8), background_color=(0.2, 0.6, 1, 1))
        reiniciar.bind(on_press = self.reiniciar)
        opciones.add_widget(reiniciar)
        
        fondo.add_widget(opciones)
        
        # Botones del tablero
        for i in range(9):
            casilla = Button(font_size=50)
            self.tablero.add_widget(casilla)
            casilla.bind(on_press = self.seleccionar)
        return fondo


    def seleccionar( self, sender):
        print(f"Presionaste la casilla #{self.tablero.children.index(sender)}")
        indice = self.tablero.children.index(sender)
        
        if self.turno:
            sender.text = 'X'
            sender.disabled = True
            sender.background_color = (0.2, 0.6, 1, 1)
            self.seleccion_x.append(indice)
            print(self.seleccion_x)
        else:
            sender.text = 'O'
            sender.disabled = True
            sender.background_color = (0.5, 0, 0, 1)  
            self.seleccion_o.append(indice)
            print(self.seleccion_o)
           
        self.turno = not self.turno
        
    def reiniciar(self, sender):
        for casilla in self.tablero.children:
            casilla.text = ''
            casilla.disabled = False
            casilla.background_color = (1, 1, 1 ,1)
        self.seleccion_o.clear()
        self.seleccion_x.clear()
        self.turno = False
    
    def es_ganador(self, sender):
        pass
    
    

if __name__ == '__main__': 
    TriQuiApp().run()