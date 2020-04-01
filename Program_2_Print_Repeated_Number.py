a=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]

d={x:a.count(x) for x in a}     #d=1:a.count(x)
                                #d=4
print (d)                       #1:4,2:2......

c=[]                            #c=array list

for num in a:                   #a in num ==> value in a stored in num
    if num not in c:            #c not in num means add num to c
       c.append(num)            #c.append(num) 
print (c)                       #c==>1,2,3,5,8,4,7,9,12,6,0


for j in c:                     #store c in j
    for x in a:                 #store a in x
        b=int(a.count(x))       #b==>count of x times ie.4,2,1,3,.......
        if(j==x):               #j==x
            print (j,'-',b)     #print ==> 1-4 2-2 3-1......
            break               #break you to stop the repeatation of the element
