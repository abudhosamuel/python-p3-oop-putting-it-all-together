class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize _page_count to None
        self.page_count = page_count  # Use the setter method to validate

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title} with {self.page_count} pages"
