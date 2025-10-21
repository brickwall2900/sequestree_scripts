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
        file_path = BASE_DIR + "/" + filename
        return file_path
    
try:
    REMOTE_URL = os.environ["_Sequestree_RemoteDataResolverURL"]
except:
    raise ValueError("No _Sequestree_RemoteDataResolverURL environment variable! Please set up _Sequestree_RemoteDataResolverURL to a URL.")
class RemoteDataResolver:
    def resolve_file(self, filename):
        path = REMOTE_URL + filename
        return path