from instance.config import *
from views import *
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(index_page)
    if test_config is None:
        pass
    else:
        pass
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
