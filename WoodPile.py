from inventory.Item import FixtureSpec

class WoodPile(FixtureSpec):

    def __init__(self):
        self.pieces = []

    def add(self, lumber):
        self.pieces += lumber