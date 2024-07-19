from http import HTTPStatus

from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from receipt_processing_app.controller.in_memory_database_controller import (
    InMemoryDatabaseController,
)
from receipt_processing_app.controller.receipt_processing_service import (
    ReceiptProcessingService,
)
from receipt_processing_app.controller.request_handler import RequestHandler

request_handler = RequestHandler(
    InMemoryDatabaseController(), ReceiptProcessingService()
)

main = Blueprint("main", __name__)


@main.post("/receipts/process")
def process_receipts():
    try:
        receipt = request.json
        receipt_id = request_handler.process_receipts(receipt)
        return jsonify({"id": receipt_id})
    except (ValueError, ValidationError):
        return "The receipt is invalid", HTTPStatus.BAD_REQUEST


@main.get("/receipts/<string:id>/points")
def get_points(id):
    try:
        total_points = request_handler.get_points(id)
        return jsonify({"points": total_points})
    except ValueError:
        return "No receipt found for that id", HTTPStatus.NOT_FOUND
