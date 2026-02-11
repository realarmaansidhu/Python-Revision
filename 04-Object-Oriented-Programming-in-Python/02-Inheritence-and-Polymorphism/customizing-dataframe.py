# Python code to implement a custom DataFrame class that logs the creation time of the DataFrame and includes it in the CSV output.

# Import pandas as pd
from datetime import datetime
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created_at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)