import json

import requests
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CurrencyConverter(APIView):
    permission_classes = (IsAuthenticated,)
    app_id = "1c8648ab4b7689dbb9d539ab"

    def get(self, request, version):

        return Response("json.loads(response)")

    def post(self, request, version):
        error = []
        if "base_currency" not in request.data:
            error.append({"base_currency": "This filed is required"})
        if "target_currency" not in request.data:
            error.append({"target_currency": "This filed is required"})
        if "amount" not in request.data:
            error.append({"amount": "This filed is required"})
        if len(error) > 0:
            return Response(
                {"success": False, "errors": error, "status_code": 1,
                 "status_message": "failed",
                 "message": "Cannot do currency conversion",
                 "data": None}, status=status.HTTP_201_CREATED)

        base_currency = request.data['base_currency']
        target_currency = request.data['target_currency']
        amount = request.data['amount']
        url = f"https://v6.exchangerate-api.com/v6/{self.app_id}/pair/{base_currency}/{target_currency}"
        response = requests.get(url).content
        conversion_rate = json.loads(response)["conversion_rate"]
        response_content = {
            "base_currency": base_currency,
            "target_currency": target_currency,
            "amount": amount,
            "rate": conversion_rate,
        }
        return Response({
            "success": True, "errors": None, "status_code": 0,
            "status_message": "success",
            "message": "Cannot do currency conversion",
            "data": response_content}, status=status.HTTP_201_CREATED
        )

    def put(self, request, pk, format=None):
        content = {'message': 'Hello, World!'}
        return Response(content)
