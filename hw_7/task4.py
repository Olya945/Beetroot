week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_dict = {i: day for i, day in enumerate(week, 1)}
print(week_dict)

reversed_week_dict = {day: i for i, day in week_dict.items()}
print(reversed_week_dict)

