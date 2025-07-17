def flatten_nested_dict(data: dict) -> dict:
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flat.update(value)
        else:
            flat[key] = value
    return flat

jsons={
  "fields": {
    "axleBoxHousingBoreDia": "string",
    "bearingSeatDiameter": "string",
    "condemningDia": "string",
    "intermediateWWP": "string",
    "lastShopIssueSize": "string",
    "rollerBearingBoreDia": "string",
    "rollerBearingOuterDia": "string",
    "rollerBearingWidth": "string",
    "treadDiameterNew": "string",
    "variationSameAxle": "string",
    "variationSameBogie": "string",
    "variationSameCoach": "string",
    "wheelDiscWidth": "string",
    "wheelGauge": "string",
    "wheelProfile": "string"
  },
  "formNumber": "string",
  "submittedBy": "string",
  "submittedDate": "2025-07-15"
}
print(flatten_nested_dict(jsons))