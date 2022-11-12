import matplotlib.pyplot as plt

# get input from driver
mpg = int(input("Enter car's MPG: "))
currRange = int(input("Enter car's current range in miles: "))
maxRange = int(input("Enter car's max range in miles: "))
priceGal = float(input("Enter current price per gallon: "))

fares = []
passengers = {}
numPassengers = 0
# add passengers to the dict
while True:
    addPass = str(input("Add new passenger? y/n : "))
    if addPass == 'n':
        break
    elif addPass != 'y':
        print("invalid entry")
        continue

    name = str(input("Enter passenger name: "))
    distance = int(input("Enter passenger's distance to home:"))
    # add the passenger
    passengers[name] = distance
    fares.append(int(round((distance / (mpg / priceGal)))))
    numPassengers += 1

if passengers:

    # now, we'll make a bar graph
    # in this bar graph, the bars will be colored based on max or min distance

    # get the index of the passenger with the most distance
    maxDistPassenger = max(passengers, key=passengers.get)
    maxIndex = list(passengers).index(maxDistPassenger)

    # get the index of the passenger with the least distance
    minDistPassenger = min(passengers, key=passengers.get)
    minIndex = list(passengers).index(minDistPassenger)

    fig = plt.figure(figsize=(10, 5))
    
    # make a list of the colors that represent each passenger
    colors = []

    # we color the passenger based on the index of the max and min
    # if the current index is the max, color red
    # if it's the min, color green
    # if it's neither, color blue
    for i in range(numPassengers):
        if i == maxIndex: colors.append('maroon')
        elif i == minIndex: colors.append('green')
        else: colors.append('blue')


    

    # here, we start making the bar graph

    names = list(passengers.keys()) # names are x-axis
    distances = list(passengers.values()) # distances are y-axis

    for name, distance, fare in zip(names, distances, fares):
        price = (f"${fare}.00")
        plt.text(name, distance//2, price, ha = 'center',
        bbox = dict(facecolor = 'pink', alpha = 1,))

    plt.bar(names, distances, color=colors, width=0.4, edgecolor = 'black', linewidth = 3)
    plt.xlabel("passengers")
    plt.ylabel("miles")
    plt.title("distance to drop-off")
    plt.show()

else:
    print("No passengers")
