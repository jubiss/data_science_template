import sys,os
sys.path.append(os.getcwd())
from sklearn.base import BaseEstimator, TransformerMixin
from src.features import pre_processing as pp
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def features_pipeline():
    numeric_column = ''
    category_column = ''
    enc = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    transform_categorical = ColumnTransformer(
        transformers=[
            ('OneHotEncoder', enc, [category_column]),
        ],
        remainder='passthrough'  # This will include all the other columns in the output
    )

    pipeline = [('clipping_numeric', pp.ClippingColumn(column=numeric_column, quantile=0.95)),
                ('other_category_column', pp.OthersCategoryTransformer(column=category_column, low_threshold=0.01)),
                ('OneHotEncoding', transform_categorical)
                            ]
    grid_search = {
        'clipping_numeric__quantile': [None, 0.95, 0.9],
        'other_category_column__low_threshold': [None, 0.01, 0.05]
    }
    return pipeline, grid_search


class BuildFeatures_CV(BaseEstimator, TransformerMixin):
    """"
    Class used to create features that need to be cross validated to prevent Data Leakage.
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return X
    
class BuildFeatures(BaseEstimator, TransformerMixin):
    """
    Class used to create features that not need to be cross validated to prevent Data Leakage
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return X