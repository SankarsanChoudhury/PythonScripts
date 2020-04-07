#In this program although we enter 2 as numerator & 4 is denominator it converts the bigger value as numerator & smaller as denominator
def div(a,b):
    if a<b:
        a,b=b,a
    print(a/b)

div(2,4)
div(6,4)

#===Using decorator you can use extra feature in existing function================
def div1(a1,b1):
    print(a1/b1)

def smart_div(func):
    def inner(a1,b1):
        if a1<b1:
            a1,b1=b1,a1
        return func(a1,b1)
    return inner

div2=smart_div(div1)
div2(2,4)