amu = int(input("enter the amount purchased"))
mem = input("enter the Memebership type")
if amu < 1000:
  if amu < 500:
    print("Discount : 0%  (amount below Rs 500)")
    print("Delivery Charge : Rs 50.00")
    print("final amount: ",amu+50)
  else:
    if mem=="Regular":
        dis=amu*0.05
        final = amu-dis+50
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 5%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 50.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Silver":
        dis=amu*0.10
        final = amu-dis+50
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 10%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 50.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Gold":
        dis=amu*0.15
        final = amu-dis+50
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 15%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 50.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Platinum":
        dis=amu*0.20
        final = amu-dis+50
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 20%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 50.00")
        print("Final Payable Amount: Rs ",final)
    else:
        print("Error: Invalid membership type entered!")
elif 1000<amu<10000:
    if mem=="Regular":
        dis=amu*0.05
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 5%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Silver":
        dis=amu*0.10
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 10%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Gold":
        dis=amu*0.15
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 15%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Platinum":
        dis=amu*0.20
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 20%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    else:
        print("Error: Invalid membership type entered!")
elif amu >10000:
    if mem=="Regular":
        dis=amu*0.05
        dis=dis - 500
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 5%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Silver":
        dis=amu*0.10
        dis=dis - 500
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 10%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Gold":
        dis=amu*0.15
        dis=dis - 500
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 15%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    elif mem=="Platinum":
        dis=amu*0.20
        dis=dis - 500
        final = amu-dis
        print("Purchased amount: Rs ",amu)
        print("Membership type: ",mem)
        print("Discount percentage: 20%")
        print("discount amount: Rs ",dis)
        print("Delivery Charge : Rs 0.00")
        print("Final Payable Amount: Rs ",final)
    else:
        print("Error: Invalid membership type entered!")
        

