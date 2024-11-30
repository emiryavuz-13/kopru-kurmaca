import random
import config as c


def yapay_zeka_secim_fonk(secim):
    while c.yapay_zeka_bool:  #İlk değeri seç ve bi daha buraya girme
        while True:
            random_sayi = random.randint(0, 4)
            if c.matrix[random_sayi][secim] >= 0:
                break

        c.secim_liste_2.append([random_sayi, secim])
        c.yapay_zeka_bool = False

    if secim < c.secim_sayisi:  #eğer yeterli seçim yaptıysak return et
        return
    else:  #bulunduuğumuz karelerin sol alt,orta ve üst bloklarına bak taş var mı diye. Var ise orayı seçmiyeceğiz
        alt = 1
        orta = 1
        ust = 1
        random_sayi = random.randint(0, 5)

        if c.matrix[c.secim_liste_2[-1][0]][secim - 1] == -1:
            orta = -1

        if c.secim_liste_2[-1][0] - 1 == -1:
            ust = -1
        elif c.matrix[c.secim_liste_2[-1][0] - 1][secim - 1] == -1:
            ust = -1

        try:
            if c.secim_liste_2[-1][0] + 1 == -1:
                alt = -1
            elif c.matrix[c.secim_liste_2[-1][0] + 1][secim - 1] == -1:
                alt = -1
        except:
            alt = -1

        if alt < 0 and orta < 0 and ust < 0:  #Diyelim ki her 3 tarafta da taş var o zaman kendi atl ve üstümüze bakıyoruz. Eğer her ikisinde de taş varsa veyahut daha önce seçtiğimiz bir bloğu seçmemiz gerekiyorsa fonksiyonu sıfırla baştan çağır, baştan seçim yapsın.eğer alt ve üstümden herhangibirisi müsaitse müsait olanlardan birini seç
            ustum = 1
            altim = 1

            if c.secim_liste_2[-1][0] - 1 == -1:
                ustum = -1
            elif c.matrix[c.secim_liste_2[-1][0] - 1][secim] == -1:
                ustum = -1

            try:
                if c.secim_liste_2[-1][0] + 1 == -1:
                    ustum = -1
                elif c.matrix[c.secim_liste_2[-1][0] + 1][secim] == -1:
                    altim = -1
            except:
                altim = -2

            if altim < 0 and ustum < 0:
                c.tekrar_yok = True
                return
            elif altim < 0:
                if [c.secim_liste_2[-1][0] - 1, secim] in c.secim_liste_2:
                    c.tekrar_yok = True
                    return
                c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim])

            elif ustum < 0:
                if [c.secim_liste_2[-1][0] + 1, secim] in c.secim_liste_2:
                    c.tekrar_yok = True
                    return

                c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim])
            else:
                if ([c.secim_liste_2[-1][0] - 1, secim] in c.secim_liste_2) and (
                        [c.secim_liste_2[-1][0] + 1, secim] in c.secim_liste_2):
                    c.tekrar_yok = True
                    return
                if random_sayi < 3:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim])
                else:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim])
            print("Burdayım")
            c.secim_sayisi += 1
            yapay_zeka_secim_fonk(secim)

        else:  #diyelim ki sol alt, orta ve üst karelerden herhangibiri müsait o zaman uygun olanlarından herhangibirini seç
            if alt < 0 and orta < 0:  #Eğer alt ve orta müsait değilse mecbur sol üst kareyi seçeceğiz
                c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])

            elif orta < 0 and ust < 0:  #Eğer sol orta ve üst kareler müsait değilse mecbur sol alt kareyi seçeceğiz
                c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])

            elif ust < 0 and alt < 0:  #Eğer sol alt ve üst kareler müsait değilse mecbur sol orta kareyi sececeğiz
                c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])


            elif ust < 0:  #Eğer sol üst kare müsait değilse %50 ihtimalle orta, %50 ihtimalle alt kareyi seçiceğiz
                if random_sayi < 3:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])
                else:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])

            elif orta < 0:  #Eğer sol orta kare müsait değilse %50 ihtimalle alt, %50 ihtimalle ust kareyi seçiceğiz
                if random_sayi < 3:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])

            elif alt < 0:  #Eğer sol alt kare müsait değilse %50 ihtimalle ust, %50 ihtimalle alt kareyi seçiceğiz
                if random_sayi < 3:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])

            else:  #Eğer hepsi müsaitse her birinin %33 şansı var ve herhangibirine gideceğiz demektir
                if random_sayi < 2:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])
                elif random_sayi < 4:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])
            yapay_zeka_secim_fonk(secim - 1)


def ogrenmis_yapay_zeka_secim_fonk(secim):
    global ilk_secim
    ilk_secim_list = []
    skor = 0
    uzunluk = len(c.skor_matrix)
    while c.yapay_zeka_bool:  #İlk değeri seç ve bi daha buraya girme
        print(c.skor_matrix, "sayii")
        for i in range(uzunluk):
            if c.skor_matrix[i][uzunluk - 1] >= 0:
                skor += c.skor_matrix[i][uzunluk - 1]
                ilk_secim_list.append(skor)
            else:
                ilk_secim_list.append(-1)
        random_sayi = random.randint(0, skor)

        for i in range(len(ilk_secim_list)):

            if ilk_secim_list[i] >= random_sayi:
                ilk_secim = i
                break

        c.secim_liste_2.append([ilk_secim, secim])
        c.yapay_zeka_bool = False

    if secim < c.secim_sayisi:  #eğer yeterli seçim yaptıysak return et
        return


    else:  #bulunduuğumuz karelerin sol alt,orta ve üst bloklarına bak taş var mı diye. Var ise orayı seçmiyeceğiz

        olasilik_liste = []
        skor = 0

        if c.secim_liste_2[-1][
            0] == 0:  #eğer en üstte isek sadece bir sol hizamızdaki ve bir sol altımızdakine bakıcaz ve ağırlığına göre alıcağız

            if c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1]
                olasilik_liste.append(skor)

            if c.skor_matrix[c.secim_liste_2[-1][0] + 1][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0] + 1][secim - 1]
                olasilik_liste.append(skor)

            random_sayi = random.randint(0, skor)

            for i in range(len(olasilik_liste)):  #Ağırlığına göre seç
                if olasilik_liste[i] >= random_sayi:
                    if i == 0:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])  #aynı hizada seçilecek
                    elif i == 1:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])  #bir alt satırı seç
                    break
            ogrenmis_yapay_zeka_secim_fonk(secim - 1)  # Recursive et

        elif c.secim_liste_2[-1][0] == uzunluk - 1:  #eğer en alt satırı seçtiysek
            if c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1]
                olasilik_liste.append(skor)

            if c.skor_matrix[c.secim_liste_2[-1][0] - 1][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0] - 1][secim - 1]
                olasilik_liste.append(skor)

            random_sayi = random.randint(0, skor)
            print("Şu değer için dönüyorum ", secim - 1, "|| olasılık listem:", olasilik_liste, "|| Rasgele sayım:",
                  random_sayi)
            for i in range(len(olasilik_liste)):  # Ağırlığına göre seç
                if olasilik_liste[i] >= random_sayi:
                    if i == 0:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])  # aynı hizada seçilecek
                    elif i == 1:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])  # bir alt satırı seç
                    break
            ogrenmis_yapay_zeka_secim_fonk(secim - 1)  # Recursive et
        else:
            if c.skor_matrix[c.secim_liste_2[-1][0] - 1][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0] - 1][secim - 1]
                olasilik_liste.append(skor)

            if c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0]][secim - 1]
                olasilik_liste.append(skor)

            if c.skor_matrix[c.secim_liste_2[-1][0] + 1][secim - 1] < 0:
                olasilik_liste.append(-1)
            else:
                skor += c.skor_matrix[c.secim_liste_2[-1][0] + 1][secim - 1]
                olasilik_liste.append(skor)

            random_sayi = random.randint(0, skor)
            print("Şu değer için dönüyorum ", secim - 1, "|| olasılık listem:", olasilik_liste, "|| Rasgele sayım:",
                  random_sayi)
            for i in range(len(olasilik_liste)):  # Ağırlığına göre seç
                if olasilik_liste[i] >= random_sayi:
                    if i == 0:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0] - 1, secim - 1])  # üst satır seçilecek
                    elif i == 1:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0], secim - 1])  # aynı hizada seçilecek
                    elif i == 2:
                        c.secim_liste_2.append([c.secim_liste_2[-1][0] + 1, secim - 1])  # bir alt satırı seç
                    break
            ogrenmis_yapay_zeka_secim_fonk(secim - 1)  # Recursive et
