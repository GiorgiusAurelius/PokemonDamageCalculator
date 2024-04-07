import pandas as pd
import os

class DatasetReader():
    
    def __init__(self, file_path:str) -> None:
        self.fp = file_path
        
        assert os.path.exists(self.fp), f"Couldn't find the file containing the dataset. Got: {self.fp} ..."
        self.dataframe = pd.read_csv(self.fp)
         
    
    
def colum_printer(df:pd.DataFrame):
    """Function for printing the columns of a dataframe

    Args:
        df (pd.DataFrame): Dataframe which columns should be printed
    """
    print()
    for col in df.columns:
        print(f"{col}", end="\t")
    print()

def row_printer(df:pd.DataFrame, name:str=None, id:str=0):
    """Function for printing the row, given the name or the id of the pokemon/move

    Args:
        df (pd.DataFrame): dataframe to read
        name (str): name of the move or the pokemon/move to print (default: None)
        id (int): id of the move or the pokemon to print (default: 0)
    """
    assert name == None or id == 0, f"Name or id not provided."
    
    if name == None and id != 0:
        row = df.loc[df['id'] == id]
    elif name != None and id == 0:
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
    
    colum_printer(pokemon_df)
    colum_printer(move_df)   
    
    row_printer(pokemon_df, name='Charmeleon')
    row_printer(move_df, name='Surf') 