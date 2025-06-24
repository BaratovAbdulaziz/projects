from ursina import *

app = Ursina()
Land= Entity(model="cube", color= color.yellow,scale=1, texture="brick",rotation(1,2,2))
EditorCamera()

app.run()
