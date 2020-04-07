#Program to find the odd and even numbers inside a list

def FindingOddAndEvenNumber(lst):

    even=0
    odd=0
    for i in lst:
        if i%2==0:
            print("{} is even".format(i))
            even=even+1
        else:
            print("{} is odd".format(i))
            odd=odd+1
    return even,odd

lst=[10,11,12,13,14,15,16,17,18,19,20]

even,odd=FindingOddAndEvenNumber(lst)

#print(even)
#print(odd)

print("Even : {} and Odd : {}".format(even,odd))  #format() is a function of string