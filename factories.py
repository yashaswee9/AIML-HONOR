from abc import ABC, abstractmethod
from typing import Dict, Type

from payment_methods import (
    PaymentMethod,
    RazorpayCardPayment,
    RazorpayUPIPayment,
    StripeCardPayment,
    StripeUPIPayment
)


class FactoryPaymentMethod(ABC):
    factory: Dict[str, Type[PaymentMethod]] = {}

    @classmethod
    def get_payment_object(cls, method_type: str, **kwargs) -> PaymentMethod:
        if method_type not in cls.factory:
            raise ValueError(f"Invalid payment method: {method_type}")

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