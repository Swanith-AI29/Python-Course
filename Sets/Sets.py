set={1,2,3,4,5,3,4,2,7,1,1}
print(set)
set1={'green','blue','pink'}
set2={'blue','yellow','green'}
print('Original set elements')
print(set1,set2)
newset=set1.intersection(set2)
print(newset)
newset1=set1.union(set2)
print(newset1)
newset2=set1.difference(set2)
print(newset2)
newset3=set2.difference(set1)
print(newset3)