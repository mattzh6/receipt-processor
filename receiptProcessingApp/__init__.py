from flask import Flask, request, jsonify, abort
from receiptProcessingApp.controller.request_handler import RequestHandler
from pydantic import ValidationError
from http import HTTPStatus

def create_app():
    # Flask only recognizes snake case for running the application
    app = Flask(__name__)
    request_handler = RequestHandler()

    @app.post("/receipts/process")
    def process_receipts():
        try:
            receipt = request.json
            receipt_id = request_handler.process_receipts(receipt)
            return jsonify({"id": receipt_id})
        except ValidationError:
            return "The receipt is invalid", HTTPStatus.BAD_REQUEST

    @app.get("/receipts/<string:id>/points")
    def get_points(id):
        try:
            total_points = request_handler.get_points(id)
            return jsonify({"points": total_points})
        except ValueError:
            return "No receipt found for that id", HTTPStatus.NOT_FOUND
    return app
