from flask import Flask, request, jsonify, abort
from receiptProcessingApp.controller.RequestHandler import RequestHandler
from pydantic import ValidationError
from http import HTTPStatus

def create_app():
    # Flask only recognizes snake case for running the application
    app = Flask(__name__)
    requestHandler = RequestHandler()

    @app.get("/receipts/<string:id>/points")
    def getPoints(id):
        try:
            totalPoints = requestHandler.getPoints(id)
            return jsonify({"points": totalPoints})
        except ValueError as e:
            return {"reason": str(e)}, HTTPStatus.NOT_FOUND

    @app.post("/receipts/process")
    def processReceipts():
        try:
            receipt = request.json
            receiptId = requestHandler.processReceipts(receipt)
            return jsonify({"id": receiptId})
        except ValidationError as e:
            return {"reason": e.errors()}, HTTPStatus.BAD_REQUEST

    return app
