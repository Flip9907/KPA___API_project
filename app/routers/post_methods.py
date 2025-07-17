from fastapi import APIRouter,status,Depends,HTTPException
from app.database import get_db
from app.schema import InspectionData,WheelInspectionForm,Users_in
from sqlalchemy.orm import Session
from app import models
from app.utils import flatten_nested_dict
router=APIRouter(prefix="/api/forms")

@router.post("/bogie-checksheet/",status_code=status.HTTP_201_CREATED)
def submit_inspection(data:InspectionData,db:Session=Depends(get_db),):
    existing_form = db.query(models.BogieCheckSheet).filter_by(formNumber=data.formNumber).first()

    if existing_form:
        raise HTTPException(
            status_code=400,
            detail=f"Form with formNumber '{data.formNumber}' already exists."
        )

    new_data=flatten_nested_dict(data.model_dump())
    new_form= models.BogieCheckSheet(**new_data)

    db.add(new_form)
    db.commit()
    db.refresh(new_form)

    return {"status": "received"}

@router.post("/wheel-specification/",status_code=status.HTTP_201_CREATED)
def submit_wheel(data: WheelInspectionForm,db:Session=Depends((get_db))):

    existing_form=db.query(models.WheelSpecifications).filter_by(formNumber=data.formNumber).first()

    if existing_form:
        raise HTTPException(
            status_code=400,
            detail=f"Form with formNumber '{data.formNumber}' already exists."
        )

    new_data=flatten_nested_dict(data.model_dump())
    new_form= models.WheelSpecifications(**new_data)
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return {"status": "well received"}

@router.post("/create_user")
def create_user(data:Users_in,db:Session=Depends(get_db)):
    new_data= models.Inspectors(**data.model_dump())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
