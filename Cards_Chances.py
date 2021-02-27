def cards():
    Cards_Hist={}
    sum1=0
    Final={}
    counter=0
    Val_1=0
    Val_2=0
    for card1 in range(1,53):
        for card2 in range(1,53):
            if(card1!=card2):
                Val_2=(card2%13)*(card2%13!=0) + (card2%13==0)*(13)
                Val_1=(card1%13)*(card1%13!=0) + (card1%13==0)*(13)

                sum1= Val_1+Val_2
                Cards_Hist[sum1] = Cards_Hist.get(sum1,0)+1
                counter+=1
        Val_1=0
        Val_2=0
        sum1=0
    sum2=0
    for key in sorted(Cards_Hist.keys()):
        Final[key]=(Cards_Hist[key]/counter)
        print("Chance for: ",key, "is: " , Final[key], "  OR %.2f" %((Final[key])*100),"%")
        sum2+= Final[key]
    print("Sum of all chances = " ,sum2*100)
    #calc: x^2 - sum of two cards
    w=0
    for num in range(2,27):
       w += ((num**2) * Final[num])

    print("x^2 is: ",  w)

cards()
