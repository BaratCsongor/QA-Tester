# Declarare informatii personale
name = "Barat Csongor"
age = 37
isMarried = True

# Afisare informatii personale
print (f"Numele meu este Csongor, am {age} ani.")
print ("Casatorit:", isMarried)
print ("\n")

# Lists + tuples + Sets

# Lists

# Creare lista 

cars=["Audi", "Wolkswagen", "Bmw", "Wolkswagen", "Dacia", "Mercedes", "Dacia"]

print(cars[0])


# Stergere din lista

# Afisare lista initiala
print(cars,"\n")
# Sterge primul elemenmt care indeplineste conditia
cars.remove("Wolkswagen")
# Afisare lista dupa stergere
print("Lista dupa stergere:", cars,"\n")

# Stergere cu index
cars.pop(5)
print("Lista dupa stergerea elementului cu index:", cars,"\n")

# Adaugare in lista

# Adaugare la sfarsitul listei
cars.append("Volvo")
print("Adaugare la sfarsitul listei:", cars,"\n")

# Adaugare in pozitia definita cu index, inserare
cars.insert(0,"Ford")
cars.insert(3,"Ferrari")
print("Lista dupa insert:", cars,"\n")





# Tema carti preferate

# Definire seturi
book1 = {"title":"Tom Sawyer", "writer":"Mark Twain", "status":"Finished" }
book2 = {"title":"The last   ", "writer":"Mark Twain", "status":"Finished" }
book3 = {"title":"Harry Potter", "writer":"J. K. Rawling", "status":"In progress" }
books =[book1,book2,book3]

# Afisare element din lista
print (books[0])
print (books[1])
print (books[2])
print("\n")
 
# Afisare carte preferata
print("Cartea mea preferata este: '" + book1["title"] + "'", "scris de", book1["writer"]+".")
print("\n")

# Exercitii

# Afisare lista cu for statement
for i in  books : 
    print (i)
print("\n")


# Cautare carte in lista
bookInList = False
for i in  books: 
    if i["title"] == "Tom Sawyer":
        bookInList = True  
if bookInList == True:
    print ("Am gasit cartea preferata in lista.")
else: 
    print ("Nu am gasit cartea preferata in lista.")

