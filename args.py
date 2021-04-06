def vol(rad):
    pi = 3.14
    v = 4 / 3 * pi * rad ** 3
    print (v)

vol(1)

def ran_check(num, low, high):
    if num >= low:
        print ("Number is higher")
    elif num <= high:
        print("Number is lower")
    else:
        print("Number in between")

ran_check(5, 2, 7)

def ran_bool(num, low, high):
    if num >= low and num <= high:
        return True

   
if ran_bool(3,1,10) == True:
    print ('its true')

string = "Hello Mr. Rogers, how are you this fine Tuesday?"
newstring = ""
count1 = 0
count2 = 0

  
for x in string:  
  
    if (x.isupper()) == True:  
        count1+= 1
        newstring+=(x.lower())  

    elif (x.islower()) == True:  
        count2+= 1
        newstring+=(x.upper())  
 
print("In original String : ")  
print("Uppercase -", count1)  
print("Lowercase -", count2)  

