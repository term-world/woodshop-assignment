
| Date              |          |
|:------------------|:---------|
| 7 November 2022 | Assigned |
| 13 November 2022 | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# WORTHY WOODSMITHS WILL WIN OUT: MAYOR MANDATES COTTAGE INDUSTRY

**Reported by `Official Mayor-Endorsed News` on `7 November 2022`**

How many tables could a woodsmith smith if a woodsmith could smith tables? What about tables? Bookshelves? Citizens of `term-world` are about to find out. The Office of the Mayor announced--effective today--that all denizes of the great digital community should gear up to, as the Mayor yelled with increasing intensity, "make....Make....MAKE! For me, of course, your Mayor."

While recent weeks have seen some unrest among the ungrateful residents of various neighborhoods--namely about NECESSARY mayoral data collection efforts--the Office of the Mayor hopes that industrious mandates to innovate might distract everyone enough that they forget about it. Which, you should. As the Mayor noted in a press conference held only for the benefit of O.M.E.N.: "[they] _should_."

So start up those saw blades and learn some lumber skills; `term-world`, the Mayor noted, is about to "get all L.L. Bean up in here."

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

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/cJAXqu65W2s/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlF99gvu4u3TIqBVk87xYirA)

## Accessing `woodpile` Content

In order to complete the workload for the `woodpile` you'll first need to `clone` the `woodpile` repository into your `workshop`.

When you `clone` a repository you're duplicating its contents and adding them to your local workspace. Since you'll be working collaboratively with your neighbors, you'll each need your own copy of the `woodpile` to work with.

In order to keep some of the magic (read: somewhat convoluted code) that makes `term-world` work the way it does, **you are required to clone all additional repositories within the `workshop`, located within your `garage`.**

Head to GitHub and:
* click on the green `Code` button
* ensure that `SSH` is selected
* copy the link that appears in the window below

It might look something like `git@github.com:term-world/woodpile-dluman`.

Once you've copied this link, navigate to your terminal window and ensure you're still in the appropriate place (in this case, the topmost level of your `workshop`). Then, enter the command:

```
git clone COPIED-LINK-HERE
```

Be sure to replace the fragment `COPIED-LINK-HERE` with the link you copied. In the example regarding `woodpile-dluman`, the full command would look like:

```
git clone git@github.com:term-world/woodshop-dluman
```

While `pull` is used to *update* the contents of a repository that already exists in your local workspace, `clone` is used to *replicate* the contents of a repository from GitHub and copy them to your local workspace.

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

### Finishing up

Two more items to finish up before we're done this week:

* choose at least _one_ of the `object`s in the `products` folder to add functionality to
  * this does not necessarily count as your _improvement_
* finish the `reflection.md` file in the `clean-up` folder

## Submitting `woodshop` Content

Considering that the work you're doing for the `woodshop` is individual, there's no need to branch your work. However, getting in the habit of doing so is a _good habit_.

When you're ready to push to GitHub, do the normal `add` and `commit` routines. Recall:

```
git add NAME_OF_FILE_OR_DIRECTORY_TO_ADD
```

You may need to do this for either:

* Individual files (i.e. `git add Thingamajig.py`)
* Directories (i.e. `git add Thingamajig`)

```
git commit -m "Descriptive commit message"
```

### Pushing to a branch

**_If you choose to work only on `main`, ignore this section, and `push` to `main` normally._**

But, if you're branching--when it comes to push, run this slightly expanded command:

```
git push origin YOUR_BRANCH_NAME
```

We're still using `git push`, but this time we're adding an extra layer of information to the command; to be precise, we're specifically instructing `git` to push our changes to a particular branch of the repository (*your* branch). In the example regarding the `gadgets` department, the command to run would look like:

```
git push origin gadgets
```