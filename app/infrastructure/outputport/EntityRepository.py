from typing import TypeVar, Generic, Optional, List
from abc import abstractmethod


# Type definition for Model
M = TypeVar("M")
# Type definition for Unique Id
K = TypeVar("K")

class EntityRepository(Generic[M, K]):
    # Fech an existing instance of the Model by it's unique Id
    @abstractmethod
    def getById(self, instance: M, id: K) -> M:
        pass
     # Filter all existing instance of the Model
    @abstractmethod
    def filter(self, instance: M,
               filterBy: Optional[dict],
               limit: Optional[int],
               start: Optional[int]) -> List[M]:
        pass
    # Create a new instance of the Model
    @abstractmethod
    def create(self, instance: M) -> M:
        pass
    # Updates an existing instance of the Model
    @abstractmethod
    def update(self, id: K, instance: M) -> M:
        pass
    # Delete an existing instance of the Model
    @abstractmethod
    def delete(self, id: K) -> None:
        pass

    @abstractmethod
    def computedOperator(self, column, v):
        pass


