words = """
A dictionary is an unordered collection which stores key–value pairs that map immutable keys to values, just as a conventional dictionary maps words to definitions.
Dictionaries can contain objects of any types; and they support nesting
fetched by key (instead of position as in list). You create dictionaries with literals and access items by key. uses Key-Value pairs
Each key can have one associated value
In contrast with lists that sequentially number each item (the index), dictionaries allow you to name each item
"""
d = dict()
for c in words:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
#Modify this code so that punctuations are skipped
