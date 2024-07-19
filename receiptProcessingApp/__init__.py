from flask import Flask, request, jsonify, abort
from receiptProcessingApp.controller.request_handler import RequestHandler
from pydantic import ValidationError
from http import HTTPStatus

def create_app():
    # Flask only recognizes snake case for running the application
    app = Flask(__name__)
    request_handler = RequestHandler()

    @app.get("/receipts/<string:id>/points")
    def get_points(id):
        try:
            total_points = request_handler.get_points(id)
            return jsonify({"points": total_points})
        except ValueError as e:
            return {"reason": str(e)}, HTTPStatus.NOT_FOUND

    @app.post("/receipts/process")
    def process_receipts():
        try:
            receipt = request.json
            receipt_id = request_handler.process_receipts(receipt)
            return jsonify({"id": receipt_id})
        except ValidationError as e:
            return {"reason": e.errors()}, HTTPStatus.BAD_REQUEST

    return app
