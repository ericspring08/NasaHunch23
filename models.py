from sklearn.svm import SVC, NuSVC
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier, HistGradientBoostingClassifier, IsolationForest
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from catboost import CatBoostClassifier
from sklearn.linear_model import RidgeClassifier, PassiveAggressiveClassifier, SGDOneClassSVM, SGDClassifier
from sklearn.dummy import DummyClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

model_options = {
    # SVC is SVCRBF
    'SVC': SVC(),
    'SVCLinear': SVC(kernel='linear'),
    'SVCPoly': SVC(kernel='poly'),
    'SVCSigmoid': SVC(kernel='sigmoid'),
    'NuSVC': NuSVC(nu=0.1),
    'GradientBoosting': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=5, random_state=0),
    'GradientBoostingSE': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=5, random_state=0, criterion='squared_error'),
    'GaussianNB': GaussianNB(),
    'GaussianNBVarSmoothing': GaussianNB(var_smoothing=1e-09),
    'DecisionTree': DecisionTreeClassifier(),
    'DecisionTreeEntropy': DecisionTreeClassifier(criterion='entropy'),
    'DecisionTreeGini': DecisionTreeClassifier(criterion='gini'),
    'KNeighbors': KNeighborsClassifier(n_neighbors=5, n_jobs=-1),
    'KNeighborsDistance': KNeighborsClassifier(n_neighbors=5, weights='distance', n_jobs=-1),
    'AdaBoost': AdaBoostClassifier(),
    'AdaBoostSAMME': AdaBoostClassifier(algorithm='SAMME'),
    'RandomForest': RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1, random_state=42, n_jobs=-1),
    'RandomForestEntropy': RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1, random_state=42, n_jobs=-1, criterion='entropy'),
    'RandomForestGini': RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1, random_state=42, n_jobs=-1, criterion='gini'),
    'MLP': MLPClassifier(),
    'MLPIdentity': MLPClassifier(activation='identity'),
    'MLPLogistic': MLPClassifier(activation='logistic'),
    'MLPTanh': MLPClassifier(activation='tanh'),
    'MLPReLU': MLPClassifier(activation='relu'),
    'QDA': QuadraticDiscriminantAnalysis(),
    'QDAPriors': QuadraticDiscriminantAnalysis(priors=[0.5, 0.5]),
    'CatBoost': CatBoostClassifier(verbose=False),
    'CatBoostAccuracy': CatBoostClassifier(verbose=False, eval_metric='Accuracy'),
    'CatBoostAUC': CatBoostClassifier(verbose=False, eval_metric='AUC'),
    'CatBoostCrossEntropy': CatBoostClassifier(verbose=False, eval_metric='CrossEntropy'),
    'CatBoostF1': CatBoostClassifier(verbose=False, eval_metric='F1'),
    'CatBoostLogloss': CatBoostClassifier(verbose=False, eval_metric='Logloss'),
    'CatBoostMCC': CatBoostClassifier(verbose=False, eval_metric='MCC'),
    'CatBoostPrecision': CatBoostClassifier(verbose=False, eval_metric='Precision'),
    'CatBoostRecall': CatBoostClassifier(verbose=False, eval_metric='Recall'),
    'ExtraTrees': ExtraTreesClassifier(n_jobs=-1),
    'ExtraTreesEntropy': ExtraTreesClassifier(n_jobs=-1, criterion='entropy'),
    'ExtraTreesGini': ExtraTreesClassifier(n_jobs=-1, criterion='gini'),
    'Bagging': BaggingClassifier(n_jobs=-1),
    'BaggingKNN': BaggingClassifier(KNeighborsClassifier(n_jobs=-1)),
    'BaggingDecisionTree': BaggingClassifier(DecisionTreeClassifier()),
    'BaggingExtraTrees': BaggingClassifier(ExtraTreesClassifier(n_jobs=-1)),
    'BaggingRandomForest': BaggingClassifier(RandomForestClassifier(n_jobs=-1)),
    'BaggingGradientBoosting': BaggingClassifier(GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=5, random_state=0)),
    'BaggingMLP': BaggingClassifier(MLPClassifier()),
    'BaggingQDA': BaggingClassifier(QuadraticDiscriminantAnalysis()),
    'BaggingLDA': BaggingClassifier(LinearDiscriminantAnalysis()),
    'BaggingSVC': BaggingClassifier(SVC()),
    'BaggingNuSVC': BaggingClassifier(NuSVC()),
    'BaggingGaussianNB': BaggingClassifier(GaussianNB()),
    'BaggingRidge': BaggingClassifier(RidgeClassifier()),
    'BaggingPA': BaggingClassifier(PassiveAggressiveClassifier(n_jobs=-1)),
    'BaggingSGD': BaggingClassifier(SGDClassifier(n_jobs=-1)),
    'BaggingDummy': BaggingClassifier(DummyClassifier(strategy="uniform")),
    'BaggingHGB': BaggingClassifier(HistGradientBoostingClassifier()),
    'BaggingIsolationForest': BaggingClassifier(IsolationForest(n_jobs=-1)),
    'Ridge': RidgeClassifier(),
    'PA': PassiveAggressiveClassifier(n_jobs=-1),
    'SGDOneClass': SGDOneClassSVM(),
    'SGD': SGDClassifier(n_jobs=-1),
    'Dummy': DummyClassifier(strategy="uniform"),
    'HGB': HistGradientBoostingClassifier(),
    'LGBM': LGBMClassifier(verbose=-1, n_jobs=-1),
    'XGB': XGBClassifier(),
    'LDA': LinearDiscriminantAnalysis(),
    'IsolationForest': IsolationForest(n_jobs=-1),
    'ExtraTree': ExtraTreeClassifier(),
    'ExtraTreeEntropy': ExtraTreeClassifier(criterion='entropy'),
    'ExtraTreeGini': ExtraTreeClassifier(criterion='gini'),
}
