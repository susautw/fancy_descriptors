from typing import Callable

from method_descriptors import MethodDescriptorBase

from method_descriptor_factories import MethodDescriptorFactoryBase, NonThreadSafeMethodDescriptorFactory


class MethodDescriptor(MethodDescriptorBase):
    trueInstance: MethodDescriptorBase

    def __init__(self, method: Callable, factory: MethodDescriptorFactoryBase = None):
        if factory is None:
            # default factory
            factory = NonThreadSafeMethodDescriptorFactory()
        self.trueInstance = factory.create(method)

    def __call__(self, *args, **kwargs):
        return self.trueInstance.__call__(*args, **kwargs)

    def __get__(self, instance, owner):
        return self.trueInstance.__get__(instance, owner)

    def clone(self):
        return self.trueInstance.clone()
