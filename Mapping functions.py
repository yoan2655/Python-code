#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define a dictionary mapping each location to its corresponding city and district
city_mapping = {
    'tel-aviv': {'city': 'תל אביב', 'district': 'Tel Aviv'},
    'jafa': {'city': 'תל אביב', 'district': 'Tel Aviv'},
    'תל אביב': {'city': 'תל אביב', 'district': 'Tel Aviv'},
    'ת''א': {'city': 'תל אביב', 'district': 'Tel Aviv'},
    'רמת-גן': {'city': 'רמת גן', 'district': 'Tel Aviv'},
    'ר''ג': {'city': 'רמת גן', 'district': 'Tel Aviv'},
    '0סכנין': {'city': 'סכנין', 'district': 'Northern'},
    '00יפו': {'city': 'יפו', 'district': 'Tel Aviv'},
    'קניון איילון': {'city': 'תל אביב', 'district': 'Tel Aviv'},
    'באקע על-גרביה': {'city': 'באקע', 'district': 'Southern'}
    # Add more entries as needed
}

# Example usage:
locations = ['tel-aviv', 'jafa', 'תל אביב', 'ת''א', 'רמת-גן', 'ר''ג', '0סכנין', '00יפו', 'קניון איילון', 'באקע על-גרביה']

for location in locations:
    city_info = city_mapping.get(location.lower())
    if city_info:
        print(f"{location} belongs to {city_info['city']} city in the {city_info['district']} district.")
    else:
        print(f"No information available for {location}.")


# In[2]:


# Define a dictionary mapping each unique city name to a city identifier and district
city_mapping = {
    'תל אביב': {'city_code': 111, 'district': 'Tel Aviv'},
    'ת''א': {'city_code': 111, 'district': 'Tel Aviv'},
    'רמת גן': {'city_code': 112, 'district': 'Tel Aviv'},
    'ר''ג': {'city_code': 112, 'district': 'Tel Aviv'},
    'סכנין': {'city_code': 113, 'district': 'Northern'},
    'יפו': {'city_code': 114, 'district': 'Tel Aviv'},
    'קניון איילון': {'city_code': 115, 'district': 'Tel Aviv'},
    'באקע': {'city_code': 116, 'district': 'Southern'}
    # Add more entries as needed
}

# List of locations
locations = ['tel-aviv', 'jafa', 'תל אביב', 'ת''א', 'רמת-גן', 'ר''ג', '0סכנין', '00יפו', 'קניון איילון', 'באקע על-גרביה']

# Mapping function
def map_location_to_city(location):
    for city_name, city_info in city_mapping.items():
        if location.lower() in city_name.lower():
            return city_info

# Create a dictionary to store the results
location_result = {}

# Map locations to cities
for location in locations:
    city_info = map_location_to_city(location)
    if city_info:
        location_result[location] = {'city': city_info['district'], 'city_code': city_info['city_code']}

# Print the results
for location, info in location_result.items():
    print(f"{location} belongs to {info['city']} (City Code: {info['city_code']})")


# In[3]:


# Define a dictionary mapping each unique city name to a city identifier and district
city_mapping = {
    'תל אביב': {'city_code': 111, 'district': 'Tel Aviv'},
    'ת''א': {'city_code': 111, 'district': 'Tel Aviv'},
    'רמת גן': {'city_code': 112, 'district': 'Tel Aviv'},
    'ר''ג': {'city_code': 112, 'district': 'Tel Aviv'},
    'סכנין': {'city_code': 113, 'district': 'Northern'},
    'יפו': {'city_code': 114, 'district': 'Tel Aviv'},
    'קניון איילון': {'city_code': 115, 'district': 'Tel Aviv'},
    'באקע': {'city_code': 116, 'district': 'Southern'}
    # Add more entries as needed
}

# List of locations
locations = ['tel-aviv', 'jafa', 'תל אביב', 'ת''א', 'רמת-גן', 'ר''ג', '0סכנין', '00יפו', 'קניון איילון', 'באקע על-גרביה']

# Mapping function
def map_location_to_city(location):
    for city_name, city_info in city_mapping.items():
        if location.lower() in city_name.lower():
            return city_info

# Create a dictionary to store the results
location_result = {}

# Map locations to cities
for location in locations:
    city_info = map_location_to_city(location)
    if city_info:
        location_result[location] = {'city': city_info['district'], 'city_code': city_info['city_code']}

# Print the results
for location, info in location_result.items():
    print(f"{location} belongs to {info['city']} (City Code: {info['city_code']})")


# In[4]:


map_location_to_city(יפו)


# In[ ]:




