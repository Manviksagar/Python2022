import os
from abc import ABC, abstractmethod

import requests


class sa(ABC):
    @abstractmethod
    def sag(self):
        pass


class child(sa):

    def y(self):
        print("sagar")

    def sag(self):
        x = 1
        print("abstarct method")
        if x == 1:
            print('true', 'sag',
            x)

Cc = child()
Cc.y()
Cc.sag()
