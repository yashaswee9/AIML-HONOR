from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number: str):
        self.card_number = card_number

    def get_details(self) -> str:
        return f"Razorpay Card ending in {self.card_number[-4:]}"

    def pay(self, amount: float) -> bool:
        print(f"Payment of ₹{amount:.2f} made using Razorpay Card.")
        return True


class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def get_details(self) -> str:
        return f"Razorpay UPI: {self.upi_id}"

    def pay(self, amount: float) -> bool:
        print(f"Payment of ₹{amount:.2f} made using Razorpay UPI.")
        return True


class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number: str):
        self.card_number = card_number

    def get_details(self) -> str:
        return f"Stripe Card ending in {self.card_number[-4:]}"

    def pay(self, amount: float) -> bool:
        print(f"Payment of ₹{amount:.2f} made using Stripe Card.")
        return True


class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def get_details(self) -> str:
        return f"Stripe UPI: {self.upi_id}"

    def pay(self, amount: float) -> bool:
        print(f"Payment of ₹{amount:.2f} made using Stripe UPI.")
        return True