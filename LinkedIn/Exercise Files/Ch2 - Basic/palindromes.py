def is_palindrome(teststr):
    if teststr==teststr[::-1]:
        return True
    else:
        return False
run = True
while(run):
    teststr=input("Enter the string to check for palindrome or 'exit':")
    if teststr=='exit':
        run=False
        break

    teststr=teststr.lower()
    newstr=""
    for i in teststr:
        if i.isalnum():
            newstr+=i

    print("Palindrome:",is_palindrome(newstr))