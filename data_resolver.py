import os

class DataResolver:
    def __init__(self, backend):
        self._backend = backend
        pass

    def resolve_file(self, filename):
        return self._backend.resolve_file(filename)
    
try:
    BASE_DIR = os.environ["_Sequestree_LocalDataResolverPath"]
except:
    raise ValueError("No _Sequestree_LocalDataResolverPath environment variable! Please set up _Sequestree_LocalDataResolverPath to a path in disk.")

class LocalDataResolver:
    def resolve_file(self, filename):
        # Our working directory is...
        # F:\UserData\sequestree\sequestree_database
        # here!

        file_path = BASE_DIR + "/" + filename
        return file_path