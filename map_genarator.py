import random

import config
from btn_func import *
from utils import yol_var_mi_fonk, matrix_okuma
from PIL import Image, ImageTk  # Arkaplan resmini eklemek için PIL kullanıyoruz

import tkinter as tk


def resim_bastirici():
    print(c.harita_tip)
    if c.harita_tip == "boş" and c.harita_buyukluk == 5:
        c.resim_label.config(image=c.resim00)
    elif c.harita_tip == "seyrek" and c.harita_buyukluk == 5:
        c.resim_label.config(image=c.resim01)
    elif c.harita_tip == "taşlı" and c.harita_buyukluk == 5:
        c.resim_label.config(image=c.resim02)

    elif c.harita_tip == "boş" and c.harita_buyukluk == 7:
        c.resim_label.config(image=c.resim10)
    elif c.harita_tip == "seyrek" and c.harita_buyukluk == 7:
        c.resim_label.config(image=c.resim11)
    elif c.harita_tip == "taşlı" and c.harita_buyukluk == 7:
        c.resim_label.config(image=c.resim12)

    elif c.harita_tip == "boş" and c.harita_buyukluk == 9:
        c.resim_label.config(image=c.resim20)
    elif c.harita_tip == "seyrek" and c.harita_buyukluk == 9:
        c.resim_label.config(image=c.resim21)
    elif c.harita_tip == "taşlı" and c.harita_buyukluk == 9:
        c.resim_label.config(image=c.resim22)


def random_secici_fonk_5x5():
    a = random.randint(0, 100)
    if a <= 40:
        c.random_secici_liste[0] = 0
    elif 40 < a <= 80:
        c.random_secici_liste[0] = 1
    elif 80 < a:
        c.random_secici_liste[0] = 2


def tas_secici_fonk_5x5_seyrek():
    gecici_liste = []
    print("!!!!", c.random_secici_liste[0])
    if c.random_secici_liste[0] == 0:

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 2:

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def tas_secici_fonk_5x5_tasli():
    gecici_liste = []
    print("!!!!", c.random_secici_liste[0])

    if c.random_secici_liste[0] == 0:

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 2:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def random_secici_fonk_7x7():
    a = random.randint(0, 100)
    if a <= 50:
        c.random_secici_liste[0] = 0
    elif 50 < a <= 70:
        c.random_secici_liste[0] = 1
    elif 70 < a:
        c.random_secici_liste[0] = 2


def tas_secici_fonk_7x7_seyrek():
    gecici_liste = []
    print("!!!!", c.random_secici_liste[0])
    if c.random_secici_liste[0] == 0:

        for i in range(1):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(3):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1



    elif c.random_secici_liste[0] == 2:

        for i in range(2):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def tas_secici_fonk_7x7_tasli():
    gecici_liste = []
    print("!!!!", c.random_secici_liste[0])
    if c.random_secici_liste[0] == 0:

        for i in range(2):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(3):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1



    elif c.random_secici_liste[0] == 2:

        for i in range(3):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def random_secici_fonk_9x9():
    a = random.randint(0, 100)
    if a <= 35:
        c.random_secici_liste[0] = 0
    elif 35 < a <= 65:
        c.random_secici_liste[0] = 1
    elif 65 < a:
        c.random_secici_liste[0] = 2


def tas_secici_fonk_9x9_seyrek():
    gecici_liste = []
    print("!!!!", c.random_secici_liste[0])
    if c.random_secici_liste[0] == 0:

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1



    elif c.random_secici_liste[0] == 2:

        for i in range(3):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def tas_secici_fonk_9x9_tasli():
    gecici_liste = []

    if c.random_secici_liste[0] == 0:

        for i in range(3):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(6):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(6):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

    elif c.random_secici_liste[0] == 1:

        for i in range(4):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(5):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(5):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1



    elif c.random_secici_liste[0] == 2:

        for i in range(5):
            index_sec = [0, 1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2, 3, 4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [4, 5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1

        for i in range(5):
            index_sec = [7, 8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            c.matrix[sayi][sutun] = -1


def oyun_harita_7x7_fonk():
    c.buton_list = []
    tahta = tk.Tk()
    tahta.title("Köprü Bağlamaca")

    #tahta.resizable(False,False)  #ilk taraf x ekseni, 2. taraf y ekseni ile oynayıp oynanamayacağını belirliyor.
    tahta.geometry("1680x1050+500+200")  #Sol taraf açılır pencere boyutu, sağ taraf bilgisayarın neresinde açılacağı
    tahta.resizable(False, False)
    tahta.lift()
    tahta.attributes('-topmost', True)


    # Canvas oluştur ve arkaplan resmini yükle
    canvas = tk.Canvas(tahta, width=1680, height=1050)
    canvas.pack(fill="both", expand=True)

    # Arkaplan resmini yükle
    img_str = ""
    if c.oyun_sonu_tahta:
        img_str = "bg3.jpg"
    elif c.oyuncu == 1:
        img_str = "bg1.jpg"
    elif c.oyuncu == 2:
        img_str = "bg2.jpg"

    bg_image = Image.open("img/" + img_str)
    bg_image = bg_image.resize((1680, 1050), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Canvas'a arkaplan resmini yerleştir
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    gec_liste = []
    rex = 605
    rey = 145
    isimler_list = ["00", "01", "02", "03", "04", "05", "06",
                    "10", "11", "12", "13", "14", "15", "16",
                    "20", "21", "22", "23", "24", "25", "26",
                    "30", "31", "32", "33", "34", "35", "36",
                    "40", "41", "42", "43", "44", "45", "46",
                    "50", "51", "52", "53", "54", "55", "56",
                    "60", "61", "62", "63", "64", "65", "66"]
    fonks_list = [degistir00, degistir01, degistir02, degistir03, degistir04, degistir05, degistir06,
                  degistir10, degistir11, degistir12, degistir13, degistir14, degistir15, degistir16,
                  degistir20, degistir21, degistir22, degistir23, degistir24, degistir25, degistir26,
                  degistir30, degistir31, degistir32, degistir33, degistir34, degistir35, degistir36,
                  degistir40, degistir41, degistir42, degistir43, degistir44, degistir45, degistir46,
                  degistir50, degistir51, degistir52, degistir53, degistir54, degistir55, degistir56,
                  degistir60, degistir61, degistir62, degistir63, degistir64, degistir65, degistir66,
                  ]

    for i in range(49):
        if i % 7 == 0:
            if len(gec_liste) != 0:
                c.buton_list.append(gec_liste)
            gec_liste = []
            rex = 600
            rey += 85
        blok_00 = tk.Button(tahta, text=isimler_list[i], bg="blue", fg="white", width=8, height=5,
                            command=fonks_list[i])
        if c.oyun_sonu_tahta:
            blok_00.config(state=tk.DISABLED)
        blok_00.place(x=rex, y=rey)
        rex += 66
        gec_liste.append(blok_00)
    c.buton_list.append(gec_liste)
    for i in range(7):
        for j in range(7):
            if c.matrix[i][j] == -1:
                c.buton_list[i][j].config(text="Kara \nparçası!!!", bg="black", state=tk.DISABLED)

    if c.oyuncu == 1:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="1. Oyuncu:" + c.birinci_oyuncu_isim, font="Verdana 22")
        label_harita.place(x=50, y=20)
    if c.oyuncu == 2 and not c.oyun_sonu_tahta:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="2. Oyuncu:" + c.ikinci_oyuncu_isim , font="Verdana 22")
        label_harita.place(x=1400, y=20)

    if c.oyun_sonu_tahta:
        for i in range(len(c.matrix)):
            for j in range(len(c.matrix)):
                if c.matrix[i][j] >= 1:
                    c.buton_list[i][j].config(bg="pink")
        yol_var_mi_fonk(0, 0)
        dosya2 = open("matrix/matrix_2.txt", "r")
        skor_matrix_yazdir = matrix_okuma(dosya2)
        dosya2.close()
        print("!!", skor_matrix_yazdir)

        ortadan_secmis_mi = False
        #Orta elemana kadar gidilmediyse ilk oyuncunun suçudur
        for i in c.secim_liste_1:
            if i[1] == 3:
                ortadan_secmis_mi = True

        if c.yol_var_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kazandınız",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kesişim yok")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1
        else:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kimse ortaya gelemedi")

        dosya1 = open("matrix/matrix_2.txt", "w")
        dosya1.write(str(skor_matrix_yazdir))
        dosya1.close()

    label_harita.place(x=400, y=50)
    tahta.mainloop()




def oyun_harita_5x5_fonk():
    c.buton_list = []
    tahta = tk.Tk()
    tahta.title("Köprü Bağlamaca")

    #tahta.resizable(False,False)  #ilk taraf x ekseni, 2. taraf y ekseni ile oynayıp oynanamayacağını belirliyor.
    tahta.geometry("1680x1050+500+200")  #Sol taraf açılır pencere boyutu, sağ taraf bilgisayarın neresinde açılacağı
    tahta.resizable(False, False)
    tahta.lift()
    tahta.attributes('-topmost', True)

    # Canvas oluştur ve arkaplan resmini yükle
    canvas = tk.Canvas(tahta, width=1680, height=1050)
    canvas.pack(fill="both", expand=True)

    # Arkaplan resmini yükle
    img_str = ""
    if c.oyun_sonu_tahta:
        img_str = "bg3.jpg"
    elif c.oyuncu == 1:
        img_str = "bg1.jpg"
    elif c.oyuncu == 2:
        img_str = "bg2.jpg"

    bg_image = Image.open("img/" + img_str)
    bg_image = bg_image.resize((1680, 1050), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Canvas'a arkaplan resmini yerleştir
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    gec_liste = []
    rex = 670
    rey = 230
    isimler_list = ["00", "01", "02", "03", "04",
                    "10", "11", "12", "13", "14",
                    "20", "21", "22", "23", "24",
                    "30", "31", "32", "33", "34",
                    "40", "41", "42", "43", "44"]
    fonks_list = [degistir00, degistir01, degistir02, degistir03, degistir04,
                  degistir10, degistir11, degistir12, degistir13, degistir14,
                  degistir20, degistir21, degistir22, degistir23, degistir24,
                  degistir30, degistir31, degistir32, degistir33, degistir34,
                  degistir40, degistir41, degistir42, degistir43, degistir44]

    print("aa")
    for i in range(25):
        if i % 5 == 0:
            if len(gec_liste) != 0:
                c.buton_list.append(gec_liste)
            gec_liste = []
            rex = 650
            rey += 85
        blok_00 = tk.Button(tahta, text=isimler_list[i], bg="blue", fg="white", width=8, height=5,
                            command=fonks_list[i])
        if c.oyun_sonu_tahta:
            blok_00.config(state=tk.DISABLED)
        blok_00.place(x=rex, y=rey)
        rex += 66
        gec_liste.append(blok_00)

    c.buton_list.append(gec_liste)

    for i in range(5):
        for j in range(5):
            if c.matrix[i][j] == -1:
                c.buton_list[i][j].config(text="Kara \nparçası!!!", bg="black", state=tk.DISABLED)

    if c.oyuncu == 1:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="1. Oyuncu:" + c.birinci_oyuncu_isim, font="Verdana 22")
        label_harita.place(x=50, y=20)
    if c.oyuncu == 2 and not c.oyun_sonu_tahta:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="2. Oyuncu:" + c.ikinci_oyuncu_isim , font="Verdana 22")
        label_harita.place(x=1400, y=20)
    if c.oyun_sonu_tahta:
        for i in range(len(c.matrix)):
            for j in range(len(c.matrix)):
                if c.matrix[i][j] >= 1:
                    c.buton_list[i][j].config(bg="pink")
        yol_var_mi_fonk(0, 0)
        dosya2 = open("matrix/matrix_1.txt", "r")
        skor_matrix_yazdir = matrix_okuma(dosya2)
        dosya2.close()
        print("!!", skor_matrix_yazdir)

        ortadan_secmis_mi = False
        #Orta elemana kadar gidilmediyse ilk oyuncunun suçudur
        for i in c.secim_liste_1:
            if i[1] == 2:
                ortadan_secmis_mi = True

        if c.yol_var_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kazandınız",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kesişim yok")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1
        else:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kimse ortaya gelemedi")

        dosya1 = open("matrix/matrix_1.txt", "w")
        dosya1.write(str(skor_matrix_yazdir))
        dosya1.close()


    tahta.mainloop()


def oyun_harita_9x9_fonk():
    c.buton_list = []
    tahta = tk.Tk()
    tahta.title("Köprü Bağlamaca")


    #tahta.resizable(False,False)  #ilk taraf x ekseni, 2. taraf y ekseni ile oynayıp oynanamayacağını belirliyor.
    tahta.geometry("1680x1050+500+200")  #Sol taraf açılır pencere boyutu, sağ taraf bilgisayarın neresinde açılacağı
    tahta.resizable(False, False)
    tahta.lift()
    tahta.attributes('-topmost', True)

    # Canvas oluştur ve arkaplan resmini yükle
    canvas = tk.Canvas(tahta, width=1680, height=1050)
    canvas.pack(fill="both", expand=True)

    # Arkaplan resmini yükle
    img_str = ""
    if c.oyun_sonu_tahta:
        img_str = "bg3.jpg"
    elif c.oyuncu == 1:
        img_str = "bg1.jpg"
    elif c.oyuncu == 2:
        img_str = "bg2.jpg"

    bg_image = Image.open("img/" + img_str)
    bg_image = bg_image.resize((1680, 1050), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Canvas'a arkaplan resmini yerleştir
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    gec_liste = []
    rex = 540
    rey = 53
    isimler_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08",
                    "10", "11", "12", "13", "14", "15", "16", "17", "18",
                    "20", "21", "22", "23", "24", "25", "26", "27", "28",
                    "30", "31", "32", "33", "34", "35", "36", "37", "38",
                    "40", "41", "42", "43", "44", "45", "46", "47", "48",
                    "50", "51", "52", "53", "54", "55", "56", "57", "58",
                    "60", "61", "62", "63", "64", "65", "66", "67", "68",
                    "70", "71", "72", "73", "74", "75", "76", "77", "78",
                    "80", "81", "82", "83", "84", "85", "86", "87", "88"]
    fonks_list = [degistir00, degistir01, degistir02, degistir03, degistir04, degistir05, degistir06, degistir07,
                  degistir08,
                  degistir10, degistir11, degistir12, degistir13, degistir14, degistir15, degistir16, degistir17,
                  degistir18,
                  degistir20, degistir21, degistir22, degistir23, degistir24, degistir25, degistir26, degistir27,
                  degistir28,
                  degistir30, degistir31, degistir32, degistir33, degistir34, degistir35, degistir36, degistir37,
                  degistir38,
                  degistir40, degistir41, degistir42, degistir43, degistir44, degistir45, degistir46, degistir47,
                  degistir48,
                  degistir50, degistir51, degistir52, degistir53, degistir54, degistir55, degistir56, degistir57,
                  degistir58,
                  degistir60, degistir61, degistir62, degistir63, degistir64, degistir65, degistir66, degistir67,
                  degistir68,
                  degistir70, degistir71, degistir72, degistir73, degistir74, degistir75, degistir76, degistir77,
                  degistir78,
                  degistir80, degistir81, degistir82, degistir83, degistir84, degistir85, degistir86, degistir87,
                  degistir88]

    for i in range(81):
        if i % 9 == 0:
            if len(gec_liste) != 0:
                c.buton_list.append(gec_liste)
            gec_liste = []
            rex = 550
            rey += 85
        blok_00 = tk.Button(tahta, text=isimler_list[i], bg="blue", fg="white", width=8, height=5,
                            command=fonks_list[i])
        if c.oyun_sonu_tahta:
            blok_00.config(state=tk.DISABLED)
        blok_00.place(x=rex, y=rey)
        rex += 66
        gec_liste.append(blok_00)

    c.buton_list.append(gec_liste)

    for i in range(9):
        for j in range(9):
            if c.matrix[i][j] == -1:
                c.buton_list[i][j].config(text="Kara \nparçası!!!", bg="black", state=tk.DISABLED)

    if c.oyuncu == 1:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="1. Oyuncu:" + c.birinci_oyuncu_isim, font="Verdana 22")
        label_harita.place(x=50, y=20)
    if c.oyuncu == 2 and not c.oyun_sonu_tahta:
        label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="2. Oyuncu:" + c.ikinci_oyuncu_isim , font="Verdana 22")
        label_harita.place(x=1400, y=20)

    if c.oyun_sonu_tahta:
        for i in range(len(c.matrix)):
            for j in range(len(c.matrix)):
                if c.matrix[i][j] >= 1:
                    c.buton_list[i][j].config(bg="pink")
        yol_var_mi_fonk(0, 0)
        dosya2 = open("matrix/matrix_3.txt", "r")
        skor_matrix_yazdir = matrix_okuma(dosya2)
        dosya2.close()
        print("!!", skor_matrix_yazdir)

        ortadan_secmis_mi = False
        #Orta elemana kadar gidilmediyse ilk oyuncunun suçudur
        for i in c.secim_liste_1:
            if i[1] == 2:
                ortadan_secmis_mi = True

        if c.yol_var_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kazandınız",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kesişim yok")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1
        else:
            label_harita = tk.Label(tahta, bg="blue", fg="yellow", text="Kaybettiniz",
                                    font="Verdana 22")
            label_harita.place(x=750, y=50)
            messagebox.showinfo("Durum", "Kaybettiniz, kimse ortaya gelemedi")


        dosya1 = open("matrix/matrix_3.txt", "w")
        dosya1.write(str(skor_matrix_yazdir))
        dosya1.close()


    tahta.mainloop()
