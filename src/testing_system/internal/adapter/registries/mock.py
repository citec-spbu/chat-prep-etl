from typing import List

from testing_system.internal.domain.entities import Experiment
from testing_system.internal.domain.interfaces import IRegistry


class MockRegistry(IRegistry):
    def __init__(self):
        self.DB = None
    def push(self, experiment: Experiment):
        return
    def check(self, experiment: Experiment) -> Experiment:
        return None
    def select(self, latest = None) -> List[Experiment]:
        return []