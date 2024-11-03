import config as c


def izin_var_mi(i, j, oyuncu):  #1. oyuncu için butona basma hakkı var mı sorgusu
    if oyuncu == 1:
        izinli_yol = 0
    else:
        izinli_yol = c.harita_buyukluk - 1
    if (j == izinli_yol or c.denetim_matrix[i][j] != 0):
        c.denetim_matrix[i][j] += 1
        try:
            c.denetim_matrix[i][j + 1] += 1
        except:
            print("Devam")
        try:
            c.denetim_matrix[i][j - 1] += 1
        except:
            print("Devam")
        try:
            c.denetim_matrix[i - 1][j + 1] += 1
        except:
            print("Bir şey yok devam et")
        try:
            c.denetim_matrix[i - 1][j] += 1
        except:
            print("Bir şey yok devam et")
        try:
            c.denetim_matrix[i - 1][j - 1] += 1
        except:
            print("Bir şey yok devam et")

        try:
            c.denetim_matrix[i + 1][j + 1] += 1
        except:
            print("Bir şey yok devam et")

        try:
            c.denetim_matrix[i + 1][j] += 1
        except:
            print("Bir şey yok devam et")
        try:
            c.denetim_matrix[i + 1][j - 1] += 1
        except:
            print("Bir şey yok devam et")

        c.secim_sayisi -= 1
        print(c.secim_sayisi)
        return True

    return False


def yol_var_mi_fonk(x, y):  #Yol var mı denetimini yapan fonks

    if c.basladin_mi:
        for i in range(len(c.matrix) - 1):
            if c.matrix[i][y] > 0:

                c.basladin_mi = False

                try:
                    yol_var_mi_fonk(i - 1, y + 1)
                except:
                    print("!!")

                yol_var_mi_fonk(i, y + 1)

                try:
                    yol_var_mi_fonk(i + 1, y + 1)
                except:
                    print("!!")

    if c.matrix[x][y] > 0 and y != len(c.matrix) - 1 and x != len(c.matrix) - 1:

        try:
            if x != 0:
                yol_var_mi_fonk(x - 1, y + 1)
        except:
            print("!!")
        try:
            yol_var_mi_fonk(x, y + 1)
        except:
            print("!!")

        yol_var_mi_fonk(x + 1, y + 1)

    if y == len(c.matrix) - 1 and c.matrix[x][y] > 0:
        c.yol_var_mi = True


def skor_hesaplama_fonk():
    boyut = len(c.skor_matrix)
    if c.skor_hesaplama_bool:  #İlk girişince taşlara -1 değerini ver bi daha buraya girme
        for i in range(boyut):
            for j in range(boyut):
                if c.matrix[i][j] == -1:
                    c.skor_matrix[i][j] = -1
        c.skor_hesaplama_bool = False

    c.matrix_okuma_bool = False
    uzunluk = boyut - 1
    orta = int(boyut / 2) + 1
    for i in range(boyut):
        if i == 0 and c.skor_matrix[i][uzunluk - 1] < 0 and c.skor_matrix[i + 1][uzunluk - 1] < 0:  #prnt.sc/241emm2
            if c.skor_matrix[i][uzunluk] >= 0:
                c.matrix_okuma_bool = True
                c.skor_matrix[i][uzunluk] = -2

        if i == uzunluk and c.skor_matrix[i][uzunluk - 1] < 0 and c.skor_matrix[i - 1][
            uzunluk - 1] < 0:  #prnt.sc/241f3ad
            if c.skor_matrix[i][uzunluk] >= 0:
                c.matrix_okuma_bool = True
                c.skor_matrix[i][uzunluk] = -2

        if i >= orta - 1 and i != uzunluk:  #ortadan sütundan sondan bir önceki sütuna kadar tara  prnt.sc/24502ap
            stack = 0
            for j in range(boyut):
                if c.skor_matrix[j][i] < 0:
                    stack += 1
                else:
                    stack = 0
                if j == 1 and stack == 2:
                    if c.skor_matrix[0][i + 1] >= 0:
                        c.matrix_okuma_bool = True
                        c.skor_matrix[0][i + 1] = -2
                if stack >= 3:
                    if c.skor_matrix[j - 1][i + 1] >= 0:
                        c.matrix_okuma_bool = True
                        c.skor_matrix[j - 1][i + 1] = -2
                if j == boyut - 1 and stack >= 2:
                    if c.skor_matrix[boyut - 1][i + 1] >= 0:
                        c.matrix_okuma_bool = True
                        c.skor_matrix[boyut - 1][i + 1] = -2
    if c.matrix_okuma_bool:
        skor_hesaplama_fonk()


def matrix_okuma(dosyam):
    icerik = dosyam.read()
    skor_matrixx = []
    denetim = []
    sayi_denitim = []
    sayilar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(icerik)):
        if icerik[i] in sayilar and not (icerik[i - 1] in sayilar):
            x = i
            while icerik[x] in sayilar:

                sayi_denitim.append(icerik[x])
                x += 1
                try:
                    icerik[x]
                except:
                    break
            denetim.append(int("".join(sayi_denitim)))
            sayi_denitim = []

        if icerik[i] == " " and icerik[i + 1] == "[":
            skor_matrixx.append(denetim)
            denetim = []
    skor_matrixx.append(denetim)
    return skor_matrixx
