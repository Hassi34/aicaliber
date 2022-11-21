from src.aicaliber.tabular.classification.model import Experiment
import tabularConfig

def training(config):
    exp = Experiment(config)
    exp.run_experiment()

if __name__ == "__main__":
    training(tabularConfig)