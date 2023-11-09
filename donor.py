import pandas as pd

def create_dataframe_and_print():
  df = pd.DataFrame(zip(range(10), range(10)))
  print(df)
