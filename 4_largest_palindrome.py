# ******************************************************************************
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# ******************************************************************************

def isPal(num):
	for x in range(0,(len(num))/2):
		# print num[x] + " compared to " + num[len(num)-1-x]
		if num[x] != num[len(num)-1-x]:
			return False
	return True

if __name__ == "__main__":

    # Generate all possible products
    dict = {}
    for num1 in range(999,99,-1):
        for num2 in range(999,99,-1):
            dict[num1*num2] = str(num1) + " " + str(num2)

    # Sort products (keys of dict)
    keys = dict.keys()
    keys.sort(reverse=True)

    # Iterate keys until palindrome is found
    for key in keys:
    	if isPal(str(key)):
    		print key
    		break
