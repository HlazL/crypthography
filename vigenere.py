text='write your plain text, if you want to stop print "stop"'
while True:
    text=input("your text: ")
    if text =='stop':
        break
    k = input(("the key: "))
    while k.isalpha() == False:
        print("Not a string")
        k = input(("the key: "))

    kod=[]
    text= list(text)
    cipher=[]
    for i in k:
        if i.isupper():
            kod.append((ord(i)-65))
        elif i.islower():
            kod.append((ord(i)-97))
    j=0
    for i in range(len(text)):
        if text[i].isupper():
            cipher.append(chr((ord(text[i])+kod[j%len(kod)]-65)%26+65))
        elif text[i].islower():
            cipher.append(chr((ord(text[i])+kod[j%len(kod)]-97)%26+97))
        else:
            cipher.append(text[i])
            j-=1
        j+=1
    print(''.join(cipher))
