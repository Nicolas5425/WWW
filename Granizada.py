print "Granizada"
x=int(raw_input("Ingrese un Numero"))
if x%2==0:
    if x/2==1:
        print x,"1"
    else:
        a=x/2
        if a%2==0:
            if a/2==1:
                print x,a,"1"
            else:
                b=a/2
                if b%2==0:
                    if b/2==1:
                        print x,a,b,"1"
                elif b%2!=0:
                    c=b*3+1
        elif a%2!=0:
            b=a*3+1
