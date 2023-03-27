from inventory.Item import FixtureSpec
from Lumber import Lumber

class Saw(FixtureSpec):

    def __init__(self, cut_size: int = 2):
        # Sets the size of the cut (i.e. how many boards to produce)
        self.cut_size = cut_size

    def cut(self, lumber: Lumber = Lumber()) -> [Lumber]:
        # Stores pieces cut in a convenient list
        pieces = []
        while len(pieces) < self.cut_size:
            piece = Lumber(lumber.length / self.cut_size)
            pieces.append(piece)
        return pieces
    
    def use(self, lumber: Lumber = Lumber()) -> [Lumber]:
        # Uses the self.cut method -- makes proper term-world object
        return self.cut(lumber)