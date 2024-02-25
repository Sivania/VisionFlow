import os
import importlib
from base_flow import BaseFlow

def load_actions():
    '''

    actions = {}
    directory = os.path.dirname(__file__)
    directories = os.listdir(directory)
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    print(directories)
    for subDirectory in directories:
        print("ccc", directory + "\\" +subDirectory)
        for filename in os.listdir(directory + "\\" +subDirectory):
            print("ddd", filename)
            if filename.endswith('.py') and not filename.startswith('_'):
                module_name = filename[:-3]
                # Construct the full module path relative to the directory
                full_module_name = f'.{subDirectory}.{module_name}'
                try:
                    # Import the module
                    module = importlib.import_module(full_module_name, module_name)
                    # Iterate over attributes of the module
                    for attribute_name in dir(module):
                        attribute = getattr(module, attribute_name)
                        # Check if attribute is a class and a subclass of BaseFlow
                        if isinstance(attribute, type) and issubclass(attribute, BaseFlow) and attribute is not BaseFlow:
                            # Instantiate the class and add to actions dictionary
                            actions[attribute_name] = attribute()
                except ModuleNotFoundError as e:
                    print(f"Failed to import module: {full_module_name}")
                    print(e)

    return actions
        '''
    return {"click", "hold"}

print(load_actions())