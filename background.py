import random
import pygame as pg 
import pygamebg

(sirina, visina) = (200, 200)
prozor = pygamebg.open_window(sirina, visina, "Boja pozadine")

def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def crtaj():
    boja = nasumicna_boja() #nasumicno odredjujemo boju pozadine
    prozor.fill(boja) #bojimo pozadinu prozora

# pokrecemo animaciju tako sto funkciju crtaj pozivamo 4 puta u sekundi
pygamebg.frame_loop(4, crtaj)