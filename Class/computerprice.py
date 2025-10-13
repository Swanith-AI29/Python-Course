class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('Selling price: {}'.format(self.__maxprice))
    def sellmaxprice(self,price):
        self.__maxprice=price

dell=computer()
dell.sell()
dell.__maxprice=1000
dell.sell()
dell.sellmaxprice(1000)
dell.sell()
