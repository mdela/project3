import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# get input from driver
mpg = int(input("Enter car's MPG: "))
priceGal = float(input("Enter current price per gallon: "))

# these cities, for me, are the worst to drive through
# because of this, I'll be charging a fee to every passenger who's getting dropped off here
cities = ['Koreatown', 'Los Angeles', 'Glendale', 'Hollywood', 'Santa Monica']

# create a dataframe to hold each row as a passenger with these fields:
df = pd.DataFrame({'name': pd.Series(dtype='str'),
                'distance': pd.Series(dtype='int'),
                'city': pd.Series(dtype='str'),
                'cost': pd.Series(dtype='int'),
                })

# add passengers
while True:
    addPass = str(input("Add new passenger? y/n : "))
    if addPass == 'n':
        break
    elif addPass != 'y':
        print("invalid entry")
        continue

    # get the fields
    name = str(input("Enter passenger name: "))
    distance = int(input("Enter passenger's distance to home: "))
    city = str(input("Enter drop-off city: "))

    # inconvenience fee for dropping off the passenger at one of California's major cities
    if city.title() in cities:
        inconvenienceFee = 3
        cost = (int((2*(round((distance / (mpg / priceGal)))) + inconvenienceFee)))
    else:
        cost = (int((2*(round((distance / (mpg / priceGal)))))))

    # append a customer as a row to the frame
    df = df.append({'name': name,
                    'distance': distance,
                    'city': city,
                    'cost':cost,},
                    ignore_index = True,)
        
# then, set up the plot
fig = px.bar(df, x='name', y='distance', color='cost', 
                    labels = {
                        'name': 'passenger',
                        'distance' : 'distance (mi)',
                        'cost' : 'cost ($)',
                    })
# titled the graph, and set it in ascending order
fig.update_layout(title_text = 'Cost to Drop off Each Passenger',
                    xaxis = {'categoryorder':'total ascending'})

# make the bars prettier
fig.update_traces(marker_line_color='black', marker_line_width=1.5,)

# then, plot
fig.show()

# extract the dataframe onto a CSV file
df.to_csv('passengers.csv', index=False)