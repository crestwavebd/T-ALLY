import requests
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

AMADEUS_API_KEY = 'AUcgJZ6gtrI60afudJaDSuwKmyUoyTAN'
STRIPE_API_KEY = 'sk_test_51PZzciCyC8OWGlHKE542bwYjZnBTEmCd4nTubWatfDsfQUWXV3pNVe6MDhhYLSJWjwR4CZ9FYNAVCE56cfbIpP2Z00uh7EeZOl'

stripe.api_key = sk_test_51PZzciCyC8OWGlHKE542bwYjZnBTEmCd4nTubWatfDsfQUWXV3pNVe6MDhhYLSJWjwR4CZ9FYNAVCE56cfbIpP2Z00uh7EeZOl

@app.route('/search-flights', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_date = request.args.get('departure_date')

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {AMADEUS_API_KEY}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": "1"
    }

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    data = request.json
    amount = data['amount']

    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
        payment_method_types=['card'],
    )

    return jsonify(payment_intent)

if __name__ == '__main__':
    app.run(debug=True)
