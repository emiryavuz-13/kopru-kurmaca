def yapay_zeka_secim_fonk(secim):
    global yapay_zeka_bool,secim_sayisi,tekrar_yok

    while yapay_zeka_bool:#İlk değeri seç ve bi daha buraya girme
        while True:
            random_sayi=random.randint(0,4)
            if matrix[random_sayi][secim]>=0:
                break

        secim_liste_2.append([random_sayi, secim])
        yapay_zeka_bool=False


    if secim<secim_sayisi: #eğer yeterli seçim yaptıysak return et
        return
    else:  #bulunduuğumuz karelerin sol alt,orta ve üst bloklarına bak taş var mı diye. Var ise orayı seçmiyeceğiz
        alt=1
        orta=1
        ust=1
        random_sayi=random.randint(0,5)

        if matrix[secim_liste_2[-1][0]][secim - 1]==-1:
            orta=-1

        if secim_liste_2[-1][0]-1==-1:
            ust=-1
        elif matrix[secim_liste_2[-1][0] - 1][secim - 1]==-1:
            ust=-1

        try:
            if secim_liste_2[-1][0]+1==-1:
                alt=-1
            elif matrix[secim_liste_2[-1][0] + 1][secim - 1]==-1:
                alt=-1
        except:
            alt=-1

        if alt<0 and orta<0 and ust<0:  #Diyelim ki her 3 tarafta da taş var o zaman kendi atl ve üstümüze bakıyoruz. Eğer her ikisinde de taş varsa veyahut daha önce seçtiğimiz bir bloğu seçmemiz gerekiyorsa fonksiyonu sıfırla baştan çağır, baştan seçim yapsın.eğer alt ve üstümden herhangibirisi müsaitse müsait olanlardan birini seç
            ustum=1
            altim=1

            if secim_liste_2[-1][0]-1==-1:
                ustum=-1
            elif matrix[secim_liste_2[-1][0] - 1][secim]==-1:
                ustum=-1


            try:
                if secim_liste_2[-1][0]+1==-1:
                    ustum=-1
                elif matrix[secim_liste_2[-1][0] + 1][secim]==-1:
                    altim=-1
            except:
                altim=-2

            if altim<0 and ustum<0:
                tekrar_yok=True
                return

            elif altim<0:
                if [secim_liste_2[-1][0] - 1, secim] in secim_liste_2:
                    tekrar_yok=True
                    return
                secim_liste_2.append([secim_liste_2[-1][0] - 1, secim])

            elif ustum < 0 :
                if [secim_liste_2[-1][0] + 1, secim] in secim_liste_2:
                    tekrar_yok=True
                    return

                secim_liste_2.append([secim_liste_2[-1][0] + 1, secim])
            else:
                if ([secim_liste_2[-1][0] - 1, secim] in secim_liste_2) and ([secim_liste_2[-1][0] + 1, secim] in secim_liste_2):
                    tekrar_yok=True
                    return
                if random_sayi<3:
                    secim_liste_2.append([secim_liste_2[-1][0] - 1, secim])
                else:
                    secim_liste_2.append([secim_liste_2[-1][0] + 1, secim])
            print("Burdayım")
            secim_sayisi+=1
            yapay_zeka_secim_fonk(secim)

        else: #diyelim ki sol alt, orta ve üst karelerden herhangibiri müsait o zaman uygun olanlarından herhangibirini seç
            if alt<0 and orta<0: #Eğer alt ve orta müsait değilse mecbur sol üst kareyi seçeceğiz
                secim_liste_2.append([secim_liste_2[-1][0] - 1, secim - 1])

            elif orta<0 and ust<0: #Eğer sol orta ve üst kareler müsait değilse mecbur sol alt kareyi seçeceğiz
                secim_liste_2.append([secim_liste_2[-1][0] + 1, secim - 1])

            elif ust<0 and alt<0: #Eğer sol alt ve üst kareler müsait değilse mecbur sol orta kareyi sececeğiz
                secim_liste_2.append([secim_liste_2[-1][0], secim - 1])


            elif ust<0: #Eğer sol üst kare müsait değilse %50 ihtimalle orta, %50 ihtimalle alt kareyi seçiceğiz
                if random_sayi<3:
                    secim_liste_2.append([secim_liste_2[-1][0], secim - 1])
                else:
                    secim_liste_2.append([secim_liste_2[-1][0] + 1, secim - 1])

            elif orta<0:#Eğer sol orta kare müsait değilse %50 ihtimalle alt, %50 ihtimalle ust kareyi seçiceğiz
                if random_sayi<3:
                    secim_liste_2.append([secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    secim_liste_2.append([secim_liste_2[-1][0] + 1, secim - 1])

            elif alt<0: #Eğer sol alt kare müsait değilse %50 ihtimalle ust, %50 ihtimalle alt kareyi seçiceğiz
                if random_sayi<3:
                    secim_liste_2.append([secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    secim_liste_2.append([secim_liste_2[-1][0], secim - 1])

            else: #Eğer hepsi müsaitse her birinin %33 şansı var ve herhangibirine gideceğiz demektir
                if random_sayi<2:
                    secim_liste_2.append([secim_liste_2[-1][0], secim - 1])
                elif random_sayi<4:
                    secim_liste_2.append([secim_liste_2[-1][0] - 1, secim - 1])
                else:
                    secim_liste_2.append([secim_liste_2[-1][0] + 1, secim - 1])
            yapay_zeka_secim_fonk(secim-1)

