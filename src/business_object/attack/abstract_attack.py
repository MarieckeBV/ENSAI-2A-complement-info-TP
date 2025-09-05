from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    ###Constructor
    def __init__(self, power, name, description):
        self._power = power
        self._name = name
        self._description = description
    
    ###Method

    @abstractmethod
    def compute_damage(self, APkm, DPkm):
        pass

    @property
    def power(self):
        return self._power
    
    @property
    def name(self):
        return self._name


