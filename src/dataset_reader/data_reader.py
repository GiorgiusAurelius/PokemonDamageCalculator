import pandas as pd
import os
import numpy as np

class DatasetReader():
    """This class contains the pandas Dataframe read from the path provided by the user and contains the functions to search for specific data in it.
    """
    def __init__(self, file_path:str) -> None:
        self.fp = file_path
        
        assert os.path.exists(self.fp), f"Couldn't find the file containing the dataset. Got: {self.fp} ..."
        self.dataframe = pd.read_csv(self.fp)
        self.set_utility_string()
        
    
    #TODO: make the search possible even without having the full name
    def search_by_name(self, name:str):
        """Function that returns the single row of the input dataframe.
        The search is performed using a string that corresponds to a pokemon or a move.

        Args:
            name (str): Name of a specific pokemon or move
        
        Returns:
            row (pandas.Dataframe): row corresponding to the provided pokemon/move's name
        """
        name_col = self.dataframe.get('name').to_list()
        # print(f'name_col:\n {name_col}')
        if name in name_col:
            # retrieve the row with the data of the pokemon/move
            row = self.dataframe.loc[self.dataframe['name'] == name]
        else:
            raise Exception(f"The provided {self.utility_string}'s name is not present in the dataset!\n Got: {name}") 

        return row


    def search_by_id(self, id:int):
        """Function that returns the single row of the input dataframe.
        The search is performed using an int that corresponds to a pokemon/move.

        Args:
            id (int): id of a specific pokemon or move
        
        Returns:
            row (pandas.Dataframe): row corresponding to the provided pokemon/move's name
        """
        name_col = self.dataframe.get('id').to_list()
        
        if id in name_col:
            row = self.dataframe.loc[self.dataframe['id'] == id]
        else:
            raise Exception(f"The provided {self.utility_string}'s id is not present in the dataset!\n Got: {id}")
        
        return row
    
    def set_utility_string(self):
        """Function used to set a string that will be used to define if the datframe is a move or pokemon one.
        """
        # Get the last part of the file_path
        csv_file_name = self.fp.split('/')[-1]
        # Remove the file extension
        csv_file_name = csv_file_name.split('.')[0]
        
        self.utility_string = csv_file_name.split('_')[-1]
        # print(f'ut_str: {self.utility_string}')    
        assert self.utility_string in ['pokemon', 'moves'], f"Weird utility string found. Got: {self.utility_string} ..."

    
    
def colum_printer(df:pd.DataFrame):
    """Function for printing the columns of a dataframe

    Args:
        df (pd.DataFrame): Dataframe which columns should be printed
    """
    print()
    for col in df.columns:
        print(f"{col}", end="\t")
    print()

def row_printer(df:pd.DataFrame, name:str=None, id:int=None):
    """Function for printing the row, given the name or the id of the pokemon/move

    Args:
        df (pd.DataFrame): dataframe to read
        name (str): name of the move or the pokemon/move to print (default: None)
        id (int): id of the move or the pokemon to print (default: 0)
    """
    assert name == None or id == None, f"Name or id not provided."
    
    if name == None and id != None:
        row = df.loc[df['id'] == id]
    elif name != None and id == None:
        row = df.loc[df['name'] == name]
    else:
        raise Exception(f"Provide only id or name!")

    print()
    # print(type(row))
    # print()
    print(row)

if __name__ == '__main__':
    # file path to the csv files containing the data
    pokemon_fp = 'C:/Users/Diego/code projects/pokemonDamageCalculator/dataset/metadata_pokemon.csv'
    move_fp = 'C:/Users/Diego/code projects/pokemonDamageCalculator/dataset/metadata_pokemon_moves.csv'
    
    assert os.path.exists(pokemon_fp), f"Couldn't find the file containing the pokemon data.\n Got: {pokemon_fp} ..."
    assert os.path.exists(pokemon_fp), f"Couldn't find the file containing the pokemon moves' data.\n Got: {move_fp} ..."
    
    pokemon_df = pd.read_csv(pokemon_fp)
    move_df = pd.read_csv(move_fp)
    
    # colum_printer(pokemon_df)
    # colum_printer(move_df)   
    # row_printer(pokemon_df, name='Charmeleon')
    # row_printer(move_df, name='Surf') 
    
    dr = DatasetReader(pokemon_fp)
    print(dr.search_by_name('Bulbasaur'))
    
    dr_m = DatasetReader(move_fp)
    
     