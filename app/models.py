from sqlalchemy import Column,String, Date,text,TIMESTAMP
from app.database import Base


class BogieCheckSheet(Base):
    __tablename__="BogieCheckSheet"
    adjustingTube               = Column(String,nullable=False)
    cylinderBody                = Column(String,nullable=False)
    pistonTrunnion              = Column(String,nullable=False)
    plungerSpring               = Column(String,nullable=False)
    axleGuide                   = Column(String,nullable=False)
    bogieFrameCondition         = Column(String,nullable=False)
    bolster                     = Column(String,nullable=False)
    bolsterSuspensionBracket    = Column(String,nullable=False)
    lowerSpringSeat             = Column(String,nullable=False)
    bogieNo                     = Column(String,nullable=False)
    dateOfIOH                   = Column(Date  ,nullable=False,server_default=text("CURRENT_DATE"))
    deficitComponents           = Column(String,nullable=False)
    incomingDivAndDate          = Column(String,nullable=False)
    makerYearBuilt              = Column(String,nullable=False)
    formNumber                  = Column(String,primary_key=True,nullable=False)
    submittedBy                 = Column(String, nullable=False)
    submittedDate               = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))


class WheelSpecifications(Base):
    __tablename__="WheelSpecifications"

    axleBoxHousingBoreDia       = Column(String,nullable=False)
    bearingSeatDiameter         = Column(String,nullable=False)
    condemningDia               = Column(String,nullable=False)
    intermediateWWP             = Column(String,nullable=False)
    lastShopIssueSize           = Column(String,nullable=False)
    rollerBearingBoreDia        = Column(String,nullable=False)
    rollerBearingOuterDia       = Column(String,nullable=False)
    rollerBearingWidth          = Column(String,nullable=False)
    treadDiameterNew            = Column(String,nullable=False)
    variationSameAxle           = Column(String,nullable=False)
    variationSameBogie          = Column(String,nullable=False)
    variationSameCoach          = Column(String,nullable=False)
    wheelDiscWidth              = Column(String,nullable=False)
    wheelGauge                  = Column(String,nullable=False)
    wheelProfile                = Column(String,nullable=False)
    formNumber                  = Column(String,primary_key=True,nullable=False)
    submittedBy                 = Column(String,nullable=False)
    submittedDate               = Column(Date  ,nullable=False,server_default=text("CURRENT_DATE"))

class Inspectors(Base):
    __tablename__="Inspectors"
    user_id=Column(String,primary_key=True,nullable=False)
    created_At=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
