import pandas as pd
import numpy as np
import re

# preprocessing dataset, making sure data is categorical and is suitable for the use by the KAD
def remap_values(data, mapping):
    # Convert data to strings before mapping
    if isinstance(data, pd.Series):
        return data.astype(str).map(mapping).fillna(data)
    else:
        return [mapping.get(str(val), val) for val in data]

shrooms = pd.read_csv('mushrooms.csv')

shrooms = shrooms[['class', 'cap-shape', 'cap-surface', 'cap-color', 'gill-size', 'stalk-shape', 'veil-type', 'population']]
print(shrooms.info())

# remapping values to be more understandable
mapping = {
    "e" : "Edible",
    "p" : "Poisonous"
}

shrooms['class'] = remap_values(shrooms['class'], mapping)


mapping = {
    'b': 'Bell',
    'c': 'Conical',
    'x': 'Convex',
    'f': 'Flat',
    'k': 'Knobbed',
    's': 'Sunken'
}

shrooms['cap-shape'] = remap_values(shrooms['cap-shape'], mapping)


mapping = {
    'f': 'Fibrous',
    'g': 'Grooves',
    'y': 'Scaly',
    's': 'Smooth'
}

shrooms['cap-surface'] = remap_values(shrooms['cap-surface'], mapping)


mapping = {
    'n': 'Brown',
    'b': 'Buff',
    'c': 'Cinnamon',
    'g': 'Gray',
    'r': 'Green',
    'p': 'Pink',
    'u': 'Purple',
    'e': 'Red',
    'w': 'White',
    'y': 'Yellow'
}

shrooms['cap-color'] = remap_values(shrooms['cap-color'], mapping)


mapping = {
    'b': 'Broad',
    'n': 'Narrow'
}

shrooms['gill-size'] = remap_values(shrooms['gill-size'], mapping)


mapping = {
    'e': 'Enlargening',
    't': 'Tapering'
}

shrooms['stalk-shape'] = remap_values(shrooms['stalk-shape'], mapping)


mapping = {
    'p': 'Partial',
    'u': 'Universal'
}

shrooms['veil-type'] = remap_values(shrooms['veil-type'], mapping)


mapping = {
    'a': 'Abundant',
    'c': 'Clustered',
    'n': 'Numerous',
    's': 'Scattered',
    'v': 'Several',
    'y': 'Solitary'
}

shrooms['population'] = remap_values(shrooms['population'], mapping)

# print(shrooms[0:10])

shrooms_sample = shrooms.sample(n=300)
print(len(shrooms_sample))
print(shrooms_sample.info())

shrooms_sample.to_csv('sample.csv', index=False)

# print(shrooms_sample.head(20))