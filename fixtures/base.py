import json


class Base:
    """
    Содержит общие методы для остальных классов:
    - Class Register.
    """

    def obj_to_dict(self) -> dict:
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
