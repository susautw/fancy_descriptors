import inspect
from abc import ABC, abstractmethod
from typing import Callable


class MethodDescriptorBase(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        MethodDescriptors must implement __call__ because the class is  a wrapper of a method
        , it makes the class become a Callable
        """
        pass

    @abstractmethod
    def __get__(self, instance, owner):
        pass

    @classmethod
    def get_instance_methods(cls, instance):
        """
        Get all marked methods of an instance with this descriptor.
        :param instance:
        :return: methods
        """
        return {
            method_name: method for method_name, method in inspect.getmembers(instance) if isinstance(method, cls)
        }

