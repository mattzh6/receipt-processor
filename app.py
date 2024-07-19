from flask import Flask

from receipt_processing_app.routes import main


def create_app():
    # Flask only recognizes snake case for running the application
    app = Flask(__name__)
    app.register_blueprint(main)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5050)