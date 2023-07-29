#inportar carpeta "random"
import random;
#declaracion
numsec = int()
resp = int()
limite = int()

#inicializacion
numsec = 0
resp = 0
limite = 15

#desarrollo
numsec = random.randint(1,limite);

print (f"""******************BINEVENIDO A ADIVINA EL NUMERO**********************

                Se generara un numero aleatorio del 1 al {limite}
                      ¡¡Adivina cual salio!!
                      
                      ****Tiene 5 intentos***
                                                                                         """);


intentos = 5;

print (f"el numero: {numsec}")

while (intentos > 0 and numsec != resp ):
    resp = int(input("Que numero cree que salio?: "));

    while (resp > limite or resp < 0):
        print (f"Ingreso un numero no valido, recuerde que el numero que tiene que adivinar esta entre 1 y {limite}. Se le devuelve el intento");

    if (resp > numsec ):
        print ("Muy alto");
        intentos = intentos - 1;
    elif (resp < numsec ):
        print ("Muy bajo");
        intentos = intentos - 1;
    else:
        print ("Felicidades, a adivinado!");
        

    print ("Le quedan ", intentos, "intentos");
        
if (intentos == 0):
    print("Se quedo sin intentos, perdio :(")
    print ("El numero secreot era: ", numsec)


        

