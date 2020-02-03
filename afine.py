text='write your plain text, if you want to stop print "stop"'
m=[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
while True:
    text=input("your text: ")
    if text=='stop':
        break
    n=1
    while n==1:
        try:
            print("the first key: ", end='')
            k1=int(input())
            print("the second key: ", end='')
            k2=int(input())
            if k1>=0 and k2>=0 and k2<26 and k1 in m:
                n=False
            else:
                print("That's not a valid int!")
        except ValueError:
            print("That's not an int!")

    text= list(text)
    cipher=[]
    for i in text:
        if i.isupper():
            cipher.append(chr(((ord(i)-65)*k1+k2)%26+65))
        elif i.islower():
            cipher.append(chr(((ord(i)-97)*k1+k2)%26+97))
        else:
            cipher.append(i)
    print(''.join(cipher))
