
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while (i <= days):
        print(f"Day {i}")
        if (i == 5):
            print("Harvest time!")
        i += 1
