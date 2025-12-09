
def ft_water_reminder():
    days_wihtout_water = int(input("Days since last watering: "))
    if (days_wihtout_water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
