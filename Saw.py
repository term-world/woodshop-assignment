from inventory.Item import FixtureSpec
from Lumber import Lumber

class Saw(FixtureSpec):

    # TODO: Add multi-line and regular comments to this file
    #       to explain the functionality of each of the methods

    def __init__(self, cut_size: int = 2):
        self.cut_size = cut_size

    def cut(self, lumber: Lumber = Lumber()) -> [Lumber]:
        pieces = []
        while len(pieces) < self.cut_size:
            piece = Lumber(lumber.length / self.cut_size)
            pieces.append(piece)
        return pieces
    
    def use(self, lumber: Lumber = Lumber()) -> [Lumber]:
        return self.cut(lumber)