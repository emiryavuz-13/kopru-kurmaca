def bos_deniz_fonk():
    global harita_tip
    harita_tip="boş"
    resim_bastirici()
def seyrek_tasli_deniz_fonk():
    global harita_tip
    harita_tip="seyrek"
    resim_bastirici()
def tasli_deniz_fonk():
    global harita_tip
    harita_tip="taşlı"
    resim_bastirici()

def kucuk_harita_fonk():
    global harita_buyukluk
    harita_buyukluk=5
    resim_bastirici()
def orta_harita_fonk():
    global harita_buyukluk
    harita_buyukluk=7
    resim_bastirici()
def buyuk_harita_fonk():
    global harita_buyukluk
    harita_buyukluk=9
    resim_bastirici()


def random_secici_fonk_5x5():
    a=random.randint(0,100)
    if a<=40:
        random_secici_liste[0]=0
    elif 40<a<=80:
        random_secici_liste[0]=1
    elif 80<a:
        random_secici_liste[0]=2

def tas_secici_fonk_5x5_seyrek():
    gecici_liste = []
    print("!!!!",random_secici_liste[0])
    if random_secici_liste[0]==0:

        for i in range(1):
            index_sec=[0,1]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(2):
            index_sec=[1,2,3]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(1):
            index_sec=[3,4]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

    elif random_secici_liste[0] == 2:

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

def tas_secici_fonk_5x5_tasli():
    gecici_liste = []
    print("!!!!", random_secici_liste[0])

    if random_secici_liste[0]==0:

        for i in range(1):
            index_sec=[0,1]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(4):
            index_sec=[1,2,3]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(1):
            index_sec=[3,4]
            sayi = random.randint(0,4)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(2):
            index_sec = [0,1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

    elif random_secici_liste[0] == 2:

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [1, 2, 3]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [3, 4]
            sayi = random.randint(0, 4)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 4)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1
def random_secici_fonk_7x7():
    a=random.randint(0,100)
    if a<=50:
        random_secici_liste[0]=0
    elif 50<a<=70:
        random_secici_liste[0]=1
    elif 70<a:
        random_secici_liste[0]=2

def tas_secici_fonk_7x7_seyrek():
    gecici_liste = []
    print("!!!!",random_secici_liste[0])
    if random_secici_liste[0]==0:

        for i in range(1):
            index_sec=[5,6]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(2):
            index_sec=[3,4]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(1):
            index_sec=[0,1]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(3):
            index_sec=[2,3]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(3):
            index_sec = [5,6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [3,4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(2):
            index_sec = [0,1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1



    elif random_secici_liste[0]==2:

        for i in range(2):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(1):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(1):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


def tas_secici_fonk_7x7_tasli():
    gecici_liste = []
    print("!!!!",random_secici_liste[0])
    if random_secici_liste[0]==0:

        for i in range(2):
            index_sec=[5,6]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(3):
            index_sec=[3,4]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(2):
            index_sec=[0,1]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(4):
            index_sec=[2,3]
            sayi = random.randint(0, 6)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,6)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(3):
            index_sec = [5,6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3,4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(3):
            index_sec = [0,1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1



    elif random_secici_liste[0]==2:

        for i in range(3):
            index_sec = [2, 3]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [0, 1]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(3):
            index_sec = [5, 6]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [3, 4]
            sayi = random.randint(0, 6)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 6)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


def random_secici_fonk_9x9():
    a=random.randint(0,100)
    if a<=35:
        random_secici_liste[0]=0
    elif 35<a<=65:
        random_secici_liste[0]=1
    elif 65<a:
        random_secici_liste[0]=2

def tas_secici_fonk_9x9_seyrek():
    gecici_liste = []
    print("!!!!",random_secici_liste[0])
    if random_secici_liste[0]==0:

        for i in range(1):
            index_sec=[0,1]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(4):
            index_sec=[2,3,4]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(4):
            index_sec=[4,5,6]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(1):
            index_sec=[7,8]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(2):
            index_sec = [0,1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2,3,4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [4,5,6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(2):
            index_sec = [7,8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1



    elif random_secici_liste[0]==2:

        for i in range(3):
            index_sec = [0,1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(2):
            index_sec = [2,3,4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(2):
            index_sec = [4,5, 6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(3):
            index_sec = [7,8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


def tas_secici_fonk_9x9_tasli():
    gecici_liste = []

    if random_secici_liste[0]==0:

        for i in range(3):
            index_sec=[0,1]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(6):
            index_sec=[2,3,4]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(6):
            index_sec=[4,5,6]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

        for i in range(3):
            index_sec=[7,8]
            sayi = random.randint(0, 8)
            sutun=random.choice(index_sec)
            while( (sayi,sutun) in gecici_liste):
                sayi=random.randint(0,8)
                sutun = random.choice(index_sec)
            gecici_liste.append((sayi,sutun))
            matrix[sayi][sutun]=-1

    elif random_secici_liste[0]==1:

        for i in range(4):
            index_sec = [0,1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2,3,4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(5):
            index_sec = [4,5,6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(5):
            index_sec = [7,8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1



    elif random_secici_liste[0]==2:

        for i in range(5):
            index_sec = [0,1]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(4):
            index_sec = [2,3,4]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


        for i in range(4):
            index_sec = [4,5,6]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1

        for i in range(5):
            index_sec = [7,8]
            sayi = random.randint(0, 8)
            sutun = random.choice(index_sec)
            while ((sayi, sutun) in gecici_liste):
                sayi = random.randint(0, 8)
                sutun = random.choice(index_sec)

            gecici_liste.append((sayi, sutun))
            matrix[sayi][sutun] = -1


