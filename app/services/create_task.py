from flask import make_response, jsonify
from extensions import db
from app.models.user import Task


def create(request):
    data = request.get_json()
    new_task = Task(name=data['name'], content=data['content'], complete=False)
    db.session.add(new_task)
    db.session.commit()
    return make_response(jsonify("New task is created!"), 200)
