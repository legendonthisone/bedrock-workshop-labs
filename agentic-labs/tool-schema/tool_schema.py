from strands import tool


@tool(
    description="Process a refund for a customer order",
    inputSchema={
        "json": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique identifier of the order to refund",
                },
                "refund_reason": {
                    "type": "string",
                    "description": "The reason for the refund",
                    "enum": ["damaged", "wrong_item", "not_delivered"],
                },
            },
            "required": ["order_id", "refund_reason"],
        }
    },
)
def process_refund(order_id: str, refund_reason: str) -> str:
    pass
