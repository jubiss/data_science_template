import numpy as np
def SGDRegressor():
    from sklearn.linear_model import SGDRegressor

    model = SGDRegressor(max_iter=50000)

    model_param_grid = {
    'model__loss': ['squared_error', 'huber', 'epsilon_insensitive'],
    'model__penalty': ['l2', 'l1', 'elasticnet', None],
    'model__learning_rate': ['constant', 'optimal', 'invscaling'],
    }

    return model, model_param_grid

def LinearRegression():
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model_param_grid = {
    }

    return model, model_param_grid