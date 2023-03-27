from inventory.Item import ItemSpec

class Lumber(ItemSpec):

    def __init__(self, length: int = 4):
        self.length = length