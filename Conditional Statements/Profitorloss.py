Buyingcost=int(input("How much did you buy it for="))
Sellingcost=int(input("How much did you sell it for="))
if Sellingcost>Buyingcost:
    Cost=Sellingcost-Buyingcost
    print(f"Profit={Cost}")
else:
    Cost2=Buyingcost-Sellingcost
    print(f"Loss={Cost2}")
    

