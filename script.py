# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# update damages function:
def convert_damages_data(damages):

  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
#print(updated_damages)

# dictionary hurricanes:
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes = {}
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# converted dictionary of hurricanes:
def years_hurricanes_dictionary(years):
  years_hurricanes = []
  for names in hurricanes:
    if hurricanes[names]['Year'] == years:
      years_hurricanes.append(hurricanes[names])
    return years_hurricanes 

print(years_hurricanes_dictionary(2017))    
print(years_hurricanes_dictionary(1955)) 

# function that counts how often each area is listed as an affected area of a hurricane:
def area_count(areas_affected):
  affected_area_hurricanes = {}

  for area in areas_affected:
    for areas in area:
      if affected_area_hurricanes.get(area):
        affected_area_hurricanes[area] += 1
        continue
      affected_area_hurricanes[area] = 1 
    return affected_area_hurricanes
#print(area_count('Florida'))

# function that finds the area affected by the most hurricanes:
def most_affected_area_h(affected_area_hurricanes):
    max_area_hurricanes = 0
    name_area = ""
    dictio_affected_most = {}

    for i, value in affected_area_hurricanes.items():
      if value > max_area_hurricanes:
       max_area_hurricanes = value
       name_area = i
    
       dictio_affected_most[name_area] = max_area_hurricanes
       return dictio_affected_most


# hurricane that caused the greatest deaths:
zip_hurricanes_deaths = zip(hurricanes, deaths)
print(list(zip_hurricanes_deaths))
max_deaths = 0
hurricane_name = ""

def greatest_deaths(zip_hurricanes_deaths):
  for key, value in zip_hurricanes_deaths.items():
    if value["Deaths"] > max_deaths:
      max_deaths = value["Deaths"]
      hurricane_name = key
  return print(f"The Hurricane that caused the most deaths was {hurricane_name} with {max_deaths}") 

# Write a function that rates hurricanes on a mortality scale:
def mortality_S (zip_hurricanes_deaths):
    mortality_scale = {}

  for key, value in zip_hurricanes_deaths.items():
    if value["Deaths"] <= 0:
      if "0" in mortality_scale:
        mortality_scale[0].append(value)
      else:
        mortality_scale["0"] = [value]

    elif value["Deaths"] > 0 and value["Deaths"] <= 100: 
      if "1" in mortality_scale:
        mortality_scale["1"].append(value)
      else:
        mortality_scale["1"] = [value]

    elif value["Deaths"] > 100 and value["Deaths"] <= 500:
      if "2" in mortality_scale:
        mortality_scale["2"].append(value)
      else:
        mortality_scale["2"] = [value]

    elif value["Deaths"] > 500 and value["Deaths"] <= 1000:
      if "3" in mortality_scale:
        mortality_scale["3"].append(value)
      else:
        mortality_scale["3"] = [value]

    elif value["Deaths"] > 1000 and value["Deaths"] <= 10000:
      if "4" in mortality_scale:
        mortality_scale["4"].append(value)
      else:
        mortality_scale["4"] = [value]
    
    elif:
      if "5" in mortality_scale:
        mortality_scale["5"].append(value)
      else:
        mortality_scale["5"] = [value]
  
  return mortality_scale
print(mortality_S(zip_hurricanes_deaths)["3"])

# A function that finds the hurricane that caused the greatest damage, and how costly it was:
zip_hurricanes_damages = zip(hurricanes, updated_damages)
print(list(zip_hurricanes_damages))

def greatest_damage(zip_hurricanes_damages):
    damage_max = 0
    name_damage_max = ""

  for key,value in zip_hurricanes_damages.items():
     if value["Damages"] == "Damages not recorded":
      continue
     elif value["Damages"] > damage_max:
       damage_max = value["Damages"]
       name_damage_max = key

hurricane_greatest_damage = {name_damage_max:damage_max}
return hurricane_greatest_damage

print(greatest_damage(zip_hurricanes_damages))

# hurricane rating (according to how much damage they cause):
def hurricane_rating_damage(zip_hurricanes_damages):
  dictio_rating_damages_hurricanes = {}

  for key, value in zip_hurricanes_damages.items():
    if value["Damages"] == "Damages not recorded":
      continue

    elif value["Damages"] <= 0:
      if "0" in damage_scale:
        damage_scale["0"].append(value)
      else:
        damage_scale["0"] = [value]  

    elif value["Damages"] > 0 and value["Damages"] <= 100000000:
      if "1" in damage_scale:
        damage_scale["1"].append(value)
      else:
        damage_scale["1"] = [value] 

    elif value["Damages"] > 100000000 and value ["Damages"] <= 1000000000:
      if "2" in damage_scale:
        damage_scale["2"].append(value)
      else:
        damage_scale["2"] = [value]

    elif value["Damages"] > 1000000000 and value["Damages"] <= 10000000000:
      if "3" in damage_scale:
        damage_scale["3"].append(value)
      else:
        damage_scale["3"] = [value]

    elif value["Damages"] 10000000000 and value["Damages"] <= 50000000000:
      if "4" in damage_scale:
        damage_scale["4"].append(value)
      else:
        damage_scale["4"] = [value] 

     else:
       if"5" in damage_scale:
        damage_scale["5"].append(value)
      else:
        damage_scale["5"] = [value]
  return damage_scale 
          
        





      




  
    
    
  




                   
