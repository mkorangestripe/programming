### Walk a dictionary and match UUIDs

pipeline_dev.json

```json
{
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
}
```

```python
import json
import re

PIPELINE_DEV = 'pipeline_dev.json'

re_uuid = re.compile("[0-F]{8}-([0-F]{4}-){3}[0-F]{12}", re.I)

with open(PIPELINE_DEV, encoding='utf-8') as open_pipeline_dev:
    pipeline_dev = json.load(open_pipeline_dev)

def walk_dict(iterobj):
    """Walk Dictionary"""

    if isinstance(iterobj, dict):
        for k in iterobj:
            walk_dict(iterobj[k])
    elif isinstance(iterobj, (list, tuple)):
        for i in iterobj:
            walk_dict(i)
    else:
        match = re_uuid.match(str(iterobj))
        if bool(match):
            print(iterobj)

walk_dict(pipeline_dev)
```

```
cdee37ba-8d76-456b-9e13-4d235bcf0b3d
d0cdf8b2-8cd8-4fb7-8461-2275a4d88104
938983bd-e7ca-4bd4-9134-a6e7d1dd9496
a76f720d-6ab3-4056-8c19-460f4b3cc30c
```
