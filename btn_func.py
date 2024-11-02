from utils import *

#Buton için fonksiyonlar
def degistir00():

    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    print("oooooo",oyuncu)
    if (izin_var_mi(0, 0,oyuncu)):
        matrix[0][0] += 1
        buton_list[0][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")

    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir01():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 1,oyuncu)):
        matrix[0][1] += 1
        buton_list[0][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir02():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 2,oyuncu)):
        matrix[0][2] += 1
        buton_list[0][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir03():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if izin_var_mi(0, 3, oyuncu):
        matrix[0][3] += 1
        buton_list[0][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir04():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if izin_var_mi(0, 4, oyuncu):
        matrix[0][4] += 1
        buton_list[0][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir05():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 5,oyuncu)):
        matrix[0][5] += 1
        buton_list[0][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir06():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 6,oyuncu)):
        matrix[0][6] += 1
        buton_list[0][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir07():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 7,oyuncu)):
        matrix[0][7] += 1
        buton_list[0][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir08():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(0, 8,oyuncu)):
        matrix[0][8] += 1
        buton_list[0][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

# ------------------------------------------------------------------------------


def degistir10():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 0,oyuncu)):
        matrix[1][0] += 1
        buton_list[1][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir11():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 1,oyuncu)):
        matrix[1][1] += 1
        buton_list[1][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir12():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 2,oyuncu)):
        matrix[1][2] += 1
        buton_list[1][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir13():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 3,oyuncu)):
        matrix[1][3] += 1
        buton_list[1][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir14():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 4,oyuncu)):
        matrix[1][4] += 1
        buton_list[1][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir15():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 5,oyuncu)):
        matrix[1][5] += 1
        buton_list[1][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir16():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 6,oyuncu)):
        matrix[1][6] += 1
        buton_list[1][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir17():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 7,oyuncu)):
        matrix[1][7] += 1
        buton_list[1][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir18():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(1, 8,oyuncu)):
        matrix[1][8] += 1
        buton_list[1][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# ------------------------------------------------------------------------------


def degistir20():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 0,oyuncu)):
        matrix[2][0] += 1
        buton_list[2][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir21():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 1,oyuncu)):
        matrix[2][1] += 1
        buton_list[2][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir22():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 2,oyuncu)):
        matrix[2][2] += 1
        buton_list[2][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir23():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 3,oyuncu)):
        matrix[2][3] += 1
        buton_list[2][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

def degistir24():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 4,oyuncu)):
        matrix[2][4] += 1
        buton_list[2][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir25():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 5,oyuncu)):
        matrix[2][5] += 1
        buton_list[2][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir26():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 6,oyuncu)):
        matrix[2][6] += 1
        buton_list[2][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir27():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 7,oyuncu)):
        matrix[2][7] += 1
        buton_list[2][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir28():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(2, 8,oyuncu)):
        matrix[2][8] += 1
        buton_list[2][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")

    # ------------------------------------------------------------------------------


def degistir30():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 0,oyuncu)):
        matrix[3][0] += 1
        buton_list[3][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir31():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 1,oyuncu)):
        matrix[3][1] += 1
        buton_list[3][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir32():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 2,oyuncu)):
        matrix[3][2] += 1
        buton_list[3][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir33():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 3,oyuncu)):
        matrix[3][3] += 1
        buton_list[3][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir34():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 4,oyuncu)):
        matrix[3][4] += 1
        buton_list[3][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir35():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 5,oyuncu)):
        matrix[3][5] += 1
        buton_list[3][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir36():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 6,oyuncu)):
        matrix[3][6] += 1
        buton_list[3][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir37():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 7,oyuncu)):
        matrix[3][7] += 1
        buton_list[3][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir38():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(3, 8,oyuncu)):
        matrix[3][8] += 1
        buton_list[3][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# ------------------------------------------------------------------------------


def degistir40():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 0,oyuncu)):
        matrix[4][0] += 1
        buton_list[4][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir41():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 1,oyuncu)):
        matrix[4][1] += 1
        buton_list[4][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir42():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 2,oyuncu)):
        matrix[4][2] += 1
        buton_list[4][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir43():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 3,oyuncu)):
        matrix[4][3] += 1
        buton_list[4][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir44():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 4,oyuncu)):
        matrix[4][4] += 1
        buton_list[4][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir45():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 5,oyuncu)):
        matrix[4][5] += 1
        buton_list[4][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
            messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir46():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 6,oyuncu)):
        matrix[4][6] += 1
        buton_list[4][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir47():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 7,oyuncu)):
        matrix[4][7] += 1
        buton_list[4][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir48():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(4, 8,oyuncu)):
        matrix[4][8] += 1
        buton_list[4][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# ------------------------------------------------------------------------------

def degistir50():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 0,oyuncu)):
        matrix[5][0] += 1
        buton_list[5][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir51():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 1,oyuncu)):
        matrix[5][1] += 1
        buton_list[5][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir52():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 2,oyuncu)):
        matrix[5][2] += 1
        buton_list[5][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir53():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 3,oyuncu)):
        matrix[5][3] += 1
        buton_list[5][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir54():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 4,oyuncu)):
        matrix[5][4] += 1
        buton_list[5][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir55():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 5,oyuncu)):
        matrix[5][5] += 1
        buton_list[5][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir56():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 6,oyuncu)):
        matrix[5][6] += 1
        buton_list[5][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir57():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 7,oyuncu)):
        matrix[5][7] += 1
        buton_list[5][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir58():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(5, 8,oyuncu)):
        matrix[5][8] += 1
        buton_list[5][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# ---------------------------------------------------------------------
def degistir60():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 0,oyuncu)):
        matrix[6][0] += 1
        buton_list[6][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir61():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 1,oyuncu)):
        matrix[6][1] += 1
        buton_list[6][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir62():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 2,oyuncu)):
        matrix[6][2] += 1
        buton_list[6][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir63():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 3,oyuncu)):
        matrix[6][3] += 1
        buton_list[6][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir64():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 4,oyuncu)):
        matrix[6][4] += 1
        buton_list[6][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir65():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 5,oyuncu)):
        matrix[6][5] += 1
        buton_list[6][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir66():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 6,oyuncu)):
        matrix[6][6] += 1
        buton_list[6][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir67():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 7,oyuncu)):
        matrix[6][7] += 1
        buton_list[6][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir68():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(6, 8,oyuncu)):
        matrix[6][8] += 1
        buton_list[6][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# --------------------------------------------------------------

def degistir70():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 0,oyuncu)):
        matrix[7][0] += 1
        buton_list[7][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir71():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 1,oyuncu)):
        matrix[7][1] += 1
        buton_list[7][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir72():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 2,oyuncu)):
        matrix[7][2] += 1
        buton_list[7][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir73():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 3,oyuncu)):
        matrix[7][3] += 1
        buton_list[7][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir74():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 4,oyuncu)):
        matrix[7][4] += 1
        buton_list[7][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir75():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 5,oyuncu)):
        matrix[7][5] += 1
        buton_list[7][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir76():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 6,oyuncu)):
        matrix[7][6] += 1
        buton_list[7][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir77():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 7,oyuncu)):
        matrix[7][7] += 1
        buton_list[7][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir78():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(7, 8,oyuncu)):
        matrix[7][8] += 1
        buton_list[7][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


# -----------------------------------------------------------------
def degistir80():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 0,oyuncu)):
        matrix[8][0] += 1
        buton_list[8][0].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir81():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 1,oyuncu)):
        matrix[8][1] += 1
        buton_list[8][1].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir82():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 2,oyuncu)):
        matrix[8][2] += 1
        buton_list[8][2].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir83():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 3,oyuncu)):
        matrix[8][3] += 1
        buton_list[8][3].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir84():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 4,oyuncu)):
        matrix[8][4] += 1
        buton_list[8][4].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir85():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 5,oyuncu)):
        matrix[8][5] += 1
        buton_list[8][5].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir86():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 6,oyuncu)):
        matrix[8][6] += 1
        buton_list[8][6].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir87():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 7,oyuncu)):
        matrix[8][7] += 1
        buton_list[8][7].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")


def degistir88():
    if secim_sayisi<=0:
        messagebox.showerror("Hata","Seçim hakkınız bitti.\nLütfen ekranı kapatıp diğer oyuncuya veriniz")
        return
    if (izin_var_mi(8, 8,oyuncu)):
        matrix[8][8] += 1
        buton_list[8][8].config(bg="grey", state=tk.DISABLED)
        if secim_sayisi==0:
            messagebox.showwarning("Uyarı", "Seçim hakkınız bitti.Lütfen diğer oyuncuya verin")
    else:
        messagebox.showwarning("Uyarı", "Buraya ulaşamazsınız.\nLütfen ulaşabildiğiniz yerlete tahta koyun")