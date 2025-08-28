mydata={'name':'Swanith','age':12,'grade':7,'city':'Bengaluru','contact number':9902071319}
print(mydata)
print(mydata['grade'])
mydata['gender']='male'
print(mydata)
print(mydata.pop('grade'))
print(mydata)
print(mydata.popitem())
print(mydata)
print(len(mydata))
print(mydata.clear())
print(mydata)
newdictionary={1:1,2:4,3:9,4:16,5:25,3:9,2:4}
print(newdictionary)
countrycode={'India':'0091','Australia':'0025','Bhutan':'0064','Brazil':'0076','Canada':'0124','Fiji':'0242'}
print('Countrycode of India')
print(countrycode.get('India','not found'))
print('Countrycode for Finland')
print(countrycode.get('Finland','not found'))
print('Countrycode for Brazil')
print(countrycode.get('Brazil','not found'))
