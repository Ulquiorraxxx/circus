#RonaldsPoļakovs 
# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import random





player_location = 1
ai_location = 1


def player_move():
    global player_location
    print("Jūsu gājiens (uzrakstat 'mest' lai mestu kaulinu)")
    metiens=input()
    #ja tiek iavadīt "mest" tad izpildas visa pārējā funkcija, ja ne tad izvada kļūdu
    if metiens == "mest":
        kaulins = random.randint(1 ,6)
        print("Jūs uzmetāt: " , kaulins)
        player_location = player_location + kaulins
        # ja player_location ir vienāds ar x skaitli tad player locationmainās pēcnoteiktiem nosacījumiem un izvada tagadējospēlētāja atrašanās vietu
        if player_location == 7: 
            player_location = 18
            print("Jums paveicās, jūs dodaties pa kāpnēm uz 18 lauciņu")
        elif player_location == 46:
            player_location = 67
            print("Jums paveicās, jūs dodaties pa kāpnēm uz 67 lauciņu")
        elif player_location == 63:
            player_location = 74
            print("Jums paveicās, jūs dodaties pa kāpnēm uz 74 lauciņu")
        elif player_location == 69:
            player_location = 80
            print("Jums paveicās, jūs dodaties pa kāpnēm uz 80 lauciņu")

        elif player_location == 24:
            player_location = 15
            print("Jums nepaveicās jūs noslīdat pa kāpnēm uz 15. lauciņu")
        elif player_location == 48:
            player_location = 39
            print("Jums nepaveicās jūs noslīdat pa kāpnēm uz 39. lauciņu")
        elif player_location == 52:
            player_location = 33
            print("Jums nepaveicās jūs noslīdat pa kāpnēm uz 33. lauciņu")
        elif player_location == 96:
            player_location = 87
            print("Jums nepaveicās jūs noslīdat pa kāpnēm uz 87. lauciņu")
        else:
            print("Jūs atrodaties uz " , player_location , ". lauciņa")
    else:
        print("kļūda")

def ai_move():
    global ai_location
    print("Pretinieka gājiens")
    kaulins = random.randint(1 , 6)
    print("Pretinieks uzmeta: " , kaulins)
    ai_location = ai_location + kaulins
    #Ja ai_location ir vienāds ar kādu no x skaitļiem tad ai_location mainās uz noteiktu skaitlisko vērtību un izvada tagadējo ai_location pozīciju, ja neizpildās tad izvada ai_location bez tā izmaiņām
    if ai_location == 7:
        ai_location = 18
        print("Pretiniekam paveicās, pretinieks dodas pa kāpnēm uz 18 lauciņu")
    elif ai_location == 46:
        ai_location = 67
        print("Pretiniekam paveicās, pretinieks dodas pa kāpnēm uz 67 lauciņu")
    elif ai_location == 63:
        ai_location = 74
        print("Pretiniekam paveicās, pretinieks dodas pa kāpnēm uz 74 lauciņu")
    elif ai_location == 69:
        ai_location = 80
        print("Pretiniekam paveicās, pretinieks dodas pa kāpnēm uz 80 lauciņu")

    elif ai_location == 24:
        ai_location = 15
        print("Pretiniekam nepaveicās pretinieks noslīd pa kāpnēm uz 15. lauciņu")
    elif ai_location == 48:
        ai_location = 39
        print("Pretiniekam nepaveicās pretinieks noslīd pa kāpnēm uz 39. lauciņu")
    elif ai_location == 52:
        ai_location = 33
        print("Pretiniekam nepaveicās pretinieks noslīd pa kāpnēm uz 33. lauciņu")
    elif ai_location == 96:
        ai_location = 87
        print("Pretiniekam nepaveicās pretinieks noslīd pa kāpnēm uz 87. lauciņu")
    else:
        print("Pretinieks atrodas uz " , ai_location , ". lauciņa")


def game():
    global player_location
    global ai_location 
    print("Spēle sākusies")
    for x in range(30): #ierobežo gājienu skaitu 
        if player_location < 100: #ja spēlētāja location ir mazāks par 100 tad turpinas spēle
            player_move()
        else: #ja nav tad neturpinas
            print("Jūs uzvarējāt")
            break
        if ai_location < 100: #ja ai location ir mazāks par 100 tad turpinas spēle
            ai_move()
        else:
            print("pretinieks uzvarēja")
            break
    if player_location >=100: # ja player_locationi ir lielāks vai vienāds ar 100 tad izvada ka spēle ir beigusies
        print("Spēle beigusies")
    elif ai_location >=100: # vēl ja ai_location ir lielāks vai vienāds ar 100 tad izvada ka spēle ir beigusies 
        print("Spēle beigusies")
    else: # citādāk izvada ka ir neizšķirts jo spēle ilga vairāk par 30 gājieniem un neviens no spēlētājiem nefinišēja
        print("Neizšķirts, jūs spēlējāt pārāk ilgi :(")
game()
