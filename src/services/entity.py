
from src.models.entity import Entity as EntityModel
from src.schemas.entity import EntityCreate, EntityUpdate
from .base import RepositoryDB

class RepositoryEntity(RepositoryDB[EntityModel, EntityCreate, EntityUpdate]):
    pass

entity_crud = RepositoryEntity(EntityModel)