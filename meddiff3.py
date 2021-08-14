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