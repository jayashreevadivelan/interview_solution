#Print n Number
#Print Multiple of Three means Fizz
#Print Multiple of Five means Buzz
#Print Multiple of Both means FizzBuzz

n=int(input("Please enter the number:")) #n=15

for i in range (1,n+1):     #i == 1 to 16
    if(i%5==0)&(i%3==0):    #if(15%5==0) and (15%3==0)
        print("FizzBuzz")   #print==>"FizzBuzz"

    elif(i%3==0):           #if(9%3==0)
        print("Fizz")       #print==>"Fizz"
    elif(i%5==0):           #if(10%5==0)
        print("Buzz")       #print==>"Buzz"
    
    else:
        print(i)            #print==>1,2,4....

