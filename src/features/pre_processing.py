from sklearn.base import BaseEstimator, TransformerMixin


def OneHotEncoderTransformerSelectedColumns(categorical_features):
    from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
    from sklearn.compose import ColumnTransformer
    enc = OneHotEncoder(handle_unknown='ignore')
    categorical_features = ['UF']

    transform_categorical = ColumnTransformer(
        transformers=[
            ('OneHotEncoder', enc, categorical_features),
        ],
        remainder='passthrough'  # This will include all the other columns in the output
    )
    return transform_categorical

class PreProcessingFeatures(BaseEstimator, TransformerMixin):
    """Class used to make all the preprocessing steps for the model to work properly"""
    def __init__(self):
        pass

    def fit(self,X, y=None):
        pass

    def transform(self,X, y=None):
        pass

    def missing_values(self, X, y):
        # Dealing with missing values
        pass

    def transforming_data(self, X, y):
        # Transforming data
        pass

    def scaling_data(self, X, y):
        pass

    def enconding_data(self, X, y):
        pass

    def outliers(self, X, y):
        pass