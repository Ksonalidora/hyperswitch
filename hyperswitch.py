import stripe

# Set your Stripe API key
stripe.api_key = 'your_stripe_api_key'

def make_payment(amount, currency='usd', card_token='tok_sample'):
    try:
        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,  # Amount in cents
            currency=currency,
            payment_method_types=['card'],
            payment_method=card_token,
            confirm=True  # Automatically confirm the payment
        )

        # Check the payment status
        if payment_intent.status == 'succeeded':
            return True, f"Payment successful! Payment ID: {payment_intent.id}"
        else:
            return False, f"Payment failed: {payment_intent.last_payment_error.message}"
    except stripe.error.StripeError as e:
        return False, f"Payment error: {e}"

if __name__ == "__main__":
    # Example usage
    amount = 1000  # Amount in cents (e.g., $10.00)
    success, message = make_payment(amount)
    if success:
        print(message)
    else:
        print(message)
