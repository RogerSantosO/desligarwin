import os
import PySimpleGUI as sg

class DesligarPc:

    def __init__(self):
        self.tempo = 0

    def iniciar(self):
        layout = [
            [sg.Text('Escolha uma opção de tempo para desligar o computador.')],
            [sg.Button('30 minutos.')],
            [sg.Button('1 hora.')],
            [sg.Button('2 horas.')],
            [sg.Button('Cancelar desligamento.')],
        ]
        self.janela = sg.Window('Desligar!',layout=layout)
        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                if self.evento == '30 minutos.':
                    self.Desligar(1800)
                if self.evento == '1 hora.':
                    self.Desligar(3600)
                if self.evento == '2 horas.':
                    self.Desligar(7200)
                if self.evento == 'Cancelar desligamento.':
                    os.system('shutdown -a')
                if self.evento == sg.WINDOW_CLOSED:
                    break
        except:
            print('ocorreu um erro')
    def Desligar(self, tempo):
        os.system('shutdown -a')
        os.system(f'shutdown -s -t {tempo}')


desligar = DesligarPc()
desligar.iniciar()
