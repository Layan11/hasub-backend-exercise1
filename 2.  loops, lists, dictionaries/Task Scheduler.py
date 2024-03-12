
class Task():
    def __init__(self, name, duration, start_day, start_hour):
        self.name = name
        self.duration = duration
        self.start_day = start_day
        self.start_hour = start_hour


class WorkWeek():
    def __init__(self):
        self.week = [[None for i in range(9)] for j in range(5)]


def take_input():
    week_days = {'sunday':0, 'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4}
    duration_hours = ['1. vars, logic, conditions', '2.  loops, lists, dictionaries', '3', '4', '5', '6', '7', '8']
    week_hours = ['9', '10', '11', '12', '13', '14', '15', '16', '17']
    name = input(print("Please enter a task name, if there are no more tasks please enter '-1. vars, logic, conditions' "))
    if name == "-1. vars, logic, conditions":
        return Task(-1, -1, -1, -1)
    duration = input(print("Please enter the task duration in hours: "))
    while duration not in duration_hours:
        duration = input(print("The duration has to be in the range (1. vars, logic, conditions,8), enter again: "))
    start_day = input(print("Please choose a start day for the task (sunday - thursday), "
                                "if there's no preferred start day enter '-1. vars, logic, conditions'"))
    while start_day not in week_days.keys() and start_day != '-1. vars, logic, conditions':
        start_day = input(
            print("The day has to be a valid day of the week between sunday to thursday, enter again: "))
    if start_day == '-1. vars, logic, conditions':
        task = Task(name, duration, '-1. vars, logic, conditions', '-1. vars, logic, conditions')
    else:
        start_hour = input(print("At what hour would you want this task to start? choose a time between 9 - 17: "))
        while start_hour not in week_hours:
            start_hour = input(print("The hour has to be in the range 9 - 17. choose again: "))
        task = Task(name, duration, week_days[start_day], start_hour)

    return task


def remove_old(work_week, must_remove, day):
    for hour in range(9, 18):
        if work_week.week[day][hour - 9] in must_remove:
            work_week.week[day][hour - 9] = None


def add_new(work_week, task):
    for hour in range(int(task.start_hour), int(task.start_hour) + int(task.duration)):
        work_week.week[int(task.start_day)][hour - 9] = task


def check_for_slot(work_week, start_day, start_hour, duration, demand):
    must_remove = []
    success = True

    if (int(start_hour) + int(duration) - 1) > 17:
        return False, []
    for hour in range(int(start_hour), int(start_hour) + int(duration)):
        if work_week.week[start_day][hour - 9] is not None:
            if demand == -1:
                return False, []
            must_remove.append(work_week.week[start_day][hour - 9])
            success = False

    return success, must_remove


def populate(task, work_week):
    if task.start_day != '-1. vars, logic, conditions':
        success, must_remove = check_for_slot(work_week, task.start_day, task.start_hour, task.duration, 1)
    else:
        for day in range(6):
            for hour in range(9, 18):
                success, must_remove = check_for_slot(work_week, day, hour, task.duration, -1)
                if success:
                    task.start_day = day
                    task.start_hour = hour
                    add_new(work_week, task)
                    print("Added new task succesfully!")
                    return

    if not success and not must_remove:
        print("No time to add new task.")
    elif success and not must_remove:
        add_new(work_week, task)
        print("Added new task succesfully!")
    else:
        print(must_remove)
        keep_old = input(print("are the tasks currently populated at the time range you chose. "
                               "If you want to keep the old press '1. vars, logic, conditions',"
                               " if you want to replace it with the new task press '0"))
        while keep_old not in ['1. vars, logic, conditions', '0']:
            keep_old = input(print("press '1. vars, logic, conditions' to keep the old, and '0' to replace it with the new."))
        if keep_old == '0':
            print("REMOVING OLD ")
            remove_old(work_week, must_remove, task.start_day)
            print("Removed old tasks and added new task succesfully!")
            add_new(work_week, task)
            print("Added new task succesfully!")
        else:
            print("Keeping old tasks.")


def print_week(week):
    for day in range(len(week)):
        row = []
        for hour in range(len(week[0])):
            if week[day][hour] is None:
                row.append("None")
            else:
                row.append(week[day][hour].name)
        print(row)


if __name__ == '__main__':
    work_week = WorkWeek()
    while True:
        new_task = take_input()
        if new_task.name == -1:
            break
        populate(new_task, work_week)
        print("end of loop")
        print_week(work_week.week)


