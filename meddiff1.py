def group_by_owners(files):
    result = {}
    for file, owner in files.items():  # use files.iteritems() on Python 2.x
        result[owner] = result.get(owner, []) + [file]  # you can use setdefault(), too
    return result

files = {
    'Input.txt': 'Stan',
    'Code.py': 'Randy',
    'Output.txt': 'Randy',
    'abc.txt' : 'stan',
    'yoyo.txt' : 'raksha'
}

print(group_by_owners(files))