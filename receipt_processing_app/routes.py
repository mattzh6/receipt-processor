from flask import Flask, request, jsonify
from receipt_processing_app.controller.request_handler import RequestHandler
from receipt_processing_app.controller.receipt_processing_service import ReceiptProcessingService
from receipt_processing_app.controller.in_memory_database_controller import InMemoryDatabaseController
from pydantic import ValidationError
from http import HTTPStatus


def create_app():
    # Flask only recognizes snake case for running the application
    app = Flask(__name__)
    in_memory_database_controller = InMemoryDatabaseController()
    receipt_processing_service = ReceiptProcessingService()
    request_handler = RequestHandler(in_memory_database_controller, receipt_processing_service)

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
