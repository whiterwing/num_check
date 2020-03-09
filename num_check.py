
class num_check:
	def check_prime(number):
	    test_num=round(number/2)
	    factor=1
	    
	    while factor<3 and test_num:
	        if number%test_num==0:
	            factor+=1
	        test_num-=1
	        
	    if factor<3 and number!=1:
	        print (number, "is a prime.")
	    else:
	        print (number, "is not a prime.")

	def check_happy(number):
	    not_happy=True
	    tested_nums=[]
	    test=number
	    
	    while not_happy:
	        test_num=0
	        
	        for num in str(test):
	            test_num+=int(num)**2
	        test=test_num
	        
	        if test_num ==1:
	            not_happy=False
	        elif test_num in tested_nums:
	            break
	        
	        tested_nums.append(test_num)
	        
	    if not_happy == False:
	        print(number, " is happy.")
	    else:
	        print(number, "is not happy.")
	            
	def check_narcissistic(number):
	    test=0
	    
	    for num in str(number):
	        test+=int(num)**len(str(number))
	        
	    if test == number:
	        print (number, "is narcissistic.")
	    else:
	        print(number, "is not narcissistic.")

if __name__ == "__main__":
	number = int(input("What number do you want to test?"))

	num_check.check_prime(number)
	num_check.check_happy(number)
	num_check.check_narcissistic(number)