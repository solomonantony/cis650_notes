xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}
zs = {}
print(zs)
zs.update(xs)
print(zs)
zs.update(ys)
print(zs)
import json
print(json.dumps(zs, indent=4, sort_keys = True))
