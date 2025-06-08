l=[2,5,10]
while True:
    c=int(input("""
       1.push elements
       2.pop elements
       3.peek elements
       4.display elements
       5.exit
       
       """))
    if c==1:
        n=input("enter the value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empety")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty")
        else:
            print(l[-1])
    elif c==4:
        print("display stake",l)
    elif c==5:
        break;

