from pydantic import BaseModel,Field
from datetime import date, datetime


class BmbcChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: date
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

class InspectionData(BaseModel):
    bmbcChecksheet: BmbcChecksheet
    bogieChecksheet: BogieChecksheet
    bogieDetails: BogieDetails
    formNumber: str
    submittedBy: str


class WheelFields(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile: str

class WheelInspectionForm(BaseModel):
    fields: WheelFields
    formNumber: str
    submittedBy: str

class Users(BaseModel):
    created_At:datetime

class Users_in(Users):
    user_id:str

    class Config:
        from_attributes:True

class Enquiry_form(BaseModel):
    formNumber: str = Field(..., description="Form number is required")
    submittedBy: str = Field(..., description="Submitted by is required")
    submittedDate: date = Field(..., description="Submitted date is required")