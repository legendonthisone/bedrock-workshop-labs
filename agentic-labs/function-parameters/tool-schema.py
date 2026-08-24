from typing import Annotated, Literal
from strands import tool


@tool
def calculate_refund_amount(
    original_price: Annotated[float, "The original purchase price of the item"],
    refund_type: Annotated[Literal["full", "partial", "store_credit"], "The type of refund to apply"],
    discount_percent: Annotated[float, "Percentage discount to apply before calculating the refund (0–100)"] = 0.0,
) -> float:
    ...
