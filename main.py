from ai import *
from map_genarator import *

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









oyuncu=1
oyun_baslangic_fonk()
matrix,denetim_matrix=matrix_secim()
sonuc_matrix=copy.deepcopy(matrix)
secim_sayisi=int(len(matrix)/2)+1
oyun_sonu_tahta=False

if yapay_zeka_tipi=="öğrenmiş":
    if harita_buyukluk==5:
        dosya=open("matrix_1.txt", "r")
    elif harita_buyukluk==7:
        dosya=open("matrix_2.txt", "r")
    elif harita_buyukluk==9:
        dosya=open("matrix_3.txt", "r")

if harita_buyukluk==7:
    random_secici_fonk_7x7()
    if harita_tip == "seyrek":
        tas_secici_fonk_7x7_seyrek()
    elif harita_tip == "taşlı":
        tas_secici_fonk_7x7_tasli()

    oyun_harita_7x7_fonk()

    secim_sayisi = int(len(matrix) / 2) + 1
    for i in range(7):
        for j in range(7):
            if matrix[i][j]==1:
                secim_liste_1.append([i,j])



    if yapay_zeka_tipi=="yok":
        for i in range(len(denetim_matrix)):
            for j in range(len(denetim_matrix)):
                denetim_matrix[i][j]=0
        oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")
        oyun_harita_7x7_fonk()

    elif yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(harita_buyukluk - 1)
        print(secim_liste_2, ">>>>>>>>>>>")
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    elif yapay_zeka_tipi=="öğrenmiş":
        skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(harita_buyukluk - 1)
        print(secim_liste_2)
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    oyun_sonu_tahta=True
    oyun_harita_7x7_fonk()


if harita_buyukluk==5:
    random_secici_fonk_5x5()
    if harita_tip == "seyrek":
        tas_secici_fonk_5x5_seyrek()
    elif harita_tip == "taşlı":
        tas_secici_fonk_5x5_tasli()

    oyun_harita_5x5_fonk()

    secim_sayisi = int(len(matrix) / 2) + 1
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==1:
                secim_liste_1.append([i,j])


    if yapay_zeka_tipi=="yok":
        for i in range(len(denetim_matrix)):
            for j in range(len(denetim_matrix)):
                denetim_matrix[i][j]=0
        oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")
        oyun_harita_5x5_fonk()

    elif yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(harita_buyukluk - 1)
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    elif yapay_zeka_tipi=="öğrenmiş":
        skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(harita_buyukluk - 1)
        print(secim_liste_2)
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    oyun_sonu_tahta=True
    oyun_harita_5x5_fonk()



if harita_buyukluk==9:
    random_secici_fonk_9x9()
    if harita_tip == "seyrek":
        tas_secici_fonk_9x9_seyrek()
    elif harita_tip == "taşlı":
        tas_secici_fonk_9x9_tasli()

    oyun_harita_9x9_fonk()

    secim_sayisi = int(len(matrix) / 2) + 1
    for i in range(harita_buyukluk):
        for j in range(harita_buyukluk):
            if matrix[i][j]==1:
                secim_liste_1.append([i,j])


    if yapay_zeka_tipi=="yok":
        for i in range(harita_buyukluk):
            for j in range(harita_buyukluk):
                denetim_matrix[i][j]=0
        oyuncu=2
        messagebox.showinfo("Durum", "2. oyuncu bekleniyor")
        oyun_harita_9x9_fonk()

    elif yapay_zeka_tipi=="normal":
        yapay_zeka_secim_fonk(harita_buyukluk - 1)
        print(secim_liste_2, ">>>>>>>>>>>")
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    elif yapay_zeka_tipi=="öğrenmiş":
        skor_matrix = matrix_okuma(dosya)
        dosya.close()
        skor_hesaplama_fonk()
        ogrenmis_yapay_zeka_secim_fonk(harita_buyukluk - 1)
        print(secim_liste_2)
        for i in secim_liste_2:
            matrix[i[0]][i[1]] += 1

    oyun_sonu_tahta=True
    oyun_harita_9x9_fonk()
