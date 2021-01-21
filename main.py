import pyautogui
from PIL import Image,ImageGrab
import time

pyautogui.FAILSAFE = True

def hit(key):
    pyautogui.keyDown(key)
    return

def collide(data):
    for i in range(300,415):
        for j in range(560,650):
            if data[i,j]>75 and data[i,j] < 200:
                hit("up")
                return
    return

if __name__ == '__main__':
    time.sleep(3)
    image = ImageGrab.grab().convert('L')


    data = image.load()

    while True:
        image = ImageGrab.grab().convert('L')

        data = image.load()
        collide(data)

    # Draw rectangle for cactus
    # for i in range(300,415):
    #     for j in range(566,650):
    #         data[i,j] = 75
    # # #
    # for i in range(300, 415):
    #     for j in range(415,566):
    #         data[i,j] = 110
    #
    # image.show()

