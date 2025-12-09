
def ft_count_harvest_recursive(day: int = 1, max_days: int = 0):
    if max_days == 0:
        max_days = int(input("Days until harvest: "))
    print(f"Day {day}")
    if (day == max_days):
        print("Harvest time!")
        return
    ft_count_harvest_recursive(day + 1, max_days)
