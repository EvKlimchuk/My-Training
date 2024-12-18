import inspect
from pprint import pprint




def introspection_info(obj):
    result = {'type': type(obj), 'attributes':[], 'methods':[],
              'module': inspect.getmodule(obj) if inspect.getmodule(obj) else 'built-in'}

    for attr in dir(obj):
        if not attr.startswith('__'):
            attribute = getattr(obj, attr)

            if inspect.ismethod(attribute) or inspect.isfunction(attribute):
                result ['methods'].append(attr)
            else:
                result ['attributes'].append(attr)
    return result

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        return f'Example method called with value {self.value}'

number_info = introspection_info(42)
string_info = introspection_info('Hello')
list_info = introspection_info([1,2,3])
example_object = ExampleClass(10)
custom_class_info = introspection_info(example_object)

print("Introspection for integer:")
pprint(number_info)
print('\nIntrospection for string')
pprint(string_info)
print('\nIntrospection for list:')
pprint(list_info)
print('\nIntrospection for custom class object:')
pprint(custom_class_info)