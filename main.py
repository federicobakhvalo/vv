# This is a sample Python script.
import requests


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Test:
    def __init__(self, test=None):
        self.test = test

    def set(self, c):
        self.test = c

    def get(self):
        return 'hello'


ex = Test()
ex.set('f')
print(ex.get())
