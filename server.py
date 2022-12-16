from flask import Flask, jsonify, request, Response, send_from_directory
from load_config import load_config
import util.constants as const
import os
import json
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():

    # Custom Config
    app = Flask(__name__)
    CORS(app)
    application = app
    load_config(application)

    # Swagger Configuration
    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': application.config[const.APP_NAME]
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "doej@abc.com"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "doej1@abc.com"
        }
    ]

    @app.route('/', methods=['GET'])
    def heartbeat():
        """
        Sample API to test the flask is configured properly
        """
        return jsonify({'message': 'server is up'})

    @app.route("/users")
    def get_users() -> list:
        return users

    @app.route('/user/<first_name>')
    def get_user(first_name: str) -> dict:
        for item in users:
            if item.get("first_name") == first_name:
                return item

        return {}

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(
        host="0.0.0.0", port=application.config[const.PORT], debug=application.config[const.DEBUG])
