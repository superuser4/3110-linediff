schedule = []


def add_event(name, day):
    schedule.append((day, name))


def remove_event(name):
    for event in schedule:
        if event[1] == name:
            schedule.remove(event)
            return


def list_events():
    print("Schedule:")
    for day, name in schedule:
        print(day, "-", name)


add_event("Meeting", "Monday")
add_event("Gym", "Tuesday")
add_event("Doctor", "Friday")




remove_event("Gym")
list_events()
