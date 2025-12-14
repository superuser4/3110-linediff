chores = []


def add_chore(chore):
    chores.append(chore)
    print("Added chore:", chore)


def remove_chore(chore):
    if chore in chores:
        chores.remove(chore)
        print("Removed chore:", chore)


def show_chore():
    print("Current chores:")
    for c in chores:
        print("-", c)


add_chore("Wash Dishes")
add_chore("Vacuum")
add_chore("Clean room")

show_chore()
remove_chore("Vacuum")
show_chore()
