s1={2,3,1}
s2={'d','a','c'}
s3=list(zip(s1,s2))
print(s3)
stock=['reliance','infosis','TCS']
price=[2175,1175,2170]
newdictionary={stock:price for  stock,price in zip(stock,price)}
print(newdictionary)