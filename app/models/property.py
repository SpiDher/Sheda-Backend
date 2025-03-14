from core.database import Base
from sqlalchemy import (String,
                        Boolean,
                        Float,
                        Enum,
                        DateTime,
                        ForeignKey,
                        CheckConstraint,
                        Integer,
                        )
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import datetime
from app.utils.enums import PropertyStatEnum,PropertyTypeEnum,AppointmentStatEnum


class Property(Base):
    __tablename__ = 'property'
    id: Mapped[int]= mapped_column('id',primary_key=True,autoincrement=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('user.id',ondelete='CASCADE'),nullable=False,)
    title:Mapped[str]=mapped_column(String(100),nullable=False,)
    description:Mapped[str]=mapped_column(String,nullable=True,)
    price:Mapped[float]=mapped_column(Float,nullable=False,)
    is_negotiable:Mapped[bool]=mapped_column(Boolean,nullable=True,default=False)
    location:Mapped[str]=mapped_column(String(70),nullable=False,)
    property_type:Mapped[PropertyTypeEnum]=mapped_column(Enum(PropertyTypeEnum),nullable=False,default=PropertyTypeEnum.apartment)
    status:Mapped[PropertyStatEnum]= mapped_column(Enum(PropertyStatEnum),nullable=False,default=PropertyStatEnum.rent)
    furnished:Mapped[bool]=mapped_column(Boolean,default=False,)
    is_active:Mapped[bool] = mapped_column(Boolean,default= True,)
    created_at: Mapped[datetime]= mapped_column(DateTime,default=datetime.now,)
    updated_at:Mapped[datetime]= mapped_column(DateTime,default=datetime.now,onupdate=datetime.now,)
    bathroom:Mapped[int]=mapped_column(Integer,nullable=False,)
    bedroom:Mapped[int]=mapped_column(Integer,nullable=False,)
    air_condition:Mapped[bool]=mapped_column(Boolean,default=False,)
    pop_ceiling:Mapped[bool]=mapped_column(Boolean,default=False,)
    floor_tiles:Mapped[bool]=mapped_column(Boolean,default=False,)
    running_water:Mapped[bool]=mapped_column(Boolean,default=False,)    
    furniture:Mapped[bool]=mapped_column(Boolean,default=False,)
    prepaid_meter:Mapped[bool]=mapped_column(Boolean,default=False,)
    wifi:Mapped[bool]=mapped_column(Boolean,default=False,)
    
    #NOTE - Relationships
    agent = relationship('Agent', back_populates='listings',lazy='selectin')
    images = relationship('PropertyImage',back_populates='property',cascade='all, delete-orphan',lazy='selectin')
    client = relationship('Client',back_populates = 'properties')
    
    __table_args__ = (
        CheckConstraint(
            f"property_type IN {tuple(item.value for item in PropertyTypeEnum)}",
            name="check_property_type"
        ),
        CheckConstraint(
            f"status IN {tuple(item.value for item in PropertyStatEnum)}",
            name="check_status"
        ),
    )
    
class PropertyImage(Base):
    __tablename__ = 'property_image'
    id:Mapped[int] = mapped_column('id',autoincrement=True,primary_key=True)
    property_id:Mapped[int] = mapped_column(Integer,ForeignKey('property.id',ondelete='CASCADE'),nullable=False)  
    image_url: Mapped[str] = mapped_column(String(255),nullable=False,)
    is_primary:Mapped[bool] = mapped_column(Boolean,nullable=True,default=False)
    property = relationship('Property',back_populates='images')

class Appointment(Base):
    __tablename__ = "appointment"

    id:Mapped[int] = mapped_column('id', primary_key=True,autoincrement=True)
    client_id:Mapped[int] = mapped_column(Integer, ForeignKey("client.id",ondelete='CASCADE'), nullable=False)
    agent_id:Mapped[int] = mapped_column(Integer, ForeignKey("agent.id",ondelete='CASCADE'), nullable=False)
    property_id:Mapped[int] = mapped_column(Integer, ForeignKey("property.id"), nullable=False)
    scheduled_at:Mapped[datetime] = mapped_column(DateTime, nullable=False)  #NOTE Date/Time of appointment
    status:Mapped[AppointmentStatEnum] = mapped_column(Enum(AppointmentStatEnum), default=AppointmentStatEnum.pending)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at:Mapped[datetime] = mapped_column(DateTime,default = datetime.now,onupdate=datetime.now)
    client = relationship("Client", back_populates="appointments")


      