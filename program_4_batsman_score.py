n=[1,2,0,0,4,1,6,2,1,3]         #assuming input as n

b1=0                            #assuming b1==0
b2=0                            #assuming b2==0


for i in range (len(n)):        # i in range of n length ie.0 to 9
    for j in range (1,6):       # for over
        
        if i==0 or i==9:        # if i ==0,9 means do something
            b1=b1+n[i]          # true means b1=b1+n[i] ie. b1=0+1;b1=0+3
            #print("b1",b1)     #print b1
            break               #break the statement
        
        else:                   #if case false means do something 
            b2=b2+n[i]          #b2=b2+n[i] ie. b2=0+2;b2=0+4....
            #print("b2",b2)     #print b2
            break               #break the statement
                                #out of loop total answer of b1 and b2 will be shown 
                                
        
total=b1+b2                     #total=b1+b2 ie.total=4+16
print ("Total:",total)          #print total

print("batsman 1 score:" ,b1 )  #print score of batsman 1
print(n[0],'+',n[9])            #print run got by batsman 1

print("Batsman 2 Score:" , b2)  #print score of batsman 2
print(n[1],'+',n[2],'+',n[3],'+',n[4],'+',n[5],'+',n[6],'+',n[7],'+',n[8])
                                #print run got by batsman 2
