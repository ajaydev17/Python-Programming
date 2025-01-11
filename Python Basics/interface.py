"""
In Python, interfaces are typically implemented using abstract base classes (ABCs).
They define a contract for behavior without dictating how it should be implemented.
An abstract base class can act as an interface by only containing abstract methods.
"""

"""
Suppose you're building a payment processing system that supports multiple payment gateways (e.g., PayPal, Stripe).
You can use interfaces to enforce a contract that all payment gateways must follow.
"""

from abc import ABC, abstractmethod


# Interface (Abstract Base Class)
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        """Authenticate the user with the payment gateway."""
        pass

    @abstractmethod
    def process_payment(self, amount):
        """Process the payment."""
        pass

    @abstractmethod
    def refund(self, transaction_id):
        """Refund a transaction."""
        pass


# Concrete Implementation for PayPal
class PayPalGateway(PaymentGateway):
    def authenticate(self, credentials):
        print(f"Authenticating with PayPal: {credentials}")

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

    def refund(self, transaction_id):
        print(f"Refunding PayPal transaction {transaction_id}")


# Concrete Implementation for Stripe
class StripeGateway(PaymentGateway):
    def authenticate(self, credentials):
        print(f"Authenticating with Stripe: {credentials}")

    def process_payment(self, amount):
        print(f"Processing Stripe payment of ${amount}")

    def refund(self, transaction_id):
        print(f"Refunding Stripe transaction {transaction_id}")


# Unified Payment Processor
class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def make_payment(self, credentials, amount):
        self.gateway.authenticate(credentials)
        self.gateway.process_payment(amount)

    def make_refund(self, transaction_id):
        self.gateway.refund(transaction_id)


# Usage
paypal = PayPalGateway()
stripe = StripeGateway()

processor = PaymentProcessor(paypal)
processor.make_payment(credentials="user:password", amount=100)
processor.make_refund(transaction_id="PAY123")

print("--- Switching to Stripe ---")
processor.gateway = stripe
processor.make_payment(credentials="token:abc123", amount=200)
processor.make_refund(transaction_id="STR456")
