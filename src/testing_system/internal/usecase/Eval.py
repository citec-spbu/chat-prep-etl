from testing_system.internal.domain.entities import \
    Answer, Experiment, Question


class Eval:
    """The measurer of the experiment"""
    def __init__(self):
        self.judge = None #TODO

    def execute(self, q: Question, a: Answer) -> Experiment:
        """
        The evaluation method
        input: Question, Answer
        output: List[MetricValue] 

        check all the entities in the
        testing_system/internal/domain/entities.py
        """
        
        raise NotImplementedError