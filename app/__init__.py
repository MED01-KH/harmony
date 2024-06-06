from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app import routes
    app.register_blueprint(routes.main_bp)

    return app
