for i in range(0, 10):
    print "Digite su Opcion"
    print "1. Papas Fritas ($1200)"
    print "2. Sandwich Combinado ($2500)"
    print "3. Pescadito ($1800)"
    print "4. Empanada ($1700)"
    print "5. Arepa ($2000)"
    print "6. Gaseosa ($1600)"
    print "7. Vaso de Te ($1000)"
    print "8. Dulce ($1000)"
    print "9. Salir"
    dgt=int(raw_input("..."))
    if dgt==1:
        print "Papas Fritas"
        print "$1200"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1200:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1200:
            print "Sus vueltas Son: ", mon-1200
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1200, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1200:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1200:
                print "Sus Vueltas Son: ", (mon+mon1)-1200
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1200, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1200:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1200:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1200
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1200, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1200:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1200:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1200
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==2:
        print "Sandwich Combinado"
        print "$2500"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==2500:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=2500:
            print "Sus vueltas Son: ", mon-2500
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-2500, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==2500:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=2500:
                print "Sus Vueltas Son: ", (mon+mon1)-2500
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-2500, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==2500:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=2500:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-2500
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-2500, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==2500:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=2500:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-2500
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Le Falta $",(mon+mon1+mon2+mon3)-2500, "Pesos"
                        mon4=int(raw_input("Ingrese el Dinero Faltante..."))
                        if mon+mon1+mon2+mon3+mon4==2500:
                            print "Entregando Producto..."
                            print "<<<<>>>>"
                        elif mon+mon1+mon2+mon3+mon4>=2500:
                            print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3+mon4)-2500
                            print "Entregando Producto..."
                            print "<<<<>>>>"
                        else:
                            print "Comience de Nuevo..."
                            print "<<<<>>>>"
    elif dgt==3:
        print "Pescadito"
        print "$1800"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1800:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1800:
            print "Sus vueltas Son: ", mon-1800
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1800, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1800:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1800:
                print "Sus Vueltas Son: ", (mon+mon1)-1800
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1800, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1800:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1800:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1800
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1800, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1800:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1800:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1800
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==4:
        print "Empanada"
        print "$1700"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1700:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1700:
            print "Sus vueltas Son: ", mon-21700
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1700, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1700:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1700:
                print "Sus Vueltas Son: ", (mon+mon1)-1700
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1700, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1700:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1700:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1700
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1700, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1700:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1700:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1700
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==5:
        print "Arepa"
        print "$2000"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==2000:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=2000:
            print "Sus vueltas Son: ", mon-2000
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-2000, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==2000:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=2000:
                print "Sus Vueltas Son: ", (mon+mon1)-2000
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-2000, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==2000:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=2000:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-2000
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-2000, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==2000:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=2000:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-2000
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==6:
        print "Gaseosa"
        print "$1600"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1600:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1600:
            print "Sus vueltas Son: ", mon-1600
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1600, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1600:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1600:
                print "Sus Vueltas Son: ", (mon+mon1)-1600
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1600, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1600:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1600:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1600
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1600, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1600:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1600:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1600
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==7:
        print "Vaso de Te"
        print "$1000"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1000:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1000:
            print "Sus vueltas Son: ", mon-1000
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1000, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1000:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1000:
                print "Sus Vueltas Son: ", (mon+mon1)-1000
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1000, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1000:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1000:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1000
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1000, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1000:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1000:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1000
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==8:
        print "Dulce"
        print "$1000"
        mon=int(raw_input("Ingrese Su Dinero"))
        if mon==1000:
            print "Entregando Producto..."
            print "<<<<>>>>"
        elif mon>=1000:
            print "Sus vueltas Son: ", mon-1000
            print "Entregando Producto..."
            print "<<<<>>>>"
        else:
            print "Le Falta $",mon-1000, "Pesos"
            mon1=int(raw_input("Ingrese el Dinero Faltante... "))
            if mon+mon1==1000:
                print "Entregando Producto..."
                print "<<<<>>>>"
            elif mon+mon1>=1000:
                print "Sus Vueltas Son: ", (mon+mon1)-1000
                print "Entregando Producto..."
                print "<<<<>>>>"
            else:
                print "Le Falta $",(mon+mon1)-1000, "Pesos"
                mon2=int(raw_input("Ingrese el Dinero Faltante..."))
                if mon+mon1+mon2==1000:
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                elif mon+mon1+mon2>=1000:
                    print "Sus Vueltas Son: ", (mon+mon1+mon2)-1000
                    print "Entregando Producto..."
                    print "<<<<>>>>"
                else:
                    print "Le Falta $",(mon+mon1+mon2)-1000, "Pesos"
                    mon3=int(raw_input("Ingrese el Dinero Faltante..."))
                    if mon+mon1+mon2+mon3==1000:
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    elif mon+mon1+mon2+mon3>=1000:
                        print "Sus Vueltas Son: ", (mon+mon1+mon2+mon3)-1000
                        print "Entregando Producto..."
                        print "<<<<>>>>"
                    else:
                        print "Comience de Nuevo"
                        print "<<<<>>>>"
    elif dgt==9:
        print "Salir"
        exit
    else:
        print "Elija la Opcion Indicada"
        print "<<<<>>>>"
    
