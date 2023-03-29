class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number, cvv, expiration_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_date = expiration_date

    def pay(self, amount):
        # perform credit card payment
        print(f"Paid {amount} using credit card")

class PayPalStrategy(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        # perform PayPal payment
        print(f"Paid {amount} using PayPal")

class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.pay(amount)

# Usage
credit_card_strategy = CreditCardStrategy("1234 5678 9012 3456", "123", "12/23")
paypal_strategy = PayPalStrategy("example@example.com", "password")

payment_processor = PaymentProcessor(credit_card_strategy)
payment_processor.process_payment(100)

payment_processor = PaymentProcessor(paypal_strategy)
payment_processor.process_payment(50)
