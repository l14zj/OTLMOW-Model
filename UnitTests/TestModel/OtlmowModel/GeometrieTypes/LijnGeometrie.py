from abc import abstractmethod
from ..GeometrieTypes.AbstracteGeometrie import AbstracteGeometrie


class LijnGeometrie(AbstracteGeometrie):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self._geometry_types.append('LINESTRING Z')
