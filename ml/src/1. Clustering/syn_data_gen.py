from sklearn.datasets import make_classification
import numpy as np
import pandas as pd
import json
import wandb
import loguru

wandb.login(key="")
wandb.init(project="d2i", entity="orion-ai",   

def main_data():
    # Generate synthetic imbalanced data
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=42)

    # Convert to DataFrame for easier handling
    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
    target = data['label']
    
    #Clean Data
    X = data.drop(['label'], axis=1)
    y = data['label']
    
    
    try: 
        with open('../data.json', 'w') as output:
            data = json.dumps(output)
        with open('../target.json', 'w') as f:
            target = json.dumps(f) # data['target'])
    except FileExistsError as e:
        print(e)
    
    return data, target

if __name__ == '__main__':
    main()
    print(f"{X} \n {y}")