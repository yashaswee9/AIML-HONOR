
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razorpay Card ending in {self.card_number[-4:]}"

    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} using Razorpay Card")
        return True


class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Razorpay UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} using Razorpay UPI")
        return True


class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Stripe Card ending in {self.card_number[-4:]}"

    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} using Stripe Card")
        return True


class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Stripe UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} using Stripe UPI")
        return True


class FactoryPaymentMethod(ABC):
    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")
        return cls.factory[method_type](**kwargs)


class RazorpayFactory(FactoryPaymentMethod):
    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }


class StripeFactory(FactoryPaymentMethod):
    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }


class Aggregator(ABC):
    def __init__(self, name, processing_fee, payment_factory):
        self.name = name
        self.processing_fee = processing_fee
        self.payment_factory = payment_factory

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass


class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay", 2.0, RazorpayFactory)

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.payment_factory.get_payment_object(method_type, **kwargs)
        fee = amount * self.processing_fee / 100
        print(f"Processing fee: Rs. {fee:.2f}")
        print(payment.get_details())
        return payment.pay(amount + fee)


class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe", 2.9, StripeFactory)

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.payment_factory.get_payment_object(method_type, **kwargs)
        fee = amount * self.processing_fee / 100
        print(f"Processing fee: Rs. {fee:.2f}")
        print(payment.get_details())
        return payment.pay(amount + fee)


class AggregatorFactory:
    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        if aggregator_name not in cls.factory:
            raise ValueError("Invalid payment gateway")
        return cls.factory[aggregator_name]()


def main():
    print("Multi-Gateway Payment Processing Engine")

    try:
        gateway = input("Select gateway (stripe/razorpay): ").strip().lower()
        aggregator = AggregatorFactory.get_aggregator_object(gateway)

        method = input("Select payment method (card/upi): ").strip().lower()

        if method == "card":
            details = {"card_number": input("Enter card number: ").strip()}
        elif method == "upi":
            details = {"upi_id": input("Enter UPI ID: ").strip()}
        else:
            raise ValueError("Invalid payment method")

        amount = float(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if aggregator.call_get_payment_object(method, amount, **details):
            print("Payment successful")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
