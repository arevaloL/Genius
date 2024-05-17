"""
Simulação do Genius: 
Saldos começam no 0
É sorteado um número (cor)
Jogador clica na cor (número)
Acertou, vai pra próxima e sorteia de novo
Errou, reseta pra 0
"""

from tkinter import *
import random
from time import *

largura = 500
altura = 500
lado = 100
initx = (largura / 2) - lado
inity = (altura / 2) - lado

modelo = [0]
usuario = [0]

def aumentaNivel():
    tmp = random.randint(1,4)
    modelo.append(tmp)

def quadrado(initx, inity, lado):
    return [initx, inity, initx + lado, inity, initx + lado, inity + lado, initx, inity + lado]

def green(event):
    print("Clicou no verde.")
    piscaGreen()
    usuario.append(1)

def red(event):
    print("Clicou no vermelho.")
    piscaRed()
    usuario.append(2)
    
def blue(event):
    print("Clicou no azul.")
    piscaBlue()
    usuario.append(3)

def yellow(event):
    print("Clicou no amarelo.")
    piscaYellow()
    usuario.append(4)

def piscaGreen():
    canvas.itemconfig("green", fill="#93e884")
    window.update()
    sleep(0.2)
    canvas.itemconfig("green", fill="#096304")
    window.update()
    
def piscaRed():
    canvas.itemconfig("red", fill="#d66d6d")
    window.update()
    sleep(0.2)
    canvas.itemconfig("red", fill="#630404")
    window.update()

def piscaBlue():
    canvas.itemconfig("blue", fill="#6d97d6")
    window.update()
    sleep(0.2)
    canvas.itemconfig("blue", fill="#0a2270")
    window.update()

def piscaYellow():
    canvas.itemconfig("yellow", fill="#d1d66d")
    window.update()
    sleep(0.2)
    canvas.itemconfig("yellow", fill="#5f6304")
    window.update()


window = Tk()
canvas = Canvas(window, width = largura, height = altura, bg='white')
canvas.pack()

canvas.create_polygon(quadrado(initx, inity, lado), fill="#096304", tags="green")
canvas.create_polygon(quadrado(initx + lado, inity, lado), fill="#630404", tags="red")
canvas.create_polygon(quadrado(initx, inity + lado, lado), fill="#0a2270", tags="blue")
canvas.create_polygon(quadrado(initx + lado, inity + lado, lado), fill="#5f6304", tags="yellow")

canvas.tag_bind("green", "<Button-1>", green)
canvas.tag_bind("red", "<Button-1>", red)
canvas.tag_bind("blue", "<Button-1>", blue)
canvas.tag_bind("yellow", "<Button-1>", yellow)
sleep(1)
while(True):

    r1 = len(usuario) == len(modelo)
    r2 = usuario[-1] == modelo[len(usuario)-1]

    if (r1 and r2):
        aumentaNivel()
        usuario = [0]
        sleep(1)
        for i in modelo:
            if i == 1:
                piscaGreen()

            elif i == 2:
                piscaRed()
                
            elif i == 3:
                piscaBlue()

            elif i == 4:
                piscaYellow()
            
            sleep(0.4)

    elif (not r2):
        print("PERDEU!")
        exit()

    canvas.after(50)
    window.update_idletasks()
    window.update()