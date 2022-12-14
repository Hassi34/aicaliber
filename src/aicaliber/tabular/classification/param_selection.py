from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
from sklearn.impute import SimpleImputer, KNNImputer
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, make_scorer, precision_score

def get_scaler(scaler):
    if scaler =='StandardScaler':
        return StandardScaler()
    elif scaler =='MinMaxScaler':
        return MinMaxScaler()
    elif scaler =='MaxAbsScaler':
        return MaxAbsScaler()
    elif scaler =='RobustScaler': 
        return RobustScaler()
    else:
        raise ValueError(f'Invalid scaler: "{scaler}"')

def get_imputer(imputer):
    if imputer == "SimpleImputer":
        return SimpleImputer(strategy = 'mean', missing_values = np.nan)
    elif imputer == "KNNImputer":
        return KNNImputer(n_neighbors=3, missing_values= np.nan)
    else:
        raise ValueError(f'Invalid imputer: "{imputer}"')

def get_heper_param_grid(model_name, metrics):
    if metrics == "f1_score":
        scoring = make_scorer(f1_score, average = 'weighted')
    elif metrics == "accuracy":
        scoring = make_scorer(accuracy_score)
    elif metrics == "recall":
        scoring = make_scorer(recall_score, average= 'weighted')
    elif metrics == "precision":
        scoring = make_scorer(precision_score, average= 'weighted')
    if model_name == "knn":
        param_grid = { 'classifier__n_neighbors' : np.arange(2, 14, 2), 
                        'classifier__weights' : ['uniform','distance'],
                        'classifier__metric' : ['minkowski','euclidean','manhattan'],
                        'classifier__algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute'],
                        'classifier__leaf_size' : np.arange(5,50,5)
                }

    elif model_name == "MLPClassifier":
        param_grid = {  'classifier__hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
                        'classifier__activation': ['tanh','logistic','relu'],
                        'classifier__solver': ['sgd', 'lbfgs', 'adam'],
                        'classifier__alpha':  np.linspace(0.0001, 0.9, 5),
                        'classifier__learning_rate': ['constant','invscaling','adaptive']
                }

    elif model_name == "RandForestClf":
        param_grid = {  'classifier__max_depth': [10,30, 60, 70, None],
                        'classifier__bootstrap': [True, False],
                        'classifier__min_samples_split': np.arange(2,8,2),
                        'classifier__min_samples_leaf': np.arange(1,5,2),
                        'classifier__n_estimators':  np.arange(10,200,20),
                        'classifier__criterion': ['gini','entropy'],
                        'classifier__max_features': ['sqrt', 'log2', None]
                }
    elif model_name == "SVC":
        param_grid = {  'classifier__C': [0.1, 1, 10, 50],
                        'classifier__kernel': ['rbf', 'poly', 'sigmoid', 'linear'],
                        'classifier__gamma': np.linspace(0.001, 1.0, 5)
                }
    elif model_name == "LogisticRegression":
        param_grid = {
                'classifier_penalty' : ['l1','l2'], 
                'classifier_C' : np.logspace(-3,3,7),
                'classifier_solver'  : ['newton-cg', 'lbfgs', 'liblinear']
                }
    elif model_name == "AdaBoost":
        param_grid = { 'classifier__n_estimators': np.arange(5, 100, 5),
                       'classifier__learning_rate':  np.linspace(0.0001, 0.9, 5),
                       'classifier__algorithm': ['SAMME', 'SAMME.R']
                }
    elif model_name == "DecisionTree":
        param_grid = { 'classifier__criterion': ['gini','entropy', 'log_loss'],
                       'classifier__max_depth': np.arange(5, 40, 5),
                       'classifier__min_samples_split': np.arange(2, 6, 2),
                       'classifier__min_samples_leaf': np.arange(1, 10, 2),
                       'classifier__max_features' : [None, 'sqrt', 'log2'] 
                }
    elif model_name == "GaussianNB":
        param_grid = { 'classifier__var_smoothing': [1e-11, 1e-10, 1e-9]}
        
    elif model_name == "GradientBoostingClf":
        param_grid = { 'classifier__n_estimators': np.arange(5, 200, 10),
                       'classifier__learning_rate': np.linspace(0.0001, 0.9, 3),
                       'classifier__subsample': np.linspace(0.4, 1.0, 3),
                       'classifier__max_depth': np.arange(5, 20, 5),
                       'classifier__max_features': [None, 'sqrt', 'log2']
                }
    elif model_name == "SGDClassifier":
        param_grid = { 'classifier__learning_rate': ['constant', 'optimal', 'invscaling', 'adaptive'],
                       'classifier__alpha': [0.0001, 0.001, 0.01, 1, 10, 100, 1000],
                       'classifier__penalty':  ['l1', 'l2', 'elasticnet'],
                       'classifier__eta0': [1, 10, 100],
                       'classifier__loss': ['hinge','squared_hinge', 'log_loss', 'modified_huber', 'perceptron']
                }
    elif model_name == "ExtraTreesClf":
        param_grid = { 'classifier__n_estimators': np.arange(10,150,20),
                       'classifier__criterion' : ["gini", "entropy", "log_loss"],
                       'classifier__min_samples_leaf': np.arange(1,10,5),
                       'classifier__min_samples_split': np.arange(2,10,5),
                       'classifier__max_features': [None,'sqrt', 'log2']
                }
    elif model_name == "xgb":
        param_grid = { 'classifier__max_depth': np.arange(3, 18, 5),
                        'classifier__gamma': np.arange(1,15,3),
                        'classifier__eta': np.linspace(0.0001, 1.0, 5),
                        'classifier__colsample_bytree': np.linspace(0.5, 1, 3),
                        'classifier__n_estimators' : np.arange(10,150,20)
                }
    elif model_name == "lightGBM":
        param_grid = {  'classifier__n_estimators': np.arange(5,150,20),
                        'classifier__colsample_bytree': np.arange(0.3,0.8, 0.3),
                        'classifier__max_depth':np.arange(5,25,5) ,
                        'classifier__num_leaves': np.arange(10,100,10),
                        'classifier__min_split_gain': np.arange(0.2,0.5,0.1),
                        'classifier__subsample': np.arange(0.01,0.9,0.1)
                }   
    return param_grid, scoring

