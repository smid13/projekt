text = {
'1':
'''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. 
'''
,'2':'''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.
''',
    '3' :
'''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.
'''}

lomitka = '-'*40
users = {'bob':'123','ann':'pass123','mike':'password123','liz':'pass123'}

# přihlášení do systemu a ověření

print(users)

user = input('Enter your username : ')
password = input('Enter your password: ')
print(lomitka)

if user in users.keys() and users.get(user) == password:
     print(f"Welcome to the app, {user} \nWe have 3 texts to be analyzed")
     print(lomitka)

else:
    print('the username or password you entered is incorrect')
    exit()

# vybrání textu

vyber_text = input('Enter a number between 1 and 3 to select: ')
if vyber_text.isalpha() :
    print('you entered the wrong value (must be digit) ')
    exit()

elif int(vyber_text) >3 or int(vyber_text)<1 :
    print('you entered the wrong value ( must be btw 1 and 3)')
    exit()
print(lomitka)

vybrany_text = text[vyber_text]

print(f"Your selected text is\n{vybrany_text}\n {lomitka}")

# prace s textem, rozdeleni po slovech, vycisteni

vycistena_slova = []
jednotliva_slova = vybrany_text.split()
for a in jednotliva_slova:
    vycistena_slova.append(a.strip(",.:?!"))

# pocet slov
pocet_slov = len(vycistena_slova)

# pocet slov zacinajicich velkym pismenem
velka_pismena = []
for a in vycistena_slova:
    if a[0].isupper():
        velka_pismena.append(a)

pocet_velka_pismena = len(velka_pismena)

# pocet slov psanych velkymi pismeny

cela_velka_slova = []
for a in vycistena_slova:
    if a.isupper() and a.isalpha():
        cela_velka_slova.append(a)
pocet_cela_velka_slova = len(cela_velka_slova)


# pocet slov psanych malymi pismeny

mala_slova = []
for a in vycistena_slova:
    if a.islower():
        mala_slova.append(a)
pocet_mala_slova = len(mala_slova)


# pocet cisel

cisla = []
for a in vycistena_slova:
    if a.isdigit():
        cisla.append(a)
pocet_cisla = len(cisla)


# suma vsech cisel

suma = []
for a in cisla:
    suma.append(int(a))
suma_cisel = sum(suma)

# vypsani rešení

print(f"There are {pocet_slov} words in the selected text.\nThere are {pocet_velka_pismena} titlecase words.\nThere are {pocet_cela_velka_slova} uppercase words.\nThere are {pocet_mala_slova} lowercase words.\nThere are {pocet_cisla} numeric strings.\nThe sum of all the numbers {suma_cisel}.\n{lomitka}")

# cetnost ruznych delek slov v textu + graf

slova_podle_delky = dict()
for a in vycistena_slova:
   slova_podle_delky[len(a)] = slova_podle_delky.get(len(a),0)+1

print("LEN|  OCCURENCES  |NR.")
print(lomitka)

for a,i in slova_podle_delky.items():
    print(a,"  ","*"*i,"  ",i)


