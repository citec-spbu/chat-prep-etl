from pathlib import Path
from typing import List
from testing_system.internal.domain.entities import Experiment
from testing_system.internal.domain.interfaces import IExperimentLoader


class Loader:
    """The experiment-loader usecase"""
    
    def __init__(self, loader: IExperimentLoader):
        self.loader = loader

    def execute(self, path_to_experiments: str) -> List[Experiment]:
        experiments = []
        folder_path = Path(path_to_experiments)

        if not folder_path.exists():
            raise FileNotFoundError
        if not folder_path.is_dir():
            raise NotADirectoryError
        for file in folder_path.rglob('*.y*ml'): #it is not good to be here, it must be in Yaml loader
            if file.is_file():
                experiments.append(self.loader.load(file))
                
        return experiments