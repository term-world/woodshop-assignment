from WoodPile import WoodPile as Pile
from Saw import Saw
from Lumber import Lumber

from plans.TablePlans import TablePlans as Table
from plans.ChairPlans import ChairPlans as Chair
from plans.BookshelfPlans import BookshelfPlans as Bookshelf

def main():
    saw = Saw()
    pile = Pile()

    total_needed = 55

    while total_needed > 0:
        
        board = Lumber()
        cut = saw.use(board)
        pile.add(cut)

        for piece in cut:
            total_needed -= piece.length

    chair = Chair(pile.pieces)
    print(chair)

    table = Table(pile.pieces)
    print(table)

    bookshelf = Bookshelf(pile.pieces)
    print(bookshelf)

if __name__ == "__main__":
    main()