for i in range(1,10):
    if i%3==0 and i%5==0:
        continue  # When it satisfies i%3==0 it does not print(i), it goes to the first line. Continue statement skips the further statements.
    print(i)


print("Bye")

print("-----------------------------------")

for x in range(5):
    if x==3:
        continue
    print("Hello",x)