import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import copy
import random


secim_liste_1=[]


random_secici_liste=[0]
yapay_zeka_tipi="yok" # yok | normal | öğrenmiş
birinci_oyuncu_isim="boş"
ikinci_oyuncu_isim="Boş"
harita_buyukluk=0  # 5 | 7 | 9
harita_tip="secilmedi"  # boş | seyrek | taşlı

#yol_var_mi.py için
yol_var_mi=False
basladin_mi=True

#yapay_zeka_secimi.py
yapay_zeka_bool=True
secim_liste_2=[]

tekrar_yok=False

#ogrenmis_yapay_zeka.py
matrix_okuma_bool=True #skor_hesaplama_fonk için || özyinelemeyi takip ediyor
skor_hesaplama_bool=True #skor_hesaplama_fonk için || ilk girişte taşları koyuyor

#Baslangic fonksiyonu için
buton_list=[]