from aggregators import Aggregator, StripeAggregator, RazorpayAggregator


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name: str) -> Aggregator:
        if aggregator_name not in cls.factory:
            raise ValueError(f"Invalid aggregator: {aggregator_name}")

        return cls.factory[aggregator_name]()