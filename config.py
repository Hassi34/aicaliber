
data_dir = "data_folder"
train_folder_name = "train"
val_folder_name = "val"
transfer_learning = True
model_architecture = "VGG16"
freeze_all = True
freeze_till = -1
augmentation = True
epochs = 1
batch_size = 32
input_shape = (224, 224, 3)
activation = "relu"
activation_output = "softmax"
loss_function = "binary_crossentropy"
metrics = "accuracy"
optimizer = "Adam" 
validation_split = 0.20
es_patience = 5

#artifacts:
artifacts_dir = "Artifacts"
model_dir = "Models"
plots_dir = "Plots"
model_name = "my_test_model"
experiment_name = "Test exp with def"
plot_name = "results_plot"
model_ckpt_dir = "Model Checkpoints"
callbacked_model_name = "model_ckpt"

#logs:
logs_dir = "Logs"
general_logs = "General Logs"
tensorboard_root_log_dir = "Tensorboard Logs"
csv_logs_dir = "CSV Logs"
csv_logs_file = "cv_test_logs.csv"
comments = "this is comments"
executed_by = 'hassii'