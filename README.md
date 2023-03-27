
| Date              |          |
|:------------------|:---------|
| Todo | Assigned |
| Todo | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# WORTHY WOODSMITHS WILL WIN OUT: MAYOR MANDATES COTTAGE INDUSTRY

**Reported by `Official Mayor-Endorsed News` on `Todo`**

How many tables could a woodsmith smith if a woodsmith could smith tables? What about tables? Bookshelves? Citizens of `term-world` are about to find out. The Office of the Mayor announced--effective today--that all denizes of the great digital community should gear up to, as the Mayor yelled with increasing intensity, "make....Make....MAKE! For me, of course, your Mayor."

While recent weeks have seen some unrest among the ungrateful residents of various neighborhoods--namely about NECESSARY mayoral data collection efforts--the Office of the Mayor hopes that industrious mandates to innovate might distract everyone enough that they forget about it. Which, you should. As the Mayor noted in a press conference held only for the benefit of O.M.E.N.: "[they] _should_."

So start up those saw blades, prepare to sell a majority stake in your soul, and learn some lumber skills; `term-world`, the Mayor noted, is about to "get all L.L. Bean up in here."

## Overview

In this activity, you'll:

* discover how to import custom modules and use them as `object`s
* continue to create `class`es and `object`s to achieve purpose-built tasks
* observe strange, but productive, `object` behaviors

To achieve this, we need to:

* use our `main.py` function to coordinate the creation of:
  * `Lumber`
  * various `object`s such as `Chair`s, `Table`s, and `Bookshelf`s
* leverage `module`s built to modify, change, and interact with others by
  * using the `Saw` and
  * `Woodpile`
* `import` necessary `module`s into `main` and use their "powers" (`method`s)

The more quantitative steps:

* create and cut `Lumber` enough to create `55` board feet (bf) to:
  * use `25` for a `Table`
  * use `20` for a `Bookshelf`
  * use `10` for a `Chair`
* add cut `Lumber` to the `Woodpile`
* pull from the `Woodpile` to build the items list above

If all of this is done correctly, you should see a `Chair.py`, `Table.py` and `Bookshelf.py` in your `products` directory.

### Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the Readme might be taken out.

## Completing `woodshop` content

For this activity, you'll need to complete the following steps for all of your `woodshop` items, creating a (somewhat) autonomous factory.

For `Saw.py`, `BookshelfPlans.py`, `ChairPlans.py`, and `TablePlans.py`, you do not need to do anything. For convenience, though:

|Plan |Required `Lumber` |
|:----|:-----------------|
|Chair| 10|
|Table| 25|
|Bookshelf| 20|
|**Total**    |**55** |

### Plans

You do not need to read the code for each plan unless interested. _However_, you should know that each has the following profile:

* they take `1` argument/parameter: a `list` of pieces from the `WoodPile`

If there's enough `Lumber` in the `WoodPile` to build an item, it builds in the `products` directory.

### `Saw.py`

However, you _do_ need to understand how `Saw.py` works. Take a moment to review the file and make comments in it (these are part of the grader).

|`method`|Parameters|Description|`return`|
|:-------|:---------|:------|:-----------|
|`__init__`|`cut_size` (`int`)|Number of pieces to cut from a `Lumber`|`None`|
|`cut`|`lumber` (`Lumber`)|`Lumber` object to cut into pieces|`list`|

### `Lumber.py`

To make anything out of wood, we need `Lumber`. Thankfully, now we can make some. In `term-world`, `Lumber` is very simple to create. All it takes is:

* a `constructor` which takes `1` _explicit_ parameter for the length of the board to create
* sets the parameter as the `length` of the individual `object` board
  * this one is only a _bit_ tricky; think of what `Lumber` knows about itself

|`method`|Parameters|Description|`return`|
|:-------|:---------|:------|:-----------|
|`__init__`|`length` (`int`)|Sets the `length` property of a given board|`None`|

### Woodpile.py

Once we've cut some `Lumber`, we need a place to store it. This is where our `WoodPile` comes in. The requirements here are a bit different:

* a `constructor` (no parameters) which makes an empty `list` called `pieces` which we'll add stuff to once we've cut wood
* a `method` (i.e. `function`) called `add` which:
  * keeps in mind that there's a `list` called `pieces`
  * takes `1` _explicit_ parameter which is a `list` of chopped pieces of wood
  * adds these to `pieces`

One clever thing to note about what `list`s do here--let's look at an example:

```python
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

# Use the increment assignment operator
numbers += new_numbers

# What happens?
print(numbers)
```

Another issue to remind yourself of: `pieces` contains a `list` of `Lumber`-type `objects`. How does that change how we handle it?

|`method`|Parameters|Description|`return`|
|:-------|:---------|:------|:-----------|
|`__init__`|`None`|Creates an empty `list` called `pieces` to add to over time |`None`|
|`add`|`lumber` (`list`)|`Lumber` objects to cut into pieces|`None`|

### `main.py`

This is the coordinating center of all of our work. Here, we use the `Woodpile`, `Saw`, various `Plan`s and `Lumber` to make our objects. We need as much `Lumber` board-feed (bf) as all `3` objects require. Here, we use all the various `method`s 

This means, we must `import`:

* `Woodpile`
* `Saw`
* `Lumber`
* `Bookshelf`
* `Chair`
* `Table`

### `reflection.md`

Don't forget to finish the `reflection.md` file in the `clean-up` folder!

## Improvement suggestions

Here are some suggestions for improvements you can, **but are not limited to** use:

|Improvement Suggestions |Description        |
|:-----------------------|:------------------|
|Methods                 |Make a given furniture product useful (i.e. give it functionality) |
|Methods                 |Make the saw more efficient by adding blades |
|Objects                 |Make and build a new product plan in the `plans` folder |
|Objects                 |Make a new cuttable material (i.e. stone?)†   |
|Objects/Methods         |Completely automate the manufacturing process†† |
|Conditional statments   |Give user a choice of which product(s) they would like to make (i.e. a menu)††† |
|Iteration/Data structures|Display number of boards made and total length of each as part of manufacturing process |
|Objects/Iteration/Data structures | If deficient some amount of board feet, report how many and which products build or fail |
|Objects                 |Add functionality to the woodpile to print how much wood has been added |


`†` If possible, also make a way to, for example, _quarry_ stone?

`††` Here, you shouldn't need to know how many board feet are required; the plans _tell_ you

`†††` The menu must also _work_ (i.e. if an object is chosen, the factory should go to work)

**Make sure to link your issue with the pull request you used to make your actually improvement.**

**If you are not following an improvement suggestion you need to have your improvement suggestion checked by the professor before proceeding.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
