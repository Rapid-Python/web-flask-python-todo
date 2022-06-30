from flask import make_response, jsonify
from app.models.user import Task
from flask_api import status


def get_all_tasks(request):
    filters = {
        "ALL": "all",
        "COMPLETED": "completed",
        "NOT_COMPLETED": "not_completed"
    }
    page_size = request.args.get('page_size', None)
    current_page = request.args.get('current_page', None)
    filter = request.args.get('filter', None)

    if filter == filters["ALL"]:
        task_query = Task.query.paginate(int(current_page), int(page_size), False)

    elif filter == filters["COMPLETED"]:
        task_query = Task.query.filter_by(complete=True).paginate(int(current_page), int(page_size), False)

    elif filter == filters["NOT_COMPLETED"]:
        task_query = Task.query.filter_by(complete=False).paginate(int(current_page), int(page_size), False)

    else:
        return make_response(jsonify("Filter not found!"), 404)

    task_items = task_query.items
    total = len(task_items)

    output = []

    for task in task_items:
        task_data = {}
        task_data['id'] = task.id
        task_data['name'] = task.name
        task_data['content'] = task.content
        task_data['complete'] = task.complete
        output.append(task_data)

    response = jsonify(
        {
            "total": total,
            "page_size": int(page_size),
            "current_page": int(current_page),
            "items": output
        }
    )

    return response, status.HTTP_201_CREATED
