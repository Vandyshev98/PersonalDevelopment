# -*- coding: utf-8 -*-
import json
from collections import namedtuple


# data = '{"1-я неделя": {"Программирование": "13", "Универ": "9"}, "2-я неделя": {"Программирование": "10", "Универ": "18"}}'
#
# x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
# print(x.name, x.hometown.name, x.hometown.id)

class UserData:
    def __init__(self, weeks):
        self.weeks = weeks

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

weeks = dict()
labels = dict()
labels["Prog"] = 12
labels["fam"] = 13
weeks[1] = labels
ud = UserData(weeks=weeks)

print(ud)
print(ud.to_json())
print(UserData.from_json(ud.to_json()))

