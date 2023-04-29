import pandas as pd
# import pymongo
from pymongo import MongoClient


# Establish a connection to MongoDB
CLIENT = MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT["pokemon_db"]


# Unfiltered data table
def all_data(*, db=DATABASE) -> pd.DataFrame:
    collection = db['pokemon_collections2']
    
    pkmn_docs = collection.find()
    
    pkmn_lookup = []
    
    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in pkmn_doc.keys()}
        
        pkmn_lookup.append(pkmn_entry)

    return (
        pd.DataFrame(pkmn_lookup)
            .set_index('Name')
            .rename(columns={'Sp_Attack': 'Sp. Attack',
                             'Sp_Defense': 'Sp. Defense',})
    )


def stats_data(*, db=DATABASE):
    collection = db['pokemon_collections2']
    
    pkmn_docs = collection.find()
    pkmn_data = ['Name', 'Hp', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense', 'Speed']
    
    pkmn_lookup = []
    
    # Iterate over the collection entries then append to pkmn_lookup
    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in filter(lambda key: key in pkmn_data, 
                                      pkmn_doc.keys())}
        pkmn_lookup.append(pkmn_entry)

    return (
        pd.DataFrame(pkmn_lookup)
            .set_index('Name')
            .rename(columns={'Sp_Attack': 'Sp. Attack',
                             'Sp_Defense': 'Sp. Defense',})
        )


# Export categorical data of Pokemon
def category_data(*, db=DATABASE):
    collection = db['pokemon_collections2']
    
    pkmn_docs = collection.find()
    pkmn_data = ['Name', 'Pokedex_Number', 'Generation', 'Type', 'Ability']
    
    pkmn_lookup = []
    
    # Iterate over the collection entries then append to pkmn_lookup
    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in filter(lambda key: key in pkmn_data, 
                                      pkmn_doc.keys())}
        pkmn_lookup.append(pkmn_entry)

    return pd.DataFrame(pkmn_lookup).set_index('Name')


# Export distributed grouped data
def distributed_data(*, db=DATABASE):
    collection = db['pokemon_collections2']
    
    pkmn_docs = collection.find()
    
    # Add a distibuted group column here
    pkmn_dist_data = [
        'Generation',
        # 'Ex. Egg Group
    ]
    
    pkmn_lookup = []

    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in filter(lambda key: key in pkmn_dist_data, 
                                      pkmn_doc.keys())}
        pkmn_lookup.append(pkmn_entry)

    return pd.DataFrame(pkmn_lookup)
        

if __name__ == '__main__':
    print(distributed_data())
    pass
    # print(category_data())
    