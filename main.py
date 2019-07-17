import pyautogui
import keyboard
import winsound
import os

images = {
    "buy" : "images/buy.png",
    "cantbuy1" : "images/cantbuy1.png",
    "cantbuy2" : "images/cantbuy2.png",
    "cantpay" : "images/cantpay.png",
    "cantprison" : "images/cantprison.png",
    "deny" : "images/deny.png",
    "drop" : "images/drop.png",
    "dropcube" : "images/dropcube.png",
    "pay" : "images/pay.png",
    "decline" : "images/decline.png",
    "surrender" : "images/surrender.png",
    "sell" : "images/sell.png"
}

brands = [
    "brands/adidas.png",
    "brands/american.png",
    "brands/apple.png",
    "brands/audi.png",
    "brands/boss.png",
    "brands/british.png",
    "brands/chanel.png",
    "brands/facebook.png",
    "brands/fanta.png",
    "brands/ford.png",
    "brands/holidayinn.png",
    "brands/kfc.png",
    "brands/lacoste.png",
    "brands/landrover.png",
    "brands/lufthansa.png",
    "brands/mercedes.png",
    "brands/nokia.png",
    "brands/novotel.png",
    "brands/puma.png",
    "brands/radissonblu.png",
    "brands/rockstar.png"
]


def click(ptr, duration=.5):
    if ptr is not None:
        center = pyautogui.center(ptr)
        pyautogui.moveTo(center[0], center[1], duration=.5)
        pyautogui.leftClick()


def trytosell():
    for brand in brands:
        ptr = pyautogui.locateOnScreen(brand, grayscale=True, confidence=.7)
        if ptr is not None:
            ptr2 = pyautogui.locateOnScreen(images['sell'], confidence=.7)
            if ptr2 is not None:
                click(ptr2, duration=0)
                return True
    return False


def bot():
    global images
    counter = 0
    prisontick = False
    ptr = pyautogui.locateOnScreen(images['decline'], confidence=.7)
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['deny'], confidence=.7)
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['drop'], confidence=.7)
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['buy'], confidence=.7)
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['pay'], confidence=.7)
    if ptr is not None:
        counter = 0
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['surrender'], confidence=.7)
    click(ptr)
    ptr = pyautogui.locateOnScreen(images['cantprison'], confidence=.7)
    if ptr is not None:
        prisontick = True
        ptr = pyautogui.locateOnScreen(images['dropcube'], confidence=.7)
        click(ptr)
    ptr = pyautogui.locateOnScreen(images['cantbuy1'], confidence=.7)
    if ptr is not None:
        ptr = pyautogui.locateOnScreen(images['cantbuy2'], confidence=.7)
        click(ptr)
    ptr = pyautogui.locateOnScreen(images['cantpay'], confidence=.7)
    if ptr is not None and not prisontick:
        winsound.Beep(3000, 1000)


def main():
    while True:
        if keyboard.is_pressed(';'):
            break
        bot()


main()
