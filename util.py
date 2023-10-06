import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[2] = bath
    x[1] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return int(str(__model.predict([x])[0])[:2])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("C:/code/CHP/server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 5 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('C:/code/CHP/server/artifacts/Chennai_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('anna nagar', 1000, 3, 3))
    print(get_estimated_price('Anna Nagar', 1000, 2, 2))
    print(get_estimated_price('chrompet', 1000, 2, 2)) # other location
    print(get_estimated_price('T Nagar', 1000, 2, 2))  # other location