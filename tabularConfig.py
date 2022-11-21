##Training Configuration
#params
data_dir = "tabular_data"
csv_file_name = "diabetes.csv"
task = "classification"
target_column = "Outcome"
autopilot = False
metrics = 'accuracy' # available_selections = ['accuracy', 'f1_score', 'recall', 'precision']
validation_split = 0.20
scaler = "StandardScaler"
imputer = "SimpleImputer"
PloyNomialFeatures = False
handle_imbalance = False 
pca = True

# Artifacts (Directory names to store the artifacts, can be customized according to the user requirements)
artifacts_dir = "Artifacts"
model_dir = "Models"
plots_dir = "Plots"
model_name = "my_test_model"
experiment_name = "light model testing"
plot_name = "results_plot"
model_ckpt_dir = "Model Checkpoints"
callbacked_model_name = "model_ckpt"

#logs (Directory names to record logs, can be customized according to the user requirements):
logs_dir = "Logs"
tensorboard_root_log_dir = "Tensorboard Logs"
csv_logs_dir = "CSV Logs"
csv_logs_file = "cv_test_logs.csv"
comments = "making comparision for optimizers"
executed_by = 'hasnain'