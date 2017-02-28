# -*- coding: cp1253 -*-
n=raw_input("δώσε αριθμούς")
l=list(n)
megethos=len(l)
m=max(l)
mik=min(l)
plmik=l.count(mik)
plm=l.count(m)
plm2=0
plmik2=0
mik2=0
m=0
athroisma=0
mo=0
t=False
t1=False
i=1

while i<megethos and t==True and t1==True:
    if x[c]<m:
        m=l[1]
        t=True
    if x[c]>mik:
        mik2=l[1]
        t1=True
    c=c+1

while i <megethos:
    if l[i]<mik2:
    	m2=l[i]
    	plmik=0
    if l[i]==mik2:
    	mik2=l[i]
    	plmik=plmin+1
    if l[i]>m:
    	m2=l[i]
    	plm=0
    if l[i]==m:
    	m2=l[i]
    	plm=plm+1
 athroisma=athroisma+l[i]
 megethos=megethos+1
 i=i+1

fmeg=meg-(plm+plmik+plm1+plmik1)
if fmeg!=0:
    mo=athroisma/megethos
    print mo
elif fmeg==0:
    print ("αδύνατη πράξη")
