#!/usr/bin/env python3

class Flower:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def return_inf(self):
        print("{} {}".format(self.color, self.name))

color = input("Kolor kwiatka: ")
name = input("Nazwa kwiatka: ")

flower = Flower(color, name)

flower.return_inf()