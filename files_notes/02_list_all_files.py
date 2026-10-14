import os
from glob import glob
result = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*.py'))]
for index, item in enumerate(result):
    print(index, item)
