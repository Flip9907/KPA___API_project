from fastapi import APIRouter,status,Depends,HTTPException
from app.database import get_db
from app.schema import InspectionData,WheelInspectionForm,Enquiry_form
from sqlalchemy.orm import Session
from app import models
from typing import List
from app.utils import reshape_flat_record,reshape_wheel_record
router=APIRouter(prefix="/api/forms")

@router.get("/bogie-checksheet/",response_model=List[InspectionData],status_code=status.HTTP_200_OK)
def get_bogie_checksheet(data:Enquiry_form=Depends(),db:Session=Depends(get_db),):
    if not (data.formNumber and data.submittedBy and data.submittedDate):
        raise HTTPException(
            status_code=400,
            detail="All fields (formNumber, submittedBy, submittedDate) are required."
        )

    result = db.query(models.BogieCheckSheet).filter(
        models.BogieCheckSheet.formNumber == data.formNumber,
        models.BogieCheckSheet.submittedBy == data.submittedBy,
        models.BogieCheckSheet.submittedDate == data.submittedDate
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail="No matching forms found")
    return [reshape_flat_record(result)]

@router.get("/wheel-specification/",response_model=List[WheelInspectionForm],status_code=status.HTTP_200_OK)
def get_wheel_specifications(data: Enquiry_form=Depends(),db:Session=Depends((get_db))):
    if not (data.formNumber and data.submittedBy and data.submittedDate):
        raise HTTPException(
            status_code=400,
            detail="All fields (formNumber, submittedBy, submittedDate) are required."
        )

    result = db.query(models.WheelSpecifications).filter(
        models.WheelSpecifications.formNumber == data.formNumber,
        models.WheelSpecifications.submittedBy == data.submittedBy,
        models.WheelSpecifications.submittedDate == data.submittedDate
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail="No matching forms found")
    print(result)
    return [reshape_wheel_record(result)]
