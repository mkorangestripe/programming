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

def walk_dict(htable, regex):
    """Walk dictionary and match regex"""

    if isinstance(htable, dict):
        for k in htable:
            walk_dict(htable[k], regex)
    elif isinstance(htable, (list, tuple)):
        for i in htable:
            walk_dict(i, regex)
    else:
        match = regex.match(str(htable))
        if bool(match):
            print(htable)

walk_dict(pipeline_dev, re_uuid)
```

```
cdee37ba-8d76-456b-9e13-4d235bcf0b3d
d0cdf8b2-8cd8-4fb7-8461-2275a4d88104
938983bd-e7ca-4bd4-9134-a6e7d1dd9496
a76f720d-6ab3-4056-8c19-460f4b3cc30c
```
