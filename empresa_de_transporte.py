ton = int();
km = int();
abono = float();
pretot = float();

ton = 0;
km = 0;
abono = 0.0;
pretot = 0.0;

IVA = 21/100;

ton = int(input("Ingrese el peso de la carga (en toneladas): "));
km = int(input("Ingrese la distancia recorrida (en km): "));

if (ton <= 0 or km <= 0):
    print ("Hubo un error, no puede ingressar ni toneladas ni kilometos negativos o nulos");
else:
    if (ton <= 2):
        abono = 1.80 * km;
        
    elif (ton <= 10):
        abono = 1.50 * km;
        
    elif (ton <= 20):
        abono = 1.00 * km; 
        
    else:
        abono = 0.50 * km;

pretot = abono + abono * IVA;

print ("Debe pagar $", pretot);
        
        
   
