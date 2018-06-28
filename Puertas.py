import winsound
from random import randint
from time import sleep

import wx

ganarcambio=0
ganarsincambio=0
perdercambio=0
perdersincambio=0
abierta=0
actual=0
otra=0
premio=0
turno = False

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        global turno
        wx.Frame.__init__(self,*args,**kwargs)
        self.Show()
        blanco = wx.Colour(255, 255, 255)
        self.SetBackgroundColour(blanco)
        panel = wx.Panel(self, -1, pos=(0, 0), size=(800, 600))
        panel.SetBackgroundColour(blanco)

        cabra1 = wx.StaticBitmap(self, -1, wx.Bitmap('cabra.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(88, 35), size=(125, 200))

        cabra2 = wx.StaticBitmap(self, -1, wx.Bitmap('cabra.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(340, 35), size=(125, 200))

        cabra3 = wx.StaticBitmap(self, -1, wx.Bitmap('cabra.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(585, 35), size=(125, 200))

        carro1 = wx.StaticBitmap(self, -1, wx.Bitmap('carro.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(0, 35), size=(200, 200))

        carro2 = wx.StaticBitmap(self, -1, wx.Bitmap('carro.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(252, 35), size=(200, 200))

        carro3 = wx.StaticBitmap(self, -1, wx.Bitmap('carro.png', wx.BITMAP_TYPE_ANY),
                                 pos=wx.Point(497, 35), size=(200, 200))
        # Puertas
        puerta1 = wx.BitmapButton(panel, -1, wx.Bitmap('puerta.png', wx.BITMAP_TYPE_ANY),
                                  wx.Point(88, 35), wx.Size(120, 200), 0)

        puerta2 = wx.BitmapButton(panel, -1, wx.Bitmap('puerta.png', wx.BITMAP_TYPE_ANY),
                                  wx.Point(340, 35), wx.Size(120, 200), 0)

        puerta3 = wx.BitmapButton(panel, -1, wx.Bitmap('puerta.png', wx.BITMAP_TYPE_ANY),
                                  wx.Point(585, 35), wx.Size(120, 200), 0)

        change = wx.BitmapButton(panel, -1, wx.Bitmap('checked.png', wx.BITMAP_TYPE_ANY),
                                 wx.Point(290, 340), wx.Size(64, 64), 0)

        do_not_change = wx.BitmapButton(panel, -1, wx.Bitmap('cross.png', wx.BITMAP_TYPE_ANY),
                                        wx.Point(440, 340), wx.Size(64, 64), 0)

        reset = wx.BitmapButton(panel, -1, wx.Bitmap('refreshing1.png', wx.BITMAP_TYPE_ANY),
                                wx.Point(368, 340), wx.Size(64, 64), 0)
        reset.SetBackgroundColour((0,0,0))
        texto = wx.StaticText(self, id=-1, label="Elige una puerta para iniciar el juego. ", pos=(200, 265),
                              size=(400, 50), style=wx.ALIGN_CENTRE)
        font = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        texto.SetFont(font)

        Ganadas = wx.StaticText(self, id=-1, label=("Partidas ganadas cambiando puerta: %d" % ganarcambio), pos=(30, 475),
                                size=(250, 50), style=wx.ALIGN_LEFT)

        Perdidas = wx.StaticText(self, id=-1, label="Partidas perdidas cambiando puerta: %d" % perdercambio, pos=(550, 475),
                                 size=(250, 50), style=wx.ALIGN_LEFT)

        Ganadas2 = wx.StaticText(self, id=-1, label="Partidas ganadas sin cambio de puerta: %d" % ganarsincambio, pos=(30, 525),
                                 size=(250, 50), style=wx.ALIGN_LEFT)

        Perdidas2 = wx.StaticText(self, id=-1, label="Partidas perdidas sin cambio de puerta: %d" % perdersincambio,
                                  pos=(550, 525), size=(250, 50), style=wx.ALIGN_LEFT)

        change.Hide()
        do_not_change.Hide()
        reset.Hide()
        cabra1.Hide()
        cabra2.Hide()
        cabra3.Hide()
        carro1.Hide()
        carro2.Hide()
        carro3.Hide()
       
        def reset_listener(self):
            global abierta;
            global actual
            global otra
            global premio
            global turno

            reset.Hide()
            cabra1.Hide()
            cabra2.Hide()
            cabra3.Hide()
            carro1.Hide()
            carro2.Hide()
            carro3.Hide()
            puerta1.Show()
            puerta1.Enable(True)
            puerta2.Show()
            puerta2.Enable(True)
            puerta3.Show()
            puerta3.Enable(True)
            turno = False

            texto.SetLabel("Elige una puerta para empezar a jugar:")

            abierta=0
            actual=0
            otra=0
            premio=0

        def change_door(self):
            global perdercambio
            global ganarcambio
            global imagen
            global actual
            global premio
            global abierta

            change.Hide()
            do_not_change.Hide()

            duplicado = actual

            if duplicado==1:
                    puerta1.Enable(True)
            if duplicado==2:
                    puerta2.Enable(True)
            if duplicado==3:
                    puerta3.Enable(True)
            actual = randint(1, 3)
            while actual == abierta or actual == duplicado:
                    actual=randint(1, 3)
            if actual==1:
                    puerta1.Enable(False)
                    
            if actual==2:
                    puerta2.Enable(False)
            if actual==3:
                    puerta3.Enable(False)
                    
            texto.SetLabel("Cambiaste la puerta %d por la puerta %d" % (duplicado, actual))
            sleep(2.2)
            winsound.PlaySound("door.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            print("El actual es %d" % actual)
            print("El premio es %d" % premio)
            print ("El abierta es %d" % abierta)
            
            if actual==1:
                    puerta1.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro1.Show()
                        ganarcambio= ganarcambio + 1
                        Ganadas.SetLabel("Partidas ganadas cambiando puerta: %d" % ganarcambio)
                        
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra1.Show()
                        perdercambio= perdercambio + 1
                        Perdidas.SetLabel("Partidas perdidas cambiando puerta: %d" % perdercambio)
            if actual==2:
                    puerta2.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro2.Show()
                        ganarcambio= ganarcambio + 1
                        Ganadas.SetLabel("Partidas ganadas cambiando puerta: %d" % ganarcambio)
                        
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra2.Show()
                        perdercambio= perdercambio + 1
                        Perdidas.SetLabel("Partidas perdidas cambiando puerta: %d" % perdercambio)
            if actual==3:
                    puerta3.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro3.Show()
                        ganarcambio= ganarcambio + 1
                        Ganadas.SetLabel("Partidas ganadas cambiando puerta: %d" % ganarcambio)
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra3.Show()
                        perdercambio= perdercambio + 1
                        Perdidas.SetLabel("Partidas perdidas cambiando puerta: %d" % perdercambio)
            reset.Show()

        def do_not_change_door(self):
            global perdersincambio
            global ganarsincambio
            change.Hide()
            do_not_change.Hide()
            texto.SetLabel("Elegiste quedarte con la puerta %d." % actual)
            print("Nueva partida")
            print("El actual es %d" % actual)
            print("El premio es %d" % premio)
            print ("El abierta es %d" % abierta)
            sleep(2.2)
            if actual==1:
                    puerta1.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro1.Show()
                        ganarsincambio= ganarsincambio + 1
                        Ganadas2.SetLabel("Partidas ganadas sin cambio de puerta: %d" % ganarsincambio)
                        
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra1.Show()
                        perdersincambio= perdersincambio + 1
                        Perdidas2.SetLabel("Partidas perdidas sin cambio de puerta: %d" % perdersincambio)
            if actual==2:
                    puerta2.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro2.Show()
                        ganarsincambio= ganarsincambio + 1
                        Ganadas2.SetLabel("Partidas ganadas sin cambio de puerta: %d" % ganarsincambio)
                        
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra2.Show()
                        perdersincambio= perdersincambio + 1
                        Perdidas2.SetLabel("Partidas perdidas sin cambio de puerta: %d" % perdersincambio)
                  
            if actual==3:
                    puerta3.Hide();
                    if actual==premio:
                        texto.SetLabel("¡Buena opción! Encontraste el premio.")
                        carro3.Show()
                        ganarsincambio= ganarsincambio + 1
                        Ganadas2.SetLabel("Partidas ganadas sin cambio de puerta: %d" % ganarsincambio)
                    else:
                        texto.SetLabel("Perdiste... Elegista la puerta de la cabra")
                        cabra3.Show()
                        perdersincambio= perdersincambio + 1
                        Perdidas2.SetLabel("Partidas perdidas sin cambio de puerta: %d" % perdersincambio)
            reset.Show()
            
            
        def timeout(abierta):
            texto.SetLabel("Observa que en la puerta %d esta la cabra." % abierta)
            sleep(2.2)
            timeout2(abierta)

        def timeout2(abierta):
            global actual
            global premio
            if actual == 1:
                texto.SetLabel("¿Deseas cambiar de puerta?")
            if actual == 2:
                texto.SetLabel("¿Deseas cambiar de puerta?")
            if actual == 3:
                texto.SetLabel("¿Deseas cambiar de puerta?")
            winsound.PlaySound("door.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            if abierta==1:
                    puerta1.Hide();
                    cabra1.Show()
            if abierta==2:
                    puerta2.Hide();
                    cabra2.Show()
            if abierta==3:
                    puerta3.Hide();
                    cabra3.Show()
            change.Show()
            do_not_change.Show()
            print("El actual es %d" % actual)
            print("El premio es %d" % premio)
            print("La abierta es %d" % abierta)

        def puertaA(usuario):
            global premio
            premio=randint(1, 3)
            global abierta
            abierta=randint(1, 3)
            while abierta==premio or abierta==usuario:
                    abierta=randint(1, 3)
            return abierta
                    
        def onpuerta1(self):
                global turno
                global actual
                global abierta
                turno = True
                actual=1
                abierta=puertaA(actual)
                texto.SetLabel("Elegista la puerta 1")
                puerta1.Disable()
                sleep(2.2)
                timeout(abierta)
                print(u"Has presionado el botón 1")

        def onpuerta2(self):
                global actual
                global abierta
                global turno
                turno = True
                actual=2
                abierta=puertaA(actual)
                texto.SetLabel("Elegiste la puerta 2")
                puerta2.Disable()
                sleep(2.2)
                timeout(abierta)
                print(u"Has presionado el botón 2")

        def onpuerta3(self):
                global actual
                global abierta
                global turno
                turno = True
                actual=3
                abierta=puertaA(actual)
                texto.SetLabel("Elegista la puerta 3")
                puerta3.Disable()
                sleep(2.2)
                timeout(abierta)
                print (u"Has presionado el botón 3")

        if turno is False:
            puerta1.Bind(wx.EVT_BUTTON, onpuerta1)
            puerta2.Bind(wx.EVT_BUTTON, onpuerta2)
            puerta3.Bind(wx.EVT_BUTTON, onpuerta3)

        change.Bind(wx.EVT_BUTTON, change_door)
        do_not_change.Bind(wx.EVT_BUTTON, do_not_change_door)
        reset.Bind(wx.EVT_BUTTON, reset_listener)


if __name__ == '__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, " Juego de las puertas", size=(800,600),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
    app.MainLoop()
