from abc import ABC, abstractmethod
from typing import Callable

from method_descriptors import MethodDescriptor


class MethodDescriptorFactoryBase(ABC):

    @abstractmethod
    def create(self, method: Callable) -> MethodDescriptor:
        pass
