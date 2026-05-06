from abc import ABC, abstractmethod
from typing import List
from testing_system.internal.domain.value_objects import \
    AssistantRequest, AssistantResponse, \
    RetrievalResponse, RetrievalRequest
from testing_system.internal.domain.entities import Experiment


class IAssistant(ABC):
    """Interface for AI Assistant implementations"""

    @abstractmethod
    def ask(self, request: AssistantRequest) -> AssistantResponse:
        """Sends request to assistant and returns responce"""
        pass

class IRetriever(ABC):
    """Interface for any database implementation"""

    @abstractmethod
    def retrieve(self, request: RetrievalRequest) -> RetrievalResponse:
        """Sends request to db and returns response with docs"""
        pass

class IRegistry(ABC):
    """Interface for versioning the experiments"""

    @abstractmethod
    def push(self, experiment: Experiment): #nothing to return or need smth?
        """Saves the experiment into registry"""
        pass

    @abstractmethod
    def check(self, experiment: Experiment) -> Experiment:
        """
        Checks the originality of the experiment`s configuration.
        not-None - exists, don`t repeat
        None - doesn`t exist, provide it and save
        """
        pass

    @abstractmethod
    def select(self, latest = None) -> List[Experiment]:
        """
        Export all the experiments from registry.
        latest: int for how many experiments to select, None for all
        """
        pass


class IExperimentLoader(ABC):
    """Interface for loading experiment descriptions into domain entities."""

    @abstractmethod
    def load(self, path: str) -> Experiment:
        """Loads an experiment from an external source."""
        pass
