#Tema if/else si for statement

# If/else Statement
if "udemy" == "Udemy":
    print("Afirmatie este corecta!")
else:
    print("Afirmatia nu este corecta!")

print("\n")
# For statement

# Creeaza o lista cu 3 caini si listeaza la fiecare numele  cu un ciclu FOR

listaCaini=["Lisa","Rex","Foxi"]

for i in listaCaini:
    print(i)
print("\n")    


# Tema functii
print("\n")

# Functia comparare doua valori intregi
def compare(x,y):
    if x>y:
        print("Primul numar introdus este mai mare!")
    elif x<y:
        print("Al doilea numar introdus este mai mare!")
    else:
        print("Numerele introduse sunt egale!")

# Verificarea functiei compare

# Caz numere egale
compare(10,10)
print("\n")

# Caz numarul1 mai mare
compare(5,2)
print("\n")

# Caz numarul2 mai mare
compare(-5,10)
print("\n")


# Functia listare 

def listare(x):
    for i in x:
        print(i)

listare(listaCaini)