num = int(input("ENter number : "))
string = str(num)
length = len(string)
sum = 0
for x in string:
    sum += int(x)**length
if ( sum == num ):
    print(num,"is a armstrong number.")
else:
    print(num,"is not a armstrong number.")