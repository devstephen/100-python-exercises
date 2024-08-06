import pyglet


window = pyglet.window.Window()
label = pyglet.text.Label("Hello World", font_name="Arial", font_size=36,
                           x=window.width // 2, y=window.height // 2, anchor_x="center", anchor_y="center", color=(0, 0, 255))
@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()