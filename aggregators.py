from abc import ABC, abstractmethod

from factories import RazorpayFactory, StripeFactory


class Aggregator(ABC):

    name: str

    @abstractmethod
    def call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        pass


class RazorpayAggregator(Aggregator):

    name = "Razorpay"
    processing_fee = 2.0
    factory = RazorpayFactory

    def call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        payment = self.factory.get_payment_object(method_type, **kwargs)
        total_amount = amount + (amount * self.processing_fee / 100)
        print(f"Processing fee: ₹{amount * self.processing_fee / 100:.2f}")
        return payment.pay(total_amount)


class StripeAggregator(Aggregator):

    name = "Stripe"
    processing_fee = 2.9
    factory = StripeFactory

    def call_get_payment_object(self, method_type: str, amount: float, **kwargs) -> bool:
        payment = self.factory.get_payment_object(method_type, **kwargs)
        total_amount = amount + (amount * self.processing_fee / 100)
        print(f"Processing fee: ₹{amount * self.processing_fee / 100:.2f}")
        return payment.pay(total_amount)