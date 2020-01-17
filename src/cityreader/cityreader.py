# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

class City:
  def __init__(self,name,lat,lon):
    self.name = name
    self.lat = float(lat)
    self.lon = float(lon)
  def __repr__(self):
    return f'{self.name} - lat:{self.lat}, lon:{self.lon}'
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('cities.csv', 'r') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
# hides header in cities.csv
      for line in reader:
        cities.append(City(line[0], line[3], line[4]))
    return cities
 
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  # normalize lats and lons
  if(lat2 < lat1):
    lat1,lat2 = lat2, lat1
  if(lon2 < lon1):
    lon1,lon2 = lon2, lon1

  within = [city for city in cities if city.lat >=
            lat1 and city.lat 
            <= lat2 and city.lon 
            >= lon1 and city.lon 
            <= lon2]

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

print("Search cities within a range, separate lats and lon with a comma")
first_input = input("Enter lat1, lon1:")
second_input = input("Enter lat2,lon2:")

lat1 = float(first_input.split(",")[0])
lon1 = float(first_input.split(",")[1])

lat2 = float(second_input.split(",")[0])
lon2 = float(second_input.split(",")[1])

for c in cityreader_stretch(lat1,lon1,lat2,lon2,cities):
  print("-------------------------------------------")
  print(f"{c.name},{c.lat},{c.lon}")

