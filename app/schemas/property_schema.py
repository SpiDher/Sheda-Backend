from pydantic import BaseModel,AnyUrl,Field
from typing import List,Union,Annotated,Optional
from app.utils.enums import PropertyStatEnum,PropertyTypeEnum

class PropertyImage(BaseModel):
    image_url:Annotated[Union[AnyUrl,str],Field(examples=['https://example/img/property.jpg'],max_length=255)]
    is_primary:Optional[bool] = False
    class Config:
        from_attributes = True

class PropertyBase(BaseModel):
    title:str
    description:str
    location:str
    price: float
    property_type:PropertyTypeEnum
    status:PropertyStatEnum
    furnished:bool
    is_active:bool
    bathroom:int
    bedroom:int
    air_condition:bool
    pop_ceiling:bool
    floor_tiles:bool
    running_water:bool
    furniture:bool
    prepaid_meter:bool
    wifi:bool
    is_negotiable:bool
    images:List[PropertyImage]
    
    class Config:
        from_attributes = True
        
class PropertyShow(PropertyBase):
    id:int
    user_id:int
    
    class Config:
        from_attributes = True
        
    
    class Config:
        from_attributes = True
        
class PropertyUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    location:Optional[str] = None
    price: Optional[float]= None
    property_type:Optional[PropertyTypeEnum]= None
    status:Optional[PropertyStatEnum] = None
    furnished:Optional[bool] = None
    is_active:Optional[bool] = None
    bathroom:Optional[int] = None
    bedroom:Optional[int] = None
    air_condition:Optional[bool] = None
    pop_ceiling:Optional[bool] = None
    floor_tiles:Optional[bool] = None
    running_water:Optional[bool] = None
    furniture:Optional[bool] = None
    prepaid_meter:Optional[bool] = None
    wifi:Optional[bool] = None
    is_negotiable:Optional[bool] = None
    images:Optional[List[PropertyImage]] = None
    
    class Config:
        from_attributes = True
        
class FilterParams(BaseModel):
    limit: Annotated[int,Field(description='The amount of listings to fetch',ge=10,default=20)]
    cursor:Annotated[int,Field(description='The Id of the last listing',ge=1,default=1)]

class PropertyFeed(BaseModel):
    data:List[PropertyShow]
    next_coursor:int|None
    
class DeleteProperty(BaseModel):
    message:str