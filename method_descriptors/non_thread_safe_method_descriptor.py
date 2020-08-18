from copy import copy
from typing import Callable

from method_descriptors import MethodDescriptorBase


class NonThreadSafeMethodDescriptor(MethodDescriptorBase):

    def __init__(self, method: Callable):
        if not isinstance(method, Callable):
            raise TypeError('method must be a Callable.')
        self.method = method
        self.instance = None
        self.owner = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            raise RuntimeError('method must bind to an instance first.')
        return self._get_method_of_instance()(*args, **kwargs)

    def _get_method_of_instance(self):
        return self.method.__get__(self.instance, self.owner)

    def __get__(self, instance, owner=None):
        self.instance = instance
        self.owner = owner
        new_instance = self.clone()

        return new_instance

    def clone(self):
        return copy(self)

