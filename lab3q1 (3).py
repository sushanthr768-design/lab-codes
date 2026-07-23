unit=int(input("enter the no of units"))
if unit <= 100:
    amu = 2*unit
elif unit <= 200:
    amu = 3.5*unit
elif unit <= 300:
    amu = 4.5*unit
else:
    amu = 6*unit          
if unit <= 300:
  if amu <= 200:
    print("units consumed : ",unit)
    print("Bill Before Discount : Rs 200.00 (min. bill applied)")
    print("Discount amount : Rs 00.00")
    print("Final Payable Amount : Rs 200.00")
  else:
    print("units consumed : ",unit)
    print("Bill Before Discount : Rs ",amu)
    print("Discount amount : Rs 00.00 ")
    print("Final Payable Amount : Rs ",amu)   
elif unit <= 500:
    print("units consumed : ",unit)
    print("Bill Before Discount : Rs ",amu)
    dis = amu*0.05
    amu=amu-dis
    print("Discount amount : Rs ",dis)
    print("Final Payable Amount : Rs ",amu)
else:
    print("units consumed : ",unit)
    print("Bill Before Discount : Rs ",amu)
    dis=amu*0.1
    amu=amu-dis
    print("Discount amount : Rs ",dis)
    print("Final Payable Amount : Rs "amu) 
                                              
