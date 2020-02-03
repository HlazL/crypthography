text='write your plain text, if you want to stop print "stop"'
while True:
    text=input("your text: ")
    if text=='stop':
        break
    n=1
    while n==1:
        try:
            print("the key: ", end='')
            k=int(input())
            if k>=0:
                n=False
            else:
                print("That's not a positive int!")
        except ValueError:
            print("That's not an int!")

    text= list(text)
    cipher=[]
    for i in text:
        if i.isupper():
            cipher.append(chr((ord(i)+k-65)%26+65))
        elif i.islower():
            cipher.append(chr((ord(i)+k-97)%26+97))
        else:
            cipher.append(i)
    print(''.join(cipher))
