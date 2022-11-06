import time
import pyglet


def audio_play(frequency):
    if frequency == 261.63:
        sound = pyglet.resource.media("pipa_C.wav", streaming=False)
        sound.play()
        time.sleep(0.1)
    if frequency == 293.66:
        sound = pyglet.resource.media("pipa_D.wav", streaming=False)
        sound.play()
        time.sleep(0.1)
    if frequency == 329.63:
        sound = pyglet.resource.media("pipa_E.wav", streaming=False)
        sound.play()
        time.sleep(0.1)
    if frequency == 392.00:
        sound = pyglet.resource.media("pipa_G.wav", streaming=False)
        sound.play()
        time.sleep(0.1)
    if frequency == 440.00:
        sound = pyglet.resource.media("pipa_A.wav", streaming=False)
        sound.play()
        time.sleep(0.1)


