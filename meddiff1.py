'''Implement a group_by_owners function that:

·         Accepts a dictionary containing the file owner name for each file name.

·         Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

 '''
def group_by_owners(files):
    result = {}
    for file, owner in files.items():  
        result[owner] = result.get(owner, []) + [file]  
    return result

files = {
    'Input.txt': 'Stan',
    'Code.py': 'Randy',
    'Output.txt': 'Randy',
    'abc.txt' : 'stan',
    'yoyo.txt' : 'raksha'
}

print(group_by_owners(files))
