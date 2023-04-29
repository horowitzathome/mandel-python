from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import bp as mb_service_bp
    app.register_blueprint(mb_service_bp)

    return app