"""My solution to codewars problem 'Moving zeros to the end'"""

# O(n) time complexity, needs to be optimized

def move_zeros(array):
	zeros = []
	array2 = []
	for i in array:
		if i is 0:
			zeros.append(0)
		elif i == 0.0 and i is not False:
			zeros.append(0)
		else:
			array2.append(i)
	array2.extend(zeros)
	return array2




move_zeros([1,2,0,1,0,1,0,3,0,1])
move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
