from app import models
from app.schema import WheelFields

BMB_CHECK_FIELDS = {"adjustingTube", "cylinderBody", "pistonTrunnion", "plungerSpring"}
BOGIE_CHECK_FIELDS = {"axleGuide", "bogieFrameCondition", "bolster", "bolsterSuspensionBracket", "lowerSpringSeat"}
BOGIE_DETAIL_FIELDS = {"bogieNo", "dateOfIOH", "deficitComponents", "incomingDivAndDate", "makerYearBuilt"}

def reshape_flat_record(record: models.BogieCheckSheet) -> dict:
    data = record.__dict__.copy()
    data.pop("_sa_instance_state", None)

    bmbc = {k: data.pop(k) for k in BMB_CHECK_FIELDS if k in data}
    bogie_check = {k: data.pop(k) for k in BOGIE_CHECK_FIELDS if k in data}
    bogie_details = {k: data.pop(k) for k in BOGIE_DETAIL_FIELDS if k in data}

    return {
        "formNumber": data.get("formNumber"),
        "submittedBy": data.get("submittedBy"),  # mapped key
        "submittedDate": data.get("submittedDate"),
        "bmbcChecksheet": bmbc,
        "bogieChecksheet": bogie_check,
        "bogieDetails": bogie_details,
    }



def reshape_wheel_record(record: models.WheelSpecifications) -> dict:
    data = record.__dict__.copy()
    data.pop("_sa_instance_state", None)

    wheel_fields = {
        key:data.pop(key)
        for key in WheelFields.model_fields.keys()
        if key in data
    }

    return {
        "formNumber": data.get("formNumber"),
        "submittedBy": data.get("submittedBy"),
        "submittedDate": data.get("submittedDate"),
        "fields": wheel_fields,
    }

def flatten_nested_dict(data: dict) -> dict:
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flat.update(value)
        else:
            flat[key] = value
    return flat
