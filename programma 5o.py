i= 1
for i in range(1000):
    n = raw_input("dwse noumero")
    l = len (n)
    
    if l > 0 and l <10:
        print ("is harshad number")
        print l
    elif l > 9 and l<100:
        m=  l % 10
        d=  l // 10
        s= m+ d
        g= m * d
        if ( l % s)==0:
            print ("is a harshad number")
            g = (l % 10) * (l // 10)
        if g!=0:
            if (l % g)==0:
                print l
        elif g==0:
            print ("mi epitrepti")
    elif l>99 and l<1000:
        m= l % 10
        d=( l // 10) % 10
        e=( l // 10) // 10
        s= m + d + e
        gin= m * d * e
        if (l % s)==0:
            print ("is a harshad number")
        if g!=0:
            if (l % g)==0:
                print (l)
        elif g==0:
             print ("mi epitrpeti")
    elif l==1000:
        print ("is a harshad number")
        print ("mi epitrepeti")
