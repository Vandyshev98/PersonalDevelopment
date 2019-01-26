from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import transaction
import json

from .. import models


@view_config(route_name='radar_example', renderer='../templates/radar_example.jinja2')
def radar_example(request):
    datasets = """[{"label":"2-я неделя","data":[8,15,10,8,4,2],"fill":true,"backgroundColor":"rgba(255, 99, 132, 0.2)","borderColor":"rgba(255,99,132,1)","borderWidth":2},{"label":"1-я неделя","data":[6,12,10,9,6,5],"fill":true,"backgroundColor":"rgba(54, 162, 235, 0.2)","borderColor":"rgba(54, 162, 235, 1)","borderWidth":2}]"""
    return {"datasets": datasets, "user_id": ""}


@view_config(route_name='statistics', renderer='../templates/statistics.jinja2')
def statistics(request):
    user = request.user
    if request.user is None:
        return HTTPFound(location="login")

    db_data = request.dbsession.query(models.Data).filter(models.Data.user_login == user.login).first()
    if not db_data:
        return HTTPFound(location="user_main")

    data = UserData.from_json(db_data.data)
    if not data.labels:
        return HTTPFound(location="add_data")
    print(data.labels.__repr__)
    print(type(data.labels.__repr__))
    print()
    print(type(data.datasets))

    return {'datasets': json.dumps(data.datasets), 'labels': json.dumps(data.labels)}


@view_config(route_name='create_directions', renderer='../templates/create_directions.jinja2')
def add_directions(request):
    user = request.user
    if user is None:
        return HTTPFound(location="login")

    if (request.POST is not None) & (len(request.POST) > 0):
        directions = list()
        directions.append(request.params.get('1'))
        directions.append(request.params.get('2'))
        directions.append(request.params.get('3'))
        directions.append(request.params.get('4'))
        directions.append(request.params.get('5'))
        directions.append(request.params.get('6'))
        directions.append(request.params.get('7'))
        directions.append(request.params.get('8'))
        not_empty_directions = list()

        for direction in directions:
            if direction:
                not_empty_directions.append(direction)
        if len(not_empty_directions) < 3:
            return {"message": "Заполните хотя бы три направления"}

        ud = UserData(labels=not_empty_directions, datasets=dict())
        user_data = models.Data(data=ud.to_json(), user_login=user.login)
        request.dbsession.add(user_data)
        transaction.commit()
        return HTTPFound(location="add_data")
    data = request.dbsession.query(models.Data).filter(models.Data.user_login == user.login).first()
    if data:
        return HTTPFound(location="add_data")
    return {}


@view_config(route_name='add_data', renderer='../templates/add_data.jinja2')
def add_data(request):
    user = request.user
    if user is None:
        return HTTPFound(location="login")

    db_data = request.dbsession.query(models.Data).filter(models.Data.user_login == user.login).first()
    if not db_data:
        return HTTPFound(location="user_main")

    data = UserData.from_json(db_data.data)
    if not data.labels:
        return HTTPFound(location="create_directions")

    if (request.POST is not None) & (len(request.POST) > 0):
        week_number = request.params.get('week_number')
        rating = list()
        for label in data.labels:
            rating.append(int(request.params.get(label)))

        dataset = dict()
        dataset["label"] = week_number + " week"
        dataset["data"] = rating
        dataset["fill"] = True
        dataset["backgroundColor"] = backgroundColor[int(week_number) - 1]
        dataset["borderColor"] = borderColor[int(week_number) - 1]
        dataset["borderWidth"] = 2

        data.datasets.append(dataset)

        request.dbsession.query(models.Data.user_login == user.login).delete(synchronize_session=False)
        new_user_data = models.Data(user_login=user.login, data=data.to_json())
        request.dbsession.add(new_user_data)
        transaction.commit()
        return HTTPFound(location="statistics")

    return {"labels": data.labels}


class UserData:
    """репрезентация данных для радара в виде json'а"""
    def __init__(self, labels, datasets):
        self.labels = labels
        self.datasets = datasets

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)


backgroundColor = ("rgba(54, 162, 235, 0.3)", "rgba(255, 99, 132, 0.3)", "rgba(43, 220, 40, 0.3)")
borderColor = ("rgba(54, 162, 235, 1)", "rgba(255, 99, 132, 1)", "rgba(43, 220, 40, 1)")
