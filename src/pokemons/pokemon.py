import pandas as pd

class Pokemon():
  """
  This object represents a pokèmon.
  A pokèmon should have the following characteristics:
    - Name
    - Type
    - Stats
    - Move set
    - Nature
    - Gender
    - Level
    - Ability
    - Status
    - Item
  """ 
  def __init__(self, info:pd.DataFrame, level:int=100) -> None:
    
    self.name = info.get('name').values[0]
    self.level = level
    self.stat_keys = ['HP', 'ATK', 'DEF', 'ATK_SP', 'DEF_SP', 'SPEED']
    
    self.type = []
    self.set_type(info)
    
    self.statistics = {}
    
    self.move_set = {}
    self.status = 'Healty'
    self.nature = None
    self.item = None
    self.gender = 'Male'
    
    self.iv = self.set_iv()
    self.ev = self.set_ev()
    self.stats = self.set_stats()
    
    
  def set_type(self, info:pd.DataFrame):
    """Setter function for the pokemon's typing list

    Args:
      - info (pd.DataFrame): info dataframe containing the pokemon's information
    """
    type_1 = info.get('type_1').values[0]
    type_2 = info.get('type_2').values[0]
    
    self.type.append(type_1)
    
    # Find if the second type is NaN (a float) or not
    if not isinstance(type_2, float):
      self.type.append(type_2)
  
  def set_nature(self, nature:str):
    pass

  def set_item(self, name:str):
    raise NotImplementedError("Items not yet implemented.")

  def set_gender(self, gender:str):
    """Setter for the pokemon's gender

    Args:
      - gender (str): The gender of the pokemon
    """
    assert gender == 'Male' or gender == 'Female' or gender == '', f"Unknown gender provided. Got: {gender} ..."
    self.gender = gender
  
  def set_iv(self, iv:dict=None) -> dict:
    """Setter for the IVs of the pokemon. If no dictionary is passed in input, it sets the IVs as default to the minimum.

    Args:
      - iv (dict, optional): dictionary containing the specific IVs provided by the user (default=None)

    Returns:
      - dict: the dictionary with the set IVs
    """
    iv_dict = {}
    
    if iv is None:
      for key in self.stat_keys:
        iv_dict[key] = 0
    else:
      # check the presence of every stat and the correctness of the provided values
      for key in iv:
        assert key in self.stat_keys, "Some stats are missing in the provided id dictionary!"
        assert iv[key] <= 31, f"Unexpected value for the IV at stat: {key}.\n Got {iv[key]}, should be less than 31!"
      iv_dict = iv
    
    return iv_dict
  
  def set_ev(self, ev:dict=None) -> dict:
    """Setter for the pokemon's EVs. If no dictionary is provided, it sets the EVs to the minimum.

    Args:
      - ev (dict, optional): dictionary that contains the specific EVs provided by the user (default=None)

    Returns:
      - dict: the dictionary with the EVs
    """
    ev_dict = {}
    tot_ev = 0
    
    if ev is None:
      for key in self.stat_keys:
        ev_dict[key] = 0
    else:
      # check the presence of every stat, the correctness of the overall provided values
      for key in ev:
        assert key in self.stat_keys, "Some stats are missing in the provided id dictionary!"
        assert ev[key] <= 252, f"Unexpected value for the EVs at stat: {key}.\n Got {ev[key]}, should be less than 252!"
        tot_ev += ev[key]
      assert tot_ev <= 510, f"Unexpected total number of EVs provided!\n Got {tot_ev}, should be less than 510!" 
      
      ev_dict = ev
  
  def set_stats(self, info:pd.DataFrame) -> dict:
    pass