class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class Paypal:
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


p = PaymentProcessor(CreditCard())
p.pay(500)

p.set_strategy(Paypal())
p.pay(300)

p.set_strategy(UPI())
p.pay(150)