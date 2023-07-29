import re
import time

def SortAcendant(list):
    for i in range(int(len(list)/2)):
        temp = list[i];
        list[i] = list[len(list)-1 -i];
        list[len(list)-1 -i] = temp;
    return list

def LetraParalela(abc,letra):
    return abc[len(abc)-1- abc.index(letra)]

def ConvertirListaEnString(lista):
    string = ""
    for elemento in lista:
        string += elemento
    return string

abc = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]

string = input("Ingresar frase: ")
string_codificado = ""

for letra in string:
    string_codificado += LetraParalela(abc, letra)
            
print(string_codificado)
