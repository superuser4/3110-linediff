chores = []


def add_chore(chore):
    if chore not in chores:
        chores.append(chore)


def remove_chore(chore):
    try:
        chores.remove(chore)
    except ValueError:
        print("chore not found:", chore)


def show_chores():
    if not chores:
        print("No chores available")
        return

    print("chores:")
    for i, c in enumerate(chores, 1):
        print(i, c)


add_chore("Wash Dishes")
add_chore("Vacuum")
add_chore("Vacuum")
add_chore("Clean room")

remove_chore("Vacuum")
show_chores()
