from mlflow.tracking import MlflowClient

# Set the MLflow tracking URI
mlflow.set_tracking_uri("https://dagshub.com/sylashalderb/project_kalke.mlflow")

# Initialize the MLflow Client
client = MlflowClient()

# List registered models
models = client.list_registered_models()
for model in models:
    print(f"Model Name: {model.name}")