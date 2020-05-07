from pathlib import Path
import json
class Config(object):
    def __init__(self, graphPath):
        self.graphPath = graphPath

def as_config(dict):
    return Config(
        dict['graphPath'],
    )

configuration = json.loads(Path("configuration.json").read_text(), object_hook = as_config)