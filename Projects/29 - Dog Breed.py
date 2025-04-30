class Dog:
    def __init__(self, breed, color, size ,attitude):
        self.breed = breed
        self.color = color
        self.size = size
        self.attitude  = attitude
    def show_details(self):
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")
        print(f"Attitude: {self.attitude}")
        print("-" * 30)
dog1 = Dog("Pomeranian", "White", "Small" , "Loyal , Playful")
dog2 = Dog("Golden Retriever", "Golden", "Large" , "Friendly")

dog1.show_details()
dog2.show_details()