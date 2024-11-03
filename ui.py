from btn_func import *
import config as c
from utils import yol_var_mi_fonk, matrix_okuma


def oyun_harita_7x7_fonk():
    c.buton_list = []
    tahta = tk.Tk()
    tahta.title("Köprü Bağlamaca")

    #tahta.resizable(False,False)  #ilk taraf x ekseni, 2. taraf y ekseni ile oynayıp oynanamayacağını belirliyor.
    tahta.geometry("1680x1050+500+200")  #Sol taraf açılır pencere boyutu, sağ taraf bilgisayarın neresinde açılacağı

    #tahta.state("zoomed") #ful ekran açar

    gec_liste = []
    rex = 600
    rey = 200
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
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            messagebox.showinfo("Durum", "Kaybettiniz")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1

        dosya1 = open("matrix/matrix_2.txt", "w")
        dosya1.write(str(skor_matrix_yazdir))
        dosya1.close()

    tahta.mainloop()


def oyun_harita_5x5_fonk():
    c.buton_list = []
    tahta = tk.Tk()
    tahta.title("Köprü Bağlamaca")

    #tahta.resizable(False,False)  #ilk taraf x ekseni, 2. taraf y ekseni ile oynayıp oynanamayacağını belirliyor.
    tahta.geometry("1680x1050+500+200")  #Sol taraf açılır pencere boyutu, sağ taraf bilgisayarın neresinde açılacağı

    #tahta.state("zoomed") #ful ekran açar

    gec_liste = []
    rex = 650
    rey = 200
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
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            messagebox.showinfo("Durum", "Kaybettiniz")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1

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

    #tahta.state("zoomed") #ful ekran açar

    gec_liste = []
    rex = 550
    rey = 50
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
            messagebox.showinfo("Durum", "Kazandınız...")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] += 1
        elif ortadan_secmis_mi:
            messagebox.showinfo("Durum", "Kaybettiniz")
            for i in c.secim_liste_2:
                skor_matrix_yazdir[i[0]][i[1]] -= 1

        dosya1 = open("matrix/matrix_3.txt", "w")
        dosya1.write(str(skor_matrix_yazdir))
        dosya1.close()

    tahta.mainloop()
