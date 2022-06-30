from flask import make_response, jsonify
from app.models.user import Task


def get_one_task(id):
    task = Task.query.filter_by(id=id).first()

    if not task:
        return make_response(jsonify("id not found"), 404)

    result = {}
    result["name"] = task.name
    result["content"] = task.content
    result["complete"] = task.complete

    return make_response(jsonify(result), 200)
