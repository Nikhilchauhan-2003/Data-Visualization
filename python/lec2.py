cp= float(input("enter cost price(in rs) :"))
sp= float(input("enter selling price(in rs) :"))
if(cp <0):
    print("invalid cp" )
elif(sp<0):
     print("invalid sp" )
else:
    if(sp>cp):
        print("profit : rs",(sp-cp))
    elif(cp>sp):
         print("loss : rs",(cp-sp))
    else:
           print("no profit no loss")