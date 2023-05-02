import pandas as pd
# import pymongo
from pymongo import MongoClient


# Establish a connection to MongoDB
CLIENT = MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT["pokemon_db"]


def group_by_stat(stat='Hp', *, db=DATABASE) -> pd.DataFrame:
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

    # Create initial dataframe
    init_dataframe = (
        pd.DataFrame(pkmn_lookup)
        .set_index('Name')
        .rename(columns={
            'Sp_Attack': 'Sp. Attack',
            'Sp_Defense': 'Sp. Defense',
        })
    )
    
    # Create subset dataframe with 10 entries by the highest given stat
    sorted_stat = init_dataframe.sort_values(stat, ascending=False)
    
    return sorted_stat.head(10)


if __name__ == '__main__':
    pass
    print(group_by_stat())
    # print(group_by_stat('Attack'))
    # print(group_by_stat('Speed'))
    