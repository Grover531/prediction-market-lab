class Market:

    def __init__(self, id, title, price, volume):
        self.id = id
        self.title = title
        self.price = price
        self.volume = volume

    def __str__(self):
        return f"{self.title} ({self.price})"
