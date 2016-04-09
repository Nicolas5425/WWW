print "Elija Opcion 1.Calculadora, 2.Impar o Par"
sel1=int(raw_input("Que Opcion Desea Elegir?"))
if sel1==1:
    op=(raw_input("Que Opcion Desea Elegir (+, -, *, /"))
    if op=="+":
        val1=int(raw_input("Ingresa Primer Dato"))
        val2=int(raw_input("Ingresa Segundo Dato"))
        print "Suma", val1 + val2
    else:
        if op=="-":
            val1=int(raw_input("Ingresa Primer Dato"))
            val2=int(raw_input("Ingresa Segundo Dato"))
            print "Resta", val1 - val2
        else:
            if op=="*":
                val1=int(raw_input("Ingresa Primer Dato"))
                val2=int(raw_input("Ingresa Segundo Dato"))
                print "Multiplicacion", val1 * val2
            else:
                if op=="/":
                    val1=int(raw_input("Ingresa Primer Dato"))
                    val2=int(raw_input("Ingresa Segundo Dato"))
                    if val2!=0:
                        print "Division", val1 / val2
                        print "Residuo", val1 % val2
else:
    if sel1==2:
        val2=int(raw_input("Ingrese Numero"))
        if val2%2==0:
            print "Es Par"
        else:
            print "Es Impar"
    else:
        print "Es Bobo"
