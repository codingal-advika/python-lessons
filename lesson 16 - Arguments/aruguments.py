def total_cal(bill_amount , tipperc) :
    total = bill_amount*(1 + 0.01*tipperc)
    total =round(total , 2)
    print('Please pay £ ' , total)
b = int(input('Enter the bill amount : '))
t = int(input('Enter the tip percentage :'))
total_cal(b , t )