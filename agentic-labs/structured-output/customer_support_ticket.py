from typing import Literal, Optional
from pydantic import BaseModel, Field


class CustomerSupportTicket(BaseModel):
    """Structured analysis of a customer support message"""

    issue_summary: str = Field(description="One-line summary of the customer's issue")
    issue_type: Literal["order_status", "refund", "damaged_item", "wrong_item", "other"] = Field(
        description="The category of the customer's issue"
    )
    urgency: Literal["low", "medium", "high"] = Field(
        description="The urgency level based on the tone and nature of the message"
    )
    order_id: Optional[str] = Field(description="The order ID mentioned in the message, if any", default=None)
