from flask import Blueprint, request
from app.services import create_task, get_task, update, get_taskinfo, deletetask

api = Blueprint('todo service', 'todo service')


@api.route('/task', methods=['POST'])
def add_task():
    return create_task.create(request)


@api.route('/', methods=['GET'])
def get_alltask():
    return get_task.get_all_tasks(request)


@api.route('/task/<id>', methods=['PUT'])
def update_taskid(id):
    return update.update_task(id, request)


@api.route('/task/<id>', methods=['GET'])
def getsingletask(id):
    return get_taskinfo.get_one_task(id)


@api.route("/task/<id>", methods=["DELETE"])
def delete_one_task(id):
    return deletetask.delete_task(id)
