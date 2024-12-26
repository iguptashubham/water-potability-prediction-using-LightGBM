import mlflow
import mlflow.sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, ConfusionMatrixDisplay, confusion_matrix
from pathlib import Path
from logger import logger_config
from model import model_pipeline
import pickle, yaml

train_logger = logger_config('train_model.log','train_model_log')

def train_model(params, train_df, test_df):
    train = pd.read_csv(train_df)
    test = pd.read_csv(test_df)
    
    x_train, y_train = train.iloc[:, :-1], train.iloc[:, -1]
    x_test, y_test = test.iloc[:, :-1], test.iloc[:, -1]
    
    train_logger.debug(msg="Model Training by given parameter")
    
    model = model_pipeline(params)
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    
    # Confusion Matrix and its display
    cm = confusion_matrix(y_test, pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title('Confusion Matrix')
    
    # Save the figure
    fig_path = 'confusion_matrix.png'
    plt.savefig(fig_path)
    plt.close()
    
    # Evaluation metrics
    metrics = {
        'accuracy_score': accuracy_score(y_test, pred),
        'f1_score': f1_score(y_test, pred),
        'precision_score': precision_score(y_test, pred),
        'recsall_score': recall_score(y_test, pred),
        'roc_auc_score': roc_auc_score(y_test, pred)
    }
    
    train_logger.debug(msg='Mlflow Start run and log params, metrics and figures')
    
    MODEL_PATH = Path(__file__).parent.parent/'models'/'model.pkl'
    with open(MODEL_PATH,'wb') as file:
        pickle.dump(model,file)
    
    mlrun_dir = Path(__file__).parent.parent / 'mlruns'
    mlrun_dir.mkdir(parents=True, exist_ok=True)
    
    mlflow.set_tracking_uri(mlrun_dir)
    mlflow.set_experiment('Water_Potability')
    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_artifact(fig_path)  # Log the confusion matrix figure
        mlflow.sklearn.log_model(model, 'model')

# Example usage
if __name__ == "__main__":
    PARAM_PATH = Path(__file__).parent.parent/'params.yaml'
    with open(PARAM_PATH,'r') as file:
        model_params = yaml.safe_load(file)
    
    lgbm_params = model_params['model_parameter']
    # Train the model and log with MLflow
    processed = Path(__file__).parent.parent / 'data' / 'processed'
    train_path = processed/'train'/'preprocessed_train.csv'
    test_path = processed/'test'/ 'preprocessed_test.csv'
    train_model(params=lgbm_params,train_df= train_path,
                test_df= test_path)
