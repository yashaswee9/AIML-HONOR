from aggregator_factory import AggregatorFactory


def main():
    print("=== Multi-Gateway Payment Processing Engine ===")

    try:
        aggregator_name = input("Select Aggregator (stripe/razorpay): ").strip().lower()

        aggregator = AggregatorFactory.get_aggregator_object(aggregator_name)

        method_type = input("Select Method (card/upi): ").strip().lower()

        if method_type == "card":
            card_number = input("Enter Card Number: ").strip()
            payment_details = {"card_number": card_number}

        elif method_type == "upi":
            upi_id = input("Enter UPI ID: ").strip()
            payment_details = {"upi_id": upi_id}

        else:
            raise ValueError("Invalid payment method.")

        amount = float(input("Enter Amount: "))

        success = aggregator.call_get_payment_object(
            method_type,
            amount,
            **payment_details
        )

        if success:
            print("Payment successful!")
        else:
            print("Payment failed.")

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()