from extensions import app
from app.controller.todo_controller import api

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)
