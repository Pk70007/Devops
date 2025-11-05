import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://<EC2-IP>:5000")
mlflow.set_experiment("App_Model_Tracking")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.sklearn.log_model(model, "model")
