import json


class Record:
    def __init__(self, timestamp, deaths, births):
        self.timestamp = timestamp
        self.deaths = deaths
        self.births = births

    # makes the Record object json serializable
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
