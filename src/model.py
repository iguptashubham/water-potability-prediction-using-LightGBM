from lightgbm import LGBMClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from logger import logger_config

build_logger = logger_config('build_model.log','build_model_log')

def model_pipeline(model_param:dict):
    build_logger.debug('Apply Column Transformations')
    clf_transformation = ColumnTransformer(
        transformers=[
            ('ph',MinMaxScaler(),[0]),
            ("""Hardness, Solids, Chloramines, Sulfate, Conductivity,
       Organic_carbon, Trihalomethanes, Turbidity""",StandardScaler(),[1,2,3,4,5,6,7,8]),
        ],remainder='passthrough'
    )
    
    build_logger.debug('Building the Pipeline of lgmbclassifier')
    
    lgbpipeline = Pipeline(
        [
            ('Columns Transformation',clf_transformation),
            ('LightGBM Regressor', LGBMClassifier(**model_param))
        ]
    )
    
    return lgbpipeline