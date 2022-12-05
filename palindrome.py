string = input("Enter string : ")
rev = string[::-1]
if ( string == rev ):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")