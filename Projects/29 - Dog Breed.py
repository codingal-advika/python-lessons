class Dog:
    def __init__(self, breed, color, size ,):
        self.breed = breed
        self.color = color
        self.size = size
    def show_details(self):
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")
        print("-" * 30)
dog1 = Dog("Pomeranian", "White", "Small")
dog2 = Dog("Golden Retriever", "Golden", "Large")

dog1.show_details()
dog2.show_details()