import sys
import importlib
mod_name = 'math'
import fractions


# import mod_name


math = importlib.import_module(mod_name)
print('math' in sys.modules)
print(math.sqrt(9))

# finder + loader == importer

print(fractions.__spec__)
print(sys.meta_path)
print(importlib.util.find_spec('decimal'))
