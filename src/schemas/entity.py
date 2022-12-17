from typing import Optional
from datetime import datetime

from pydantic import BaseModel

# Shared properties
# EntityBase-схема описывает то, что мы ожидаем получить при создании и
# обновлении элементов пользовательским вводом: например, наименование объекта в базе данных.
class EntityBase(BaseModel):
    title: str

# Properties to receive on entity creation
class EntityCreate(EntityBase):
    pass

# Properties to receive on entity update
class EntityUpdate(EntityBase):
    pass

# Properties shared by models stored in DB
# EntityInDBBase — результат выполнения методов. Это то, что мы будем
# отдавать пользователю — детальную информацию по нужным полям модели.
class EntityInDBBase(EntityBase):
    id: int
    title: str
    created_at: datetime

    class Config:
        orm_mode = True

# Properties to return to client
class Entity(EntityInDBBase):
    pass

# Properties stored in DB

class EntityInDB(EntityInDBBase):
    pass