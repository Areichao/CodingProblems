class FileSystem:

    def __init__(self):
        """ initalize the filepath system"""
        self.root = {} # nested like a Trie, {directory: {children}} or {file: ""}
        
    def ls(self, path: str) -> List[str]:
        """ returns filename or list of files in directory in lexicographic order """
        # O(n log n)
        if path == "/": 
            return sorted(self.root)
        # get to file path first
        node = self._getToDirectory(path)
        endName = path.rsplit("/", 1)[-1]
        # if file, just return the file name 
        if isinstance(node[endName], str):
            return [endName]
        # otherwise, return a sorted list of file and dir names
        return sorted(node[endName])
        

    def mkdir(self, path: str) -> None:
        """ new directory given a path. if intermediate directories dont exist, they should be created """

        node = self.root
        for folder in path.split("/")[1:]:
            # if folder is not in current keys, add and then 
            if folder not in node:
                node[folder] = {}
            # iterate to the folder
            node = node[folder]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        """ append content or create file with filepath """
        node = self._getToDirectory(filePath)
        fileName = filePath.rsplit("/", 1)[-1]
        # after iteration, check if filePath exists inside this folder.
        if fileName in node:
            # append content into the current file
            node[fileName] += content
        else:
            # create a new instance in the trie
            node[fileName] = content


    def readContentFromFile(self, filePath: str) -> str:
        """ returns content of file inside filePath """
        node = self._getToDirectory(filePath)
        fileName = filePath.rsplit("/", 1)[-1]
        # return all contents inside the file
        return node[fileName]
    

    def _getToDirectory(self, path: str) -> dict:
        """ returns the inside of a file given the path """
        # get to the end of the directory 
        node = self.root
        for folder in path.split("/")[1:-1]:
            node = node[folder]
        return node
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)