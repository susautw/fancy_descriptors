from typing import Callable

from method_descriptor_factories import MethodDescriptorFactoryBase
from method_descriptors import MethodDescriptor, NonThreadSafeMethodDescriptor, ThreadSafeMethodDescriptor


class NonThreadSafeMethodDescriptorFactory(MethodDescriptorFactoryBase):
    def create(self, method: Callable) -> MethodDescriptor:
        return NonThreadSafeMethodDescriptor(method)


class ThreadSafeMethodDescriptorFactory(MethodDescriptorFactoryBase):
    def create(self, method: Callable) -> MethodDescriptor:
        return ThreadSafeMethodDescriptor(method)
