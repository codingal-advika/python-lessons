class computer:
    def __init__(self):
        self.maxprice = 356

    def sell(self):
        print('The price it was sold 1 year ago:{}'.format(self.maxprice))
    
    def MaxPrice(self  , price):
        self.Maxprice = price
com = computer
com.sell
com._MaxPrice = 600
com.sell
com.set_MaxPrice(600)
com.sell