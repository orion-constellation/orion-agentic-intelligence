
import os
import numpy as np
import pandas as pd
import configparser
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, ClusterMixin
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score, accuracy_score, f1_score, \
recall_score, precision_score, adjusted_rand_score, normalized_mutual_info_score
import matplotlib.pyplot as plt
from sklearn.utils.validation import check_is_fitted
from sklearn.utils import check_array
from syn_data_gen import main_data as syn
from sklearn.cluster import KMeans, DBSCAN
from custom_models import DBSCANTransformer

import wandb
from loguru import logger
data = '..agents.sample_data.json'

wandb.login(key=os.getenv('WANDB_API_KEY'))
wandb.init(project="d2i", entity="orion-ai",   
    config={
    "learning_rate": 0.02,
    "architecture": [KMeans, DBSCANTransformer()],
    "dataset": "Synthetic-Gen180724",
    "epochs": 10,
    })

file_path = '../syn_data_gen/'
config = configparser.ConfigParser()
config.read('config.ini')


   
#Import Data
if config.DEBUG == True:
    df = syn.main()
elif os.path.isfile("") and os.path(file_path).split("/")[-1].endswith(".csv"):
    df = pd.read_csv(file_path)
elif os.path.isfile("") and os.path(file_path).split("/")[-1].endswith(".json"):
    df = pd.read_json(file_path)
elif os.path.isfile("") and os.path(file_path).split("/")[-1].endswith(".parquet"):
    df = pd.read_parquet(file_path)
else:
    raise ValueError("File type not supported")

def pipelines(data, algs=["Kmeans", "DBSCAN_Transformer"]):
    """
    Pipelines for the initial clustering of the data
    Input: data (JSON) from threat hunters
    Args: "Scaler", "Model"
    
    
    Return Models
    """
    pipeline_kmeans = Pipeline([
        ('scaler',StandardScaler(),
        'kmeans', KMeans(n_clusters=2, random_state=42, algorithm="auto")) 
    ])

    pipeline_dbscan = Pipeline([
        ('scaler', StandardScaler()),
        ('dbscan', DBSCAN(eps=0.5, min_samples=5))
    ])
def cluster_pipelines(data, pipelines=[pipeline_kmeans, pipeline_dbscan], algs="kmeans"):
    if algs == "kmeans":
        pipeline = pipeline_kmeans
    elif algs == "dbscan":
        pipeline = pipeline_dbscan
    else:
        raise ValueError(f"Unsupported algorithm: {algs}")

    scaled_features = pipeline.named_steps['scaler'].fit_transform(data)
    clusters = pipeline.named_steps[algs].fit_predict(scaled_features)
    
    # Calculating Error Metrics
    silhouette = silhouette_score(scaled_features, clusters)
    ari = adjusted_rand_score(data, clusters)
    nmi = normalized_mutual_info_score(data, clusters)

    wandb.log({"silhouette_score": silhouette})
    wandb.log({"adjusted_rand_score": ari})
    wandb.log({"normalized_mutual_info_score": nmi})
    
    print(f"Silhouette Score: {silhouette}")
    print(f"Adjusted Rand Index: {ari}")
    print(f"Normalized Mutual Information Score: {nmi}")

    return clusters

# Example usage
data = syn.main()  # Example data, replace with actual dataset
clusters = cluster_pipelines(data, algs="kmeans")
           



