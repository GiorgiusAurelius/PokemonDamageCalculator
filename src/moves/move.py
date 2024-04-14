import pandas as pd

class Move():
  """
  This class represents a pokèmon's move.
  A move should have the following characteristics:
    - Name
    - type
    - power
    - damage_class
  """
  
  def __init__(self, move_info:pd.DataFrame) -> None:
    
    self.name = move_info.get('name').values[0]
    self.type = move_info.get('type').values[0]
    self.power = move_info.get('power').values[0]
    self.damage_class = move_info.get('damage_class').values[0]
    
  def print_move_info(self):
    print(f"name: {self.name}")
    print(f"type: {self.type}")
    print(f"power: {self.power}")
    print(f"damage class: {self.damage_class}")

if __name__ == "__main__":
  from src.dataset_reader.data_reader import DatasetReader
  # file path to the csv files containing the data
  move_fp = 'C:/Users/Diego/code projects/pokemonDamageCalculator/dataset/metadata_pokemon_moves.csv'
  move_df = pd.read_csv(move_fp)
  move_dr = DatasetReader(move_fp)
  
  move = Move(move_dr.search_by_name('Scald'))
  move.print_move_info()
  
 