def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multi(x,y):
    return x*y
def div(x,y):
    return x/y

def Menu():
    """Funcion que Muestra el Menu"""
    print("----claculadora----")
    print("1)    suma   ")
    print("2)    resta   ")
    print("3)    multiplicacion   ")
    print("4)    division   ")

def main():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print ("La Suma es:", suma(x,y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print ("La Resta es:",resta(x,y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",multi(x,y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            print ("La Division es:", div(x,y))
            opc = int(input("Selecione Opcion\n"))
main()