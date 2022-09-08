import time
import yaml
import tensorflow as tf

def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)
    return content

def get_unique_filename(filename, is_model_name = False):
    if is_model_name:
        time_stamp = time.strftime("_on_%Y%m%d_at_%H%M%S_.h5")
    else :
        time_stamp = time.strftime("_on_%Y%m%d_at_%H%M%S")
    unique_filename  = f"{filename}_{time_stamp}"
    return unique_filename
def set_memory_growth():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)