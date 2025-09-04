import array as arr
arraynum=arr.array('i',[1,3,5,3,7,9,3])
print("Original Array:"+str(arraynum))
print('Number of occurances of the number 3 in the array:'+str(arraynum.count(3)))
arraynum.reverse()
print('Reverse order:'+str(arraynum))