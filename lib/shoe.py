class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize _size to None
        self.size = size  # Use the setter method to validate
        self.condition = "New"  # Default condition is "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def __str__(self):
        return f"{self.brand} shoe in size {self.size}"
