import openai
import os


def get_delivery_date(order_id):
    import datetime
    delivery_date = datetime.datetime.now()
    return delivery_date


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_delivery_date",
            "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The customer's order ID."
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False
            }
        }
    }
]

messages = []
messages.append({"role": "system",
                 "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order?"})
messages.append(
    {"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"})
messages.append({"role": "user", "content": "i think it is order_12399995"})

response = openai.chat.completions.create(
    model='gpt-4o',
    messages=messages,
    tools=tools
)
import json

# Extract the arguments for get_delivery_date
# Note this code assumes we have already determined that the model generated a function call. See below for a more production ready example that shows how to check if the model generated a function call

tool_call = response.choices[0].message.tool_calls[0]

print(f"tool_call ={tool_call}")

arguments = json.loads(tool_call.function.arguments)

print(f" arguments= {arguments}")

order_id = arguments.get('order_id')

print(f"order_id= {order_id}")

# Call the get_delivery_date function with the extracted order_id

delivery_date = get_delivery_date(order_id)

print(f"delivery_date= {delivery_date}")

function_call_result_message = {
    "role": "tool",
    "content": json.dumps({
        "order_id": order_id,
        "delivery_date": delivery_date.strftime('%Y-%m-%d %H:%M:%S')
    }),
    "tool_call_id": response.choices[0].message.tool_calls[0].id
}

print(function_call_result_message)

# Prepare the chat completion call payload

completion_payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system",
         "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."},
        {"role": "user", "content": "Hi, can you tell me the delivery date for my order?"},
        {"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"},
        {"role": "user", "content": "i think it is order_12399995"},
        response.choices[0].message,
        function_call_result_message
    ]
}

print(completion_payload)

response = openai.chat.completions.create(
    model=completion_payload["model"],
    messages=completion_payload["messages"]
)

# Print the response from the API. In this case it will typically contain a message such as "The delivery date for your order #12345 is xyz. Is there anything else I can help you with?"

print(response)


