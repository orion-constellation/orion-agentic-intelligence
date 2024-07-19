"""
Custom Models for Clustering
"""
from sklearn.base import BaseEstimator, ClusterMixin
from wandb_fns import create_model_artifact, create_dataset_artifact,  modeL_predict_eval
from sklearn.utils.validation import check_is_fitted

# Custom DBSCAN Transformer
class DBSCANTransformer(BaseEstimator, ClusterMixin):
    def __init__(self, eps=0.5, min_samples=8):
        """
        Initialize the DBSCANTransformer.

        Parameters:
            eps (float): The maximum distance between two samples for one to be considered as in the neighborhood of the other.
            min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.

        Returns:
            None
        """
        self.eps = eps
        self.min_samples = min_samples

    def fit(self, X, y=None):
        """
        Fit the DBSCANTransformer to the given data.

        Parameters:
            X (array-like): The input data to fit the model on.
            y (array-like, optional): The target values (ignored by DBSCANTransformer). Defaults to None.

        Returns:
            self: The fitted DBSCANTransformer instance.
        """
        self.dbscan_ = DBSCANTransformer(eps=self.eps, min_samples=self.min_samples)
        self.dbscan_.fit(X)
        return self

    def predict(self, X, y=None):
        """
        Predict cluster labels for the input samples.

        Parameters:
            X (array-like): The input samples.
            y (array-like, optional): Ignored. Defaults to None.

        Returns:
            array-like: Cluster labels for each sample.
        """
        check_is_fitted(self, 'dbscan')
        return self.dbscan_.fit_predict(X)

