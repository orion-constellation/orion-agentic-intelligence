import os
from typing import Dict
import pandas as pd
import numpy as np
import json
import arrow 


def load_dataset(data) -> pd.DataFrame:
    """
    Load the Dolly dataset and convert to a pandas DataFrame
    """
    dataset = pd.read_csv(data)
    return dataset







In the cell below we perform the following preprocessing steps:
* Load the Dolly dataset and convert to a pandas DataFrame
* Select examples in the set CATEGORY
* Clean text and convert to ascii
* Remove examples with more words than MAX_WORDS
* Drop unnecessary columns
* Sample NUM_EXAMPLES examples for the demo