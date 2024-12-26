import mlflow
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent/'mlruns'
MODEL_PATH = ROOT_DIR / '407811645975662891'/'110384e44ff24f5287c5e5515b185e88'/'artifacts'/'model'

def load_model(df,model=MODEL_PATH):
    loaded_model = mlflow.pyfunc.load_model(model)
    predictiion = loaded_model.predict(df)
    return predictiion