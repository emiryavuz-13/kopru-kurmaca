from utils import *
from ai import *
from map_genarator import *


dosya =""
if c.yapay_zeka_tipi=="öğrenmiş":

    if c.harita_buyukluk==5:
        dosya=open("matrix/matrix_1.txt", "r")
    elif c.harita_buyukluk==7:
        dosya=open("matrix/matrix_2.txt", "r")
    elif c.harita_buyukluk==9:
        dosya=open("matrix/matrix_3.txt", "r")

if c.harita_buyukluk==7:
    random_secici_fonk_7x7()
    if c.harita_tip == "seyrek":
        tas_secici_fonk_7x7_seyrek()
    elif c.harita_tip == "taşlı":
        tas_secici_fonk_7x7_tasli()

    oyun_harita_7x7_fonk()

    c.secim_sayisi = int(len(c.matrix) / 2) + 1
    for i in range(7):
        for j in range(7):
            if c.matrix[i][j]==1:
                c.secim_liste_1.append([i,j])



    if c.yapay_zeka_tipi=="yok":
        for i in range(len(c.denetim_matrix)):
            for j in range(len(c.denetim_matrix)):
                c.denetim_matrix[i][j]=0
        c.oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")
        oyun_harita_7x7_fonk()

    elif c.yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        print(c.secim_liste_2, ">>>>>>>>>>>")
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    elif c.yapay_zeka_tipi=="öğrenmiş":
        c.skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        print(c.secim_liste_2)
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    c.oyun_sonu_tahta=True
    oyun_harita_7x7_fonk()


if c.harita_buyukluk==5:
    random_secici_fonk_5x5()
    if c.harita_tip == "seyrek":
        tas_secici_fonk_5x5_seyrek()
    elif c.harita_tip == "taşlı":
        tas_secici_fonk_5x5_tasli()

    oyun_harita_5x5_fonk()

    c.secim_sayisi = int(len(c.matrix) / 2) + 1
    for i in range(5):
        for j in range(5):
            if c.matrix[i][j]==1:
                c.secim_liste_1.append([i,j])


    if c.yapay_zeka_tipi=="yok":
        for i in range(len(c.denetim_matrix)):
            for j in range(len(c.denetim_matrix)):
                c.denetim_matrix[i][j]=0
        c.oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")

        oyun_harita_5x5_fonk()

    elif c.yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    elif c.yapay_zeka_tipi=="öğrenmiş":
        c.skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        print(c.secim_liste_2)
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    c.oyun_sonu_tahta=True
    oyun_harita_5x5_fonk()



if c.harita_buyukluk==9:
    random_secici_fonk_9x9()
    if c.harita_tip == "seyrek":
        tas_secici_fonk_9x9_seyrek()
    elif c.harita_tip == "taşlı":
        tas_secici_fonk_9x9_tasli()

    oyun_harita_9x9_fonk()

    c.secim_sayisi = int(len(c.matrix) / 2) + 1
    for i in range(c.harita_buyukluk):
        for j in range(c.harita_buyukluk):
            if c.matrix[i][j]==1:
                c.secim_liste_1.append([i,j])


    if c.yapay_zeka_tipi=="yok":
        for i in range(c.harita_buyukluk):
            for j in range(c.harita_buyukluk):
                c.denetim_matrix[i][j]=0
        c.oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")
        oyun_harita_9x9_fonk()

    elif c.yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        print(c.secim_liste_2, ">>>>>>>>>>>")
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    elif c.yapay_zeka_tipi=="öğrenmiş":
        c.skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(c.harita_buyukluk - 1)
        print(c.secim_liste_2)
        for i in c.secim_liste_2:
            c.matrix[i[0]][i[1]] += 1

    c.oyun_sonu_tahta=True
    oyun_harita_9x9_fonk()
