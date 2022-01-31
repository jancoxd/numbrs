import config
import gc

print(gc.mem_free())

from machine import Pin

print(gc.mem_free())

from neopixel import NeoPixel
import urequests

print(gc.mem_free())

import json

print(gc.mem_free())

TICKER_URL = 'https://www.bitstamp.net/api/v2/ticker/'
pixelcount = 35
pixels = NeoPixel(Pin(13), pixelcount, brightness=config.brightness)
color = (255, 255, 255)


# Function for splitting  number in to Singletons
def mid(s, offset, amount):
    return s[offset - 1:offset + amount - 1]


def getprices(pair):
    try:
        r = urequests.get(TICKER_URL + pair).content
        dict = json.loads(r)
        return dict['last']
    except Exception as e:
        return "0"
        print(e)


def fct1(led):
    led = int(led)
    # Define the right number of the starting Led, 7 numbers per LED Strip.
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = (0, 0, 0)
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = (0, 0, 0)
    pixels[1 + (7 * led)] = (0, 0, 0)
    pixels[0 + (7 * led)] = (0, 0, 0)
    pixels.write()


def fct2(led):
    led = int(led)

    # Define the right number of the starting Led, 7 numbers per LED Strip.
    pixels[6 + (7 * led)] = color
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = (0, 0, 0)
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = (0, 0, 0)
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct3(led):
    led = int(led)

    # Define the right number of the starting Led, 7 numbers per LED Strip.
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = (0, 0, 0)
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct4(led):
    led = int(led)

    # Define the right number of the starting Led, 7 numbers per LED Strip.
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = (0, 0, 0)
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = (0, 0, 0)
    pixels[1 + (7 * led)] = color
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct5(led):
    led = int(led)

    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = (0, 0, 0)
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = color
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct6(led):
    led = int(led)

    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = (0, 0, 0)
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = (0, 0, 0)
    pixels[0 + (7 * led)] = (0, 0, 0)
    pixels.write()


def fct7(led):
    led = int(led)

    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = (0, 0, 0)
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = (0, 0, 0)
    pixels[0 + (7 * led)] = (0, 0, 0)
    pixels.write()


def fct8(led):
    led = int(led)

    pixels[6 + (7 * led)] = color
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = color
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct9(led):
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = color
    pixels[0 + (7 * led)] = color
    pixels.write()


def fct0(led):
    pixels[6 + (7 * led)] = color
    pixels[5 + (7 * led)] = color
    pixels[4 + (7 * led)] = color
    pixels[3 + (7 * led)] = color
    pixels[2 + (7 * led)] = color
    pixels[1 + (7 * led)] = color
    pixels[0 + (7 * led)] = (0, 0, 0)
    pixels.write()


def fct(led):
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels[1 + (7 * led)] = color
    pixels[2 + (7 * led)] = (0, 0, 0)
    pixels[3 + (7 * led)] = (0, 0, 0)
    pixels[4 + (7 * led)] = color
    pixels[5 + (7 * led)] = (0, 0, 0)
    pixels[6 + (7 * led)] = (0, 0, 0)
    pixels.write()


def getnumbers(loc):
    # Split Pairs into single numbers
    number = mid(pair, loc, 1)

    return number


def init():
    pair = getprices(config.basevalue)
    run = config.run

    if run:
        first = str(mid(pair, 1, 1))
        sec = str(mid(pair, 2, 1))
        third = str(mid(pair, 3, 1))
        fourth = str(mid(pair, 4, 1))
        if config.basevalue == "BTCUSD":
            fifth = str(mid(pair, 5, 1))

        second = "fct"
        function_name = second + first
        result = eval(function_name + "(4)")
        print(result)

        function_name = second + sec
        result = eval(function_name + "(3)")
        print(result)

        function_name = second + third
        result = eval(function_name + "(2)")
        print(result)

        function_name = second + fourth
        result = eval(function_name + "(1)")
        print(result)

        if config.basevalue == "BTCUSD":
            function_name = second + fifth
            result = eval(function_name + "(0)")
            print(result)

        print(first)
        print(sec)
        print(third)
        print(fourth)
        if config.basevalue == "BTCUSD":
            print(fifth)

def clear():
    for number in range(1, pixelcount):
        print(number)
        pixels[number] = (0, 0, 0)
        pixels.write()




