"""Walk a dictionary and match on uuid patterns."""

import json
import re

pipeline_dev = '''{
 "triggers": [
  {
   "enabled": true,
   "expectedArtifactIds": [
    "cdee37ba-8d76-456b-9e13-4d235bcf0b3d",
    "d0cdf8b2-8cd8-4fb7-8461-2275a4d88104",
    "938983bd-e7ca-4bd4-9134-a6e7d1dd9496"
   ],
   "payloadConstraints": {
    "app": "analyticscollector-develop",
    "appid": "a76f720d-6ab3-4056-8c19-460f4b3cc30c"
   },
   "runAsUser": "jenkins@some-domain.com",
   "source": "analyticscollector-develop",
   "type": "webhook"
  }
 ]
}'''

re_uuid = re.compile("[0-F]{8}-([0-F]{4}-){3}[0-F]{12}", re.I)

pipeline = json.loads(pipeline_dev)

def walk_dict(iterobj):
    if isinstance(iterobj, dict):
        for k in iterobj:
            walk_dict(iterobj[k])
    elif isinstance(iterobj, list) or isinstance(iterobj, tuple):
        for i in iterobj:
            walk_dict(i)
    else:
        match = re_uuid.match(str(iterobj))
        if bool(match):
            print iterobj

walk_dict(pipeline)

# Output
# cdee37ba-8d76-456b-9e13-4d235bcf0b3d
# d0cdf8b2-8cd8-4fb7-8461-2275a4d88104
# 938983bd-e7ca-4bd4-9134-a6e7d1dd9496
# a76f720d-6ab3-4056-8c19-460f4b3cc30c
