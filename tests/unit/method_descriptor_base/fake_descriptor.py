from typing import Any, Callable

from fancy_descriptors.method_descriptor_base import MethodDescriptor
from fancy_descriptors.method_descriptor_factories import MethodDescriptorFactoryBase


class FakeDescriptor(MethodDescriptor):
    value: Any

    def __init__(self, method: Callable, value: Any, factory: MethodDescriptorFactoryBase = None):
        super().__init__(method, factory=factory)
        self.value = value

    def get_value(self):
        return self.value
