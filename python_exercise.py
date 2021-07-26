# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:14:33 2021

@author: talha
"""

class Cat:
    name = ""
    surname = ""
    age = 0
    def __init__(self): # class içinndeki tüm fonksiyonlar self almalı
        self.name = "cat"

cat1 = Cat()  #sınıfların objeleri parantez ile tanımlanır
print(cat1.name)




# if __name__ == "__main__":
#     # pass



class Feline:
    
    def __init__(self,name):
        self.name = name   # basta degisken tanımana gerek yok böylede tanımlayabilirsin 
        print("Creating a feeline")
        
        
feel = Feline("cat2")
print(feel.name)

# class inheritance

class Live:
    name = []
    age = 0
    kind = ""
    born_place = ""
    def __init__(self,name,age,kind,born_place):
        print("New live is created--")
        self.name = name
        self.age = age
        self.kind = kind 
        self.born_place = born_place
    def shout(self):
        print("DOnt make me angry i",self.name)
    
#inheritace alacağımız sınıf Live tepe sınıf

class Human(Live): # live dan inherit aldık
    def __init__(self): # Eğer kendi init fonksiyonumuz yoksa inherit aldığımız sınıfın initi 
        super().__init__("name", 0, "kind", "born_place") # yukarıdaki constructora girdi.
        print("Heyy") # hem üstteki inite hemde hemde alta girmez
        #contructor ı override etmek kötü bir fikri çünkü Live ın initinde hayati islemler oabşr
        
        #örnek name Live in __initinde tanımlanmış olsaydı bize super i cagırmadan name
        # sorarsak hata verir.çümkü oranın initini geçtik
    

hum1 = Human()
hum1.shout()   # üst sınıfın foksiyonlarını kullanabiliriz .
    
    