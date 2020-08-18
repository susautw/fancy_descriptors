from asyncio import Lock
from typing import Callable

from method_descriptors import NonThreadSafeMethodDescriptor


class ThreadSafeMethodDescriptor(NonThreadSafeMethodDescriptor):
    def __init__(self, method: Callable):
        super().__init__(method)
        self.lock = Lock()

    def _get_method_of_instance(self):
        with self.lock:
            return super(ThreadSafeMethodDescriptor, self)._get_method_of_instance()

    def __get__(self, instance, owner=None):
        with self.lock:
            new_instance = super(ThreadSafeMethodDescriptor, self).__get__(instance, owner)
        return new_instance

    def clone(self):
        new_instance = super(ThreadSafeMethodDescriptor, self).clone()
        new_instance.lock = Lock()
        return new_instance
