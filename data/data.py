import pandas as pd
# import pymongo
from pymongo import MongoClient


# Establish a connection to MongoDB
CLIENT = MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT["pokemon_db"]


def stats_data(*, db=DATABASE):
    collection = db['pokemon_collections']
    
    pkmn_docs = collection.find()
    pkmn_data = ['Name', 'Hp', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense', 'Speed']
    
    pkmn_lookup = []
    
    # Iterate over the collection entries then append to pkmn_lookup
    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in filter(lambda key: key in pkmn_data, pkmn_doc.keys())}
        pkmn_lookup.append(pkmn_entry)

    return (
        pd.DataFrame(pkmn_lookup)
            .set_index('Name')
            .rename(columns={'Sp_Attack': 'Sp. Attack',
                             'Sp_Defense': 'Sp. Defense',})
        )


# Export categorical data of Pokemon
def category_data(*, db=DATABASE):
    collection = db['pokemon_collections']
    
    pkmn_docs = collection.find()
    pkmn_data = ['Name', 'Pokedex_Number', 'Type', 'Ability']
    
    pkmn_lookup = []
    
    # Iterate over the collection entries then append to pkmn_lookup
    for pkmn_doc in pkmn_docs:
        pkmn_entry = {k: pkmn_doc[k]
                      for k in filter(lambda key: key in pkmn_data, pkmn_doc.keys())}
        pkmn_lookup.append(pkmn_entry)

    return pd.DataFrame(pkmn_lookup).set_index('Name')


if __name__ == '__main__':
    print(category_data())
    