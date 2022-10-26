import json
import string
import random
import requests
from growthbook import GrowthBook

# Fetch feature definitions from GrowthBook API
# In production, we recommend adding a db or cache layer
apiResp = requests.get("hello world")
features = apiResp.json()["features"]

# print(json.dumps(features, indent=4))

letters = string.ascii_lowercase
user_id = "".join(random.choice(letters) for i in range(10))

# # TODO: Real user attributes
attributes = {
    "id": user_id,
    # "id": "x",
}

# # Tracking callback when someone is put in an experiment
def on_experiment_viewed(experiment, result):
    # Use whatever event tracking system you want
    print({"experimentId": experiment.key, "variationId": result.variationId})
    print(result.to_dict())


# # Create a GrowthBook instance
gb = GrowthBook(
    enabled=True,
    attributes=attributes,
    features=features,
    trackingCallback=on_experiment_viewed,
    qaMode=False,
)

# ?: Use a feature

# ?: Boolean
if gb.isOn("search-feature-1"):
    print("Feature is enabled!")
    # print(gb.getFeatureValue("search-feature-1", "x"))

# ?: String, JSON or Number
color = gb.getFeatureValue("search-feature-1", "x")
print(color)

# ?: Also use evalFeature to get the full object stream
obj = gb.evalFeature("search-feature-1")
print(obj.to_dict())
