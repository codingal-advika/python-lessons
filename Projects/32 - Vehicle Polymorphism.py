class BMW():
    def colour(self):
        print('The colour of a BMW is black')
    def tyrepattern(self):
        print('The tyre pattern is a ribbon pattern')
    def model(self):
        print('The latest car model of a BMW is the BMW M5 Touring Plug-in Hybrid.')

print("-" * 30)

class Ferrari():
    def colour(self):
        print('The colour of the Ferrari is red')
    def tyrepattern(self):
        print('The tyre pattern is asymmetric tread')
    def model(self):
        print('The latest car model of a Ferrar is the 296 Speciale')

ob_BMW = BMW()
ob_Ferrari = Ferrari()
for features in (ob_BMW , ob_Ferrari):
    features.colour()
    features.tyrepattern()
    features.model()
    print("-" * 30)

