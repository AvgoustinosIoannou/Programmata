p=raw_input("Dwse parastasi")
x=p.count("(")
g=p.count(")")
h=0
if p[1]=="(" and p[-1]==")":
 eleg=True
 for i in p:
     if p[1]=="(":
        h=h+1
else:
    h=h-1
if h<0:
    eleg=False
else:
    eleg=False
if eleg and h==0:
    print "parastasi"
elif eleg==False:
    print "oxi parastasi"
