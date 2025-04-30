class India():
    def capital(self):
        print('New Dehli is the capital of India')#
    def language(self):
        print('The most common language spoken in India is Hindi')
    def type(self):
        print('India is a Constitutional republic type of country')

print("-" * 50)

class USA():
    def capital(self):
        print('Washington D.C is the capital of USA(Uited States of America)')
    def language(self):
        print('The most common laguage spoken in the USA is English')
    def type(self):
        print('The USA is a Federal republic country')

ob_Ind = India()
ob_USA = USA()
for country in (ob_Ind, ob_USA):
    country.capital()
    country.language()
    country.type()
    print("-" * 50)