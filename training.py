from TensorFlow.CV.model import Experiment
import config

def training(config):
    exp = Experiment(config)
    exp.run_experiment()

if __name__ == "__main__":
    training(config)