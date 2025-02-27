from fastapi import APIRouter,UploadFile,File,HTTPException,status
from app.services.user_service import GetSellerAccount
from app.services.profile import upload_image,update_pfp,update_user
from core.dependecies import FileUploadException,DBSession
from app.schemas.property_schema import PropertyBase
from app.services.listing import create_property_listing
router = APIRouter(prefix='/property',tags=['Property'])

@router.post('/list-property',response_model=PropertyBase,description='Upload Property',status_code=status.HTTP_201_CREATED)
async def list_property(current_user:GetSellerAccount,payload:PropertyBase,db:DBSession):
    return await create_property_listing(current_user,payload,db)
    