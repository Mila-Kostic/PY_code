import pygame as pg, pygamebg
prozor = pygamebg.open_window(200, 300, "PyGameBg")
prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("black"), (20, 20, 160, 160), 5)
pygamebg.wait_loop()
