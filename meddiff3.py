'''Write a function that provides a change directory (cd) function for an abstract file system.

Notes:
Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).
The function should support both relative and absolute paths.
The function will not be passed any invalid paths.
Do not use built-in path-related functions.

For example:
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

Output:
Should display '/a/b/c/x'.'''
class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        PREV = '..'
        DIV = '/'

        #c_list = ['', 'a', 'b', 'c', 'd']
        c_list = self.current_path.split(DIV)
        #n_list = ['..', 'x']
        n_list = new_path.split(DIV)

        for item in n_list:
            if item == PREV:
                #delete the last item in list
                del c_list[-1]
            else:
                c_list.append(item)
        #add "/" before each item in the list and printout as string                    
        self.current_path = "/".join(c_list)
        return self.current_path


path = Path('/a/b/c/d')
path.cd('../z')
print(path.current_path)
