# Tema Creaza o clasa dog cu 3 atribute age, color, breed si metodele run() si eat() cu cate un mesaj...
# Creaza 3 obiecte si afiseaza la fiecare culoarea si faptul ca alearga
class dog:
    def __init__(self, age, color, breed):
        self.age = age
        self.color = color
        self.breed = breed

    def run(self):
        print("This dog is running fast!") 

    def eat(self):
        print("This dog eats everything!") 



 #OOP Definire clasa si obiecte

# Importa clasa dog din fisierul classdog.py
# from classdog import dog

# Definire obiecte din clasa dog
Rex=dog(5, "white", "Bishon")
Max=dog(2, "chocolate", "Rottweiler")
Lisa=dog(1,"black", " Belgian Shepard")

# Afisarea informatiilor 
print(Rex.color)
Rex.run()
print(Max.color)
Max.run()
print(Lisa.color)
Lisa.run()
