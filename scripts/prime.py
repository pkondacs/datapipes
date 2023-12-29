
def generate_prime_factors(number):
    factors = []
    
    

    while True:
        try:
            #number = int(input("input an integer:  "))
            number
            
        
            break
        except ValueError:
            print("No valid integer! Please try again ...")
            return ValueError
    
    if number == 1:
        print("[ ]")
    elif number==2:
        factors.append(2)
        return factors
    elif number==3:
        factors.append(3)
        return factors

    else:
    
    
        while number % 2 == 0:
            factors.append(2)

            number //= 2
            
        divisor = 3
        while number != 1 and divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                # prime numbers are odd except 2
                divisor += 2
        print ("the prime factors are: ")
        return factors
        #for i in range(len(factors)):
            #return factors[i]
#generate_prime_factors()
'''
def prints():
    print(generate_prime_factors(1))
prints()'''