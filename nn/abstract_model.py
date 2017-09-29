from abc import ABCMeta, abstractmethod
from utils.util import describe


class Model:
    __metaclass__ = ABCMeta

    def __init__(self, feature_input, seq_lengths, mode, num_classes, settings=None):
        self.input = feature_input
        self.seq_lengths = seq_lengths
        self.mode = mode,
        self.num_classes = num_classes
        self.settings = settings

    @describe
    @abstractmethod
    def build_graph(self):
        pass
