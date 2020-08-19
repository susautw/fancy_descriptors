from typing import Any, Callable

from fancy_descriptors.method_descriptor_base import MethodDescriptor


class FakeDescriptor(MethodDescriptor):
    value: Any

    def __init__(self, method: Callable, value: Any):
        super().__init__(method)
        self.value = value

    def get_value(self):
        return self.value
