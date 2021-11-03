def is_on_list(days: list, day: str) -> bool:
  if day in days:
    return True
  else:
    return False

def get_x(days: list, i: int) -> str:
  return days[i]

def add_x(days: list, day: str) -> None:
  days.append(day)

def remove_x(days: list, day: str) -> None:
  days.remove(day)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #