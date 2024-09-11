import pgzrun

WIDTH=600
HEIGHT=600
TITLE="HELLO WORLD"
rect=Rect((200,200),(100,100))
def draw():
    screen.clear()
    screen.fill("pink")
    screen.draw.line((0,0),(250,300),"blue")
    screen.draw.circle((250,250),50,("red"))
    screen.draw.filled_circle((300,300),70,"purple")
    screen.draw.filled_rect((rect),("green"))
pgzrun.go()







