from flask import make_response, jsonify
from extensions import db
from app.models.user import Task


def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    if not task:
        return make_response(jsonify("Task id not found"), 404)
    db.session.delete(task)
    db.session.commit()
    return make_response(jsonify("Deleted!"), 200)
