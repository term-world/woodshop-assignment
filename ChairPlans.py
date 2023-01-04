from inventory.Item import FixtureSpec
from inventory.Item import Factory

"""
Note: You do not need to browse this file unless interested.
"""

class ChairPlans(FixtureSpec):

    def __init__(self, lumber: list = []):
        self.lumber = lumber
        self.required = 10
        self.built = False
        self.build()
        if self.built:
            self.make()
    
    def __str__(self) -> str:
        if self.built:
            return "It's a chair."
        return "It's not a chair yet."

    def build(self):
        sorted(
            self.lumber, 
            key = lambda piece: piece.length
        )
        if not self.check_pile():
            return
        while self.required > 0:
            smallest = self.lumber.pop()
            self.required -= smallest.length
        self.built = True
    
    def check_pile(self) -> bool:
        total = 0
        for piece in self.lumber:
            total += piece.length
        if total < self.required:
            return False
        return True

    def make(self):
        if self.built:
            Factory("Chair", "./products")
        fixes = [
            {"find": "ItemSpec", "replace": "FixtureSpec"},
            {"find": "consumable = True\n", "replace": ""},
            {"find": "  ", "replace": "    "},
            {"find": "    \n", "replace": ""},
            {"find": "__file__", "replace":""}
        ]
        with open("products/Chair.py", "r+") as fh:
            source = fh.read()
            for fix in fixes:
                source = source.replace(fix["find"], fix["replace"])
            fh.seek(0)
            fh.write(source)
            fh.truncate()