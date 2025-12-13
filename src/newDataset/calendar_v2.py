schedule = {}


def add_event(name, day):
    if day not in schedule:
        schedule[day] = []
    schedule[day].append(name)


def remove_event(name):
    for day in schedule:
        if name in schedule[day]:
            schedule[day].remove(name)
            if not schedule[day]:
                del schedule[day]
            return


def list_events():
    if not schedule:
        print("No events scheduled")
        return

    print("Weekly schedule:")
    for day in sorted(schedule):
        for event in schedule[day]:
            print(day, "-", event)


add_event("Meeting", "Monday")
add_event("Gym", "Tuesday")
add_event("Doctor", "Friday")

remove_event("Gym")
list_events()
