import copy
from PIL import Image, ImageTk

from tkinter import messagebox

import tkinter as tk


def resim_bastirici():
    print(harita_tip)
    if harita_tip == "boş" and harita_buyukluk == 5:
        resim_label.config(image=resim00)
    elif harita_tip == "seyrek" and harita_buyukluk == 5:
        resim_label.config(image=resim01)
    elif harita_tip == "taşlı" and harita_buyukluk == 5:
        resim_label.config(image=resim02)

    elif harita_tip == "boş" and harita_buyukluk == 7:
        resim_label.config(image=resim10)
    elif harita_tip == "seyrek" and harita_buyukluk == 7:
        resim_label.config(image=resim11)
    elif harita_tip == "taşlı" and harita_buyukluk == 7:
        resim_label.config(image=resim12)

    elif harita_tip == "boş" and harita_buyukluk == 9:
        resim_label.config(image=resim20)
    elif harita_tip == "seyrek" and harita_buyukluk == 9:
        resim_label.config(image=resim21)
    elif harita_tip == "taşlı" and harita_buyukluk == 9:
        resim_label.config(image=resim22)

    if harita_tip != "secilmedi":
        if harita_buyukluk == 5:
            resim_label.place(x=680, y=400)
        elif harita_buyukluk == 7:
            resim_label.place(x=610, y=360)
        elif harita_buyukluk == 9:
            resim_label.place(x=580, y=300)


def buton_renk_ayarla(boyanacak_sekme, boyanacak_buton):
    if boyanacak_sekme == "büyüklük":
        kucuk_harita_buton.config(bg="gray", fg="white")
        orta_harita_buton.config(bg="gray", fg="white")
        buyuk_harita_buton.config(bg="gray", fg="white")

        if boyanacak_buton == "küçük":
            kucuk_harita_buton.config(bg="#4582f7", fg="white")
        elif boyanacak_buton == "orta":
            orta_harita_buton.config(bg="#4582f7", fg="white")
        elif boyanacak_buton == "büyük":
            buyuk_harita_buton.config(bg="#4582f7", fg="white")

    elif boyanacak_sekme == "tip":
        bos_deniz_buton.config(bg="gray", fg="white")
        seyrek_deniz_buton.config(bg="gray", fg="white")
        tasli_deniz_buton.config(bg="gray", fg="white")

        print(boyanacak_buton)
        if boyanacak_buton == "boş":
            bos_deniz_buton.config(bg="#4582f7", fg="black")
        elif boyanacak_buton == "seyrek":
            seyrek_deniz_buton.config(bg="#4582f7", fg="black")
        elif boyanacak_buton == "taşlı":
            tasli_deniz_buton.config(bg="#4582f7", fg="black")

def bos_deniz_fonk():
    global harita_tip
    harita_tip = "boş"
    buton_renk_ayarla("tip", harita_tip)
    resim_bastirici()



def seyrek_tasli_deniz_fonk():
    global harita_tip
    harita_tip = "seyrek"
    buton_renk_ayarla("tip", harita_tip)

    resim_bastirici()


def tasli_deniz_fonk():
    global harita_tip
    harita_tip = "taşlı"
    buton_renk_ayarla("tip", harita_tip)

    resim_bastirici()


def kucuk_harita_fonk():
    global harita_buyukluk
    harita_buyukluk = 5
    buton_renk_ayarla("büyüklük", "küçük")

    resim_bastirici()


def orta_harita_fonk():
    global harita_buyukluk
    harita_buyukluk = 7
    buton_renk_ayarla("büyüklük", "orta")

    resim_bastirici()


def buyuk_harita_fonk():
    global harita_buyukluk
    harita_buyukluk = 9
    buton_renk_ayarla("büyüklük", "büyük")

    resim_bastirici()


def basla_fonk():
    global birinci_oyuncu_isim, ikinci_oyuncu_isim, yapay_zeka_tipi

    birinci_oyuncu_isim = tk.Entry.get(birinci_oyuncu_entry)
    ikinci_oyuncu_isim = tk.Entry.get(ikinci_oyuncu_entry)
    if not (not (len(birinci_oyuncu_isim) == 0 or birinci_oyuncu_isim == " ") and not (
            (len(ikinci_oyuncu_isim) == 0 or ikinci_oyuncu_isim[0] == " ") and yapay_zeka_tipi == "yok")):
        messagebox.showwarning("Uyarı", "Lütfen oyuncu isimlerini giriniz")
    elif harita_tip == "secilmedi":
        messagebox.showwarning("Uyarı", "Lütfen harita tipini seçiniz")
    elif harita_buyukluk == 0:
        messagebox.showwarning("Uyarı", "Lütfen harita büyüklüğünü seçiniz")
    else:
        if yapay_zeka_tipi == "normal":
            soru = messagebox.askquestion("Yapay zeka seçimi", "Öğrenmiş yapay zeka aktif edilsin mi?", )
            if soru == "yes":
                yapay_zeka_tipi = "öğrenmiş"

        butun.destroy()


def oyun_baslangic_fonk():
    global yapay_zeka_kontrolcusu, ikinci_oyuncu_entry, birinci_oyuncu_entry, butun, resim00, resim01, resim02, \
        resim10, resim11, resim12, resim20, resim21, resim22, resim_label, harita_tip, bos_deniz_buton, seyrek_deniz_buton,\
        tasli_deniz_buton, kucuk_harita_buton, orta_harita_buton, buyuk_harita_buton

    butun = tk.Tk()
    butun.title("Köprü Bağlamaca")

    butun.geometry("1680x1050+500+200")

    # Canvas oluştur ve arkaplan resmini yükle
    canvas = tk.Canvas(butun, width=1680, height=1050)
    canvas.pack(fill="both", expand=True)

    # Arkaplan resmini yükle
    bg_image = Image.open("img/bg3.jpg")
    bg_image = bg_image.resize((1680, 1050), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas'a arkaplan resmini yerleştir
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    butun.resizable(False, False)

    label_harita = tk.Label(butun, bg="#97d3eb", fg="black", text="Boyut seçimi", font="Verdana 22")
    label_harita.place(x=225, y=50)
    label_harita = tk.Label(butun, bg="#97d3eb", fg="black", text="Harita seçimi", font="Verdana 22")
    label_harita.place(x=1170, y=50)
    bos_deniz_buton = tk.Button(butun, bg="grey", fg="white", text="Boş deniz", font="Verdana 15",
                                command=bos_deniz_fonk)
    seyrek_deniz_buton = tk.Button(butun, bg="grey", fg="white", text="Seyrek taşlı deniz", font="Verdana 15",
                                   command=seyrek_tasli_deniz_fonk)
    tasli_deniz_buton = tk.Button(butun, bg="grey", fg="white", text="Taşlı deniz", font="Verdana 15",
                                  command=tasli_deniz_fonk)
    bos_deniz_buton.place(x=1200, y=100)
    seyrek_deniz_buton.place(x=1200, y=150)
    tasli_deniz_buton.place(x=1200, y=200)
    kucuk_harita_buton = tk.Button(butun, bg="grey", fg="white", font="Verdana 15", text="5 X 5 harita",
                                   command=kucuk_harita_fonk)
    kucuk_harita_buton.place(x=250, y=100)
    orta_harita_buton = tk.Button(butun, bg="grey", fg="white", font="Verdana 15", text="7 X 7 harita",
                                  command=orta_harita_fonk)
    orta_harita_buton.place(x=250, y=150)
    buyuk_harita_buton = tk.Button(butun, bg="grey", fg="white", font="Verdana 15", text="9 X 9 harita",
                                   command=buyuk_harita_fonk)
    buyuk_harita_buton.place(x=250, y=200)

    isim_giriniz_label = tk.Label(butun, text="İsimlerinizi giriniz", bg="#97d3eb", fg="black", font="Verdana 22")
    isim_giriniz_label.place(x=700, y=50)
    birinci_oyunu_label = tk.Label(butun, text="Birinci oyuncu", bg="#97d3eb", fg="black",font=("bold"))
    birinci_oyunu_label.place(x=670, y=120)
    ikinci_oyuncu_label = tk.Label(butun, text="İkinci oyuncu", bg="#97d3eb", fg="black",font=("bold"))
    ikinci_oyuncu_label.place(x=670, y=150)
    birinci_oyuncu_entry = tk.Entry(butun)
    birinci_oyuncu_entry.place(x=780, y=120)
    ikinci_oyuncu_entry = tk.Entry(butun)
    ikinci_oyuncu_entry.place(x=780, y=150)
    basla_buton = tk.Button(butun, text="Başla", bg="grey", font="Verdana 20", command=basla_fonk)
    basla_buton.place(x=760, y=220)
    resim00 = ImageTk.PhotoImage(Image.open("img/00.png"))
    resim01 = ImageTk.PhotoImage(Image.open("img/01.png"))
    resim02 = ImageTk.PhotoImage(Image.open("img/02.png"))
    resim10 = ImageTk.PhotoImage(Image.open("img/10.png"))
    resim11 = ImageTk.PhotoImage(Image.open("img/11.png"))
    resim12 = ImageTk.PhotoImage(Image.open("img/12.png"))
    resim20 = ImageTk.PhotoImage(Image.open("img/20.png"))
    resim21 = ImageTk.PhotoImage(Image.open("img/21.png"))
    resim22 = ImageTk.PhotoImage(Image.open("img/22.png"))
    yapay_zeka_kontrolcusu = tk.IntVar()
    yapay_zeka_kontrolcusu.set(0)
    yapay_zeka_checkbuton = tk.Checkbutton(butun, variable=yapay_zeka_kontrolcusu, text="Yapay zeka aktif edilsin mi?", bg="#97d3eb", fg="black",
                                           command=yapay_zeka_aktif_mi_fonk)
    yapay_zeka_checkbuton.place(x=720, y=180)
    resim_label = tk.Label(butun)
    butun.mainloop()


def matrix_secim():
    global harita_buyukluk, matrix
    if harita_buyukluk == 5:
        matrix = \
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
    elif harita_buyukluk == 7:
        matrix = \
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ]
    elif harita_buyukluk == 9:
        matrix = \
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
    denetim_matrix = copy.deepcopy(matrix)
    return matrix, denetim_matrix


def yapay_zeka_aktif_mi_fonk():
    global yapay_zeka_tipi
    if tk.IntVar.get(yapay_zeka_kontrolcusu) == 0:
        yapay_zeka_tipi = "yok"
        ikinci_oyuncu_entry.config(state="normal")

    else:
        yapay_zeka_tipi = "normal"
        ikinci_oyuncu_entry.config(state="disabled")


secim_liste_1 = []
random_secici_liste = [0]
yapay_zeka_tipi = "yok"  # yok | normal | öğrenmiş
birinci_oyuncu_isim = "boş"
ikinci_oyuncu_isim = "Boş"
harita_buyukluk = 0  # 5 | 7 | 9
harita_tip = "secilmedi"  # boş | seyrek | taşlı

#yol_var_mi.py için
yol_var_mi = False
basladin_mi = True

#yapay_zeka_secimi.py
yapay_zeka_bool = True
secim_liste_2 = []
skor_matrix = []
tekrar_yok = False

#ogrenmis_yapay_zeka.py
matrix_okuma_bool = True  #skor_hesaplama_fonk için || özyinelemeyi takip ediyor
skor_hesaplama_bool = True  #skor_hesaplama_fonk için || ilk girişte taşları koyuyor

#Baslangic fonksiyonu için
buton_list = []
yapay_zeka_kontrolcusu = ""
ikinci_oyuncu_entry = ""
birinci_oyuncu_entry = ""
butun = ""
resim00 = ""
resim01 = ""
resim02 = ""
resim10 = ""
resim11 = ""
resim12 = ""
resim20 = ""
resim21 = ""
resim22 = ""
resim_label = ""
label_text = ""
oyuncu = 1
oyun_baslangic_fonk()
matrix, denetim_matrix = matrix_secim()

sonuc_matrix = copy.deepcopy(matrix)
secim_sayisi = int(len(matrix) / 2)
oyun_sonu_tahta = False
