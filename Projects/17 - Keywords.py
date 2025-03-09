print('ONLY USE THIS CODE IF YOU LIVE IN THE UK!')
billAmount = int(input('Enter how much do you have to pay £'))
paidAmount = int(input('Enter how much you have paid already £'))
if billAmount and paidAmount < 0:
    print('You have to enter a positive number not negetive.')
else:
    if paidAmount >=billAmount :
        change= paidAmount - billAmount
        print('You have paid the whole amount.You will recieve a change of £ ' , change)
    else: 
        billAmount > paidAmount
        a = billAmount - paidAmount
        print('You have to pay £',a)


