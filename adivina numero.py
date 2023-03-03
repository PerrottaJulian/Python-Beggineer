#inportar carpeta "random"
import random;
#declaracion
numsec = int()
resp = int()

#inicializacion
numsec = 0
resp = 0

#desarrollo
numsec = random.randint(1,10);

print ("""******************BINEVENIDO A ADIVINA EL NUMERO**********************

                Se generara un numero aleatorio del 1 al 10
                      ¡¡Adivina cual salio!!
                      
                      ****Tiene 5 intentos***
                                                                                         """);


intentos = 5;
resp = int(input("Que numero cree que salio?: "));

while (intentos > 0 or numsec != resp ):

    if (resp > 10 or resp < 0):
        print ("Ingreso un numero no valido, recuerde que el numero que tiene que adivinar esta entre 1 y 10. Se le devuelve el intento");

    elif (resp > numsec ):
        print ("Muy alto");
    elif (resp < numsec ):
        print ("Muy bajo");
        
    intentos = intentos - 1;
    print ("Le quedan ", intentos, "intentos");
        
    resp = int(input("Que numero cree que salio?: "));
    
    if (resp == numsec):
        print ("Felicidades, a adivinado!");
        break;
        
    if (intentos == 0):
        print("Se quedo sin intentos, perdio :(")
        print ("El numero secreot era: ", numsec)
        

