import wx
import sys
class MainWindow(wx.Frame):
    # Creamos nuestra ventana a partir de un Frame
    def __init__(self):
        # Con super ejecutamos su propio constructor y le pasamos los argumentos
        # Así se crea la ventana en su propia instancia self
        super().__init__(None, wx.ID_ANY, size=(200, 100))
        button = wx.Button(self, wx.ID_ANY, "Hola")
        button.Bind(wx.EVT_BUTTON, self.hola)
        # Finalmente mostramos la ventana
        self.Show(True)
    # Se requiere un parámetro de argumentos indeterminados en los métodos
    def hola(self, *args):
        print("¡Hola mundo!")
# Creamos la aplicación, la ventana e iniciamos el bucle
print("\n================================")
print(sys.argv)
app = wx.App()
window = MainWindow()
app.MainLoop()
