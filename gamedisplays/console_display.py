#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdout
import os
from colorama import Fore, Back
import platform

class StringSimulator(object):
    def __init__(self, length, pin=0):
        self.length = length
        self.pin = pin
        self.pixel_array = [(0, 0, 0) for x in range(length)]
        if platform.system() == 'Linux':
            os.system('setterm -cursor off')

    def __del__(self):
        if platform.system() == 'Linux':
            os.system('setterm -cursor on')
        print ""

    def set_pixel_color(self, index, red, green, blue):
        self.pixel_array[index] = (red, green, blue)

    def clear_display(self):
        for x in range(self.length):
            self.pixel_array[x] = (0, 0, 0)

    def update_display(self):
        output_string = ""
        for i in range(self.length):
            term_color = self._get_term_color(self.pixel_array[i])
            if term_color == Fore.RESET:
                character = "."
            else:
                character = "█"
            output_string += term_color + character
        stdout.write("\r" + output_string)
        stdout.flush()

    @staticmethod
    def _get_term_color(color_tuple):
        red = color_tuple[0]
        green = color_tuple[1]
        blue = color_tuple[2]

        if red > 127 and green > 127 and blue > 127:
            term_color = Fore.WHITE
        elif red > 127 and blue > 127:
            term_color = Fore.MAGENTA
        elif red > 127 and green > 127:
            term_color = Fore.YELLOW
        elif blue > 127 and green > 127:
            term_color = Fore.CYAN
        elif red > 127:
            term_color = Fore.RED
        elif green > 127:
            term_color = Fore.GREEN
        elif blue > 127:
            term_color = Fore.BLUE
        else:
            term_color = Fore.RESET

        return term_color

if __name__ == "__main__":
    from time import sleep

    def test_display():
        sim = StringSimulator(16)
        sim.clear_display()
        sim.update_display()
        for i in range(0, 16):
            sim.set_pixel_color(i, 255, 255, 255)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 0, 255, 255)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 255, 0, 255)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 255, 255, 0)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 0, 0, 255)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 255, 0, 0)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 0, 255, 0)
            sim.update_display()
            sleep(0.1)
        for i in range(0, 16):
            sim.set_pixel_color(i, 0, 0, 0)
            sim.update_display()
            sleep(0.1)

    test_display()

