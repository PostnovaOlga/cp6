try:
	print("How_many_elements?")
	a=int(input())
	array = [0]*a
	for i in range(len(array)):
	    i = str(i + 1)
	    print("Element " + i, end = " ")
	    i = int(i)
	    i = i - 1
	    array[i] = int(input())
	print("Delta:")
	delta = int(input())
	smallest = array[0] if array else None
	for i in array:
		if i < smallest:
			smallest = i
	x = delta + smallest
	t = 0
	for i in array:
		if i == x:
			t = t+1
	print ("Result: ", t)		
except ValueError :
	print("Incorrect_data")