import time
import pyglet


def audio_play(frequency):
    if frequency == 261.63:
        sound = pyglet.resource.media("dizi_C.wav", streaming=False)
        sound.play()
        time.sleep(0.5)
    if frequency == 293.66:
        sound = pyglet.resource.media("dizi_D.wav", streaming=False)
        sound.play()
        time.sleep(0.5)
    if frequency == 329.63:
        sound = pyglet.resource.media("dizi_E.wav", streaming=False)
        sound.play()
        time.sleep(0.5)
    if frequency == 392.00:
        sound = pyglet.resource.media("dizi_G.wav", streaming=False)
        sound.play()
        time.sleep(0.5)
    if frequency == 440.00:
        sound = pyglet.resource.media("dizi_A.wav", streaming=False)
        sound.play()
        time.sleep(0.5)


