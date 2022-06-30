from flask import make_response, jsonify
from extensions import db
from app.models.user import Task


def update_task(id, request):
    data = request.get_json()

    name = data.get('name', None)
    content = data.get('content', None)
    complete = data.get('complete', None)

    task = Task.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify("Task not found!"), 404)

    task.name = name
    task.content = content
    task.complete = complete

    db.session.commit()

    return make_response(jsonify("Updated!"), 200)
