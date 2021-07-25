import json
import os
import stripe


def main(event, context):
    stripe.api_key = ""

    result = stripe.Charge.create(
      amount=2000,
      currency="mxn",
      source="tok_amex",
      description="My First Test Charge (created for API docs)",
    )

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(result)
    }

    return response
