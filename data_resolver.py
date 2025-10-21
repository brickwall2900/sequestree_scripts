import os

class DataResolver:
    def __init__(self, backend):
        self._backend = backend
        pass

    def resolve_file(self, filename):
        return self._backend.resolve_file(filename)

class LocalDataResolver:
    def __init__(self):
        try:
            self._baseDir = os.environ["_Sequestree_LocalDataResolverPath"]
        except:
            raise ValueError("No _Sequestree_LocalDataResolverPath environment variable! Please set up _Sequestree_LocalDataResolverPath to a path in disk.")

    def resolve_file(self, filename):
        file_path = self._baseDir + "/" + filename
        return file_path

class RemoteDataResolver:
    def __init__(self):
        try:
            self._remoteUrl = os.environ["_Sequestree_RemoteDataResolverURL"]
        except:
            raise ValueError("No _Sequestree_RemoteDataResolverURL environment variable! Please set up _Sequestree_RemoteDataResolverURL to a URL.")

    def resolve_file(self, filename):
        path = self._remoteUrl + filename
        return path