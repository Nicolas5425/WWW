for i in range (0, 10):
    print "Operacion de Numeros"
    print "1. Suma"
    print "2. Resta"
    print "3. Multiplicacion"
    print "4. Division y Residuo"
    print "<<<<>>>>"
    x=int(raw_input("Digite su Opcion"))
    if x==1:
        prm=int(raw_input("Ingrese el primer dato"))
        prm1=int(raw_input("Ingrese Segundo Dato"))
        print "Suma: ", prm+prm1
        print "<<<<>>>>"
    elif x==2:
        prm=int(raw_input("Ingrese el primer dato"))
        prm1=int(raw_input("Ingrese Segundo Dato"))
        print "Resta: ", prm-prm1
        print "<<<<>>>>"
    elif x==3:
        prm=int(raw_input("Ingrese el primer dato"))
        prm1=int(raw_input("Ingrese Segundo Dato"))
        print "Multiplicacion: ", prm*prm1
        print "<<<<>>>>"
    elif x==4:
        prm=int(raw_input("Ingrese el primer dato"))
        if prm !=0:
            prm1=int(raw_input("Ingrese Segundo Dato"))
            if prm1!=0:
                print "Division: ", prm/prm1
                print "Residuo: ", prm%prm1
                print "<<<<>>>>"
            else:
                print "Digite una Opcion Valida..."
                print "<<<<>>>>"
                exit
        else:
            print "Digite una Opcion Valida..."
            print "<<<<>>>>"
            exit
