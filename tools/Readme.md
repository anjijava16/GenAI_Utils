# Run the Inspect function:

```

def get_current_weather(city:str):
    """
    This function featch the current weather of the given city.

    """
    return "city"

```


# Run the Function
/Users/welcome/anaconda3/envs/autogen_studio/bin/python /Users/welcome/Library/Mobile Documents/com~apple~CloudDocs/Sai_Workspace/lang_server_app/DeepDive_GenAI/Agents_Demos/autogen_agents/custom_agents/openai_orchestration_agents/inspect_fun.py 


```
{
  'type': 'function',
  'function': {
    'name': 'get_current_weather',
    'description': 'This function featch the current weather of the given city.',
    'parameters': {
      'type': 'object',
      'properties': {
        'city': {
          'type': 'string'
        }
      },
      'required': [
        'city'
      ]
    }
  }
}

```


This code is an implementation of an **OpenAI GPT-based conversational agent** designed for customer support, where the assistant interacts with a user and uses a **function-calling mechanism** to provide the delivery date of an order.

Here’s a breakdown of the code:

---

### 1. **Importing Required Libraries**
```python
import openai
import os
import json
import datetime
```
- The `openai` library is used to interact with the OpenAI API.
- `datetime` is used to handle and return the current date and time for the delivery date.
- `json` helps with parsing and formatting data exchanged between the assistant and tools.

---

### 2. **Defining the Tool**
```python
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
```
- This defines the **tool** `get_delivery_date`:
  - It takes an `order_id` as input (a string).
  - The tool is designed to fetch and return the delivery date of the order.
  - **Parameters schema** specifies the required inputs and validates them.

---

### 3. **Creating the Chat Messages**
```python
messages = []
messages.append({"role": "system",
                 "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})
messages.append({"role": "user", "content": "Hi, can you tell me the delivery date for my order?"})
messages.append(
    {"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"})
messages.append({"role": "user", "content": "i think it is order_12399995"})
```
- The `messages` array simulates a conversation:
  - **System message**: Sets the assistant's behavior as a helpful support agent.
  - **User messages**: User initiates the request and provides an order ID.
  - **Assistant message**: Requests the order ID explicitly.

---

### 4. **Calling OpenAI API for Completion**
```python
response = openai.chat.completions.create(
    model='gpt-4o',
    messages=messages,
    tools=tools
)
```
- This sends the current conversation (`messages`) and the available tools (`tools`) to the OpenAI model `gpt-4o`.
- The response includes:
  - The assistant's next response.
  - Whether it decided to call a tool (`tool_call`).

---

### 5. **Extracting Tool Call Arguments**
```python
tool_call = response.choices[0].message.tool_calls[0]
arguments = json.loads(tool_call.function.arguments)
order_id = arguments.get('order_id')
```
- **Extracts the tool call**:
  - The assistant indicates it needs to use the `get_delivery_date` tool and specifies the `order_id`.
- **Parses the tool call arguments**:
  - Extracts the `order_id` from the tool call payload.

---

### 6. **Calling the Tool**
```python
delivery_date = get_delivery_date(order_id)
```
- The script manually calls the `get_delivery_date` function, which returns the current date/time as a mock delivery date.

---

### 7. **Preparing the Tool's Result**
```python
function_call_result_message = {
    "role": "tool",
    "content": json.dumps({
        "order_id": order_id,
        "delivery_date": delivery_date.strftime('%Y-%m-%d %H:%M:%S')
    }),
    "tool_call_id": response.choices[0].message.tool_calls[0].id
}
```
- Formats the tool's result into a structured JSON object:
  - Includes the `order_id` and the formatted `delivery_date`.
  - Links the result to the tool call using its `tool_call_id`.

---

### 8. **Sending Back the Full Conversation**
```python
completion_payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."},
        {"role": "user", "content": "Hi, can you tell me the delivery date for my order?"},
        {"role": "assistant", "content": "Hi there! I can help with that. Can you please provide your order ID?"},
        {"role": "user", "content": "i think it is order_12399995"},
        response.choices[0].message,
        function_call_result_message
    ]
}
```
- Updates the conversation to include:
  - The assistant's original tool call.
  - The tool's result.
- Sends it back to the API to generate the assistant's response.

---

### 9. **Generating the Final Response**
```python
response = openai.chat.completions.create(
    model=completion_payload["model"],
    messages=completion_payload["messages"]
)

print(response)
```
- Gets the final response from the API after incorporating the tool's result.
- This response typically communicates the delivery date to the user.

---

### Key Features:
- **Function Calls**: Demonstrates OpenAI's new function-calling capabilities for better integration with external systems.
- **Tool Management**: The assistant uses tools dynamically based on user requests.
- **Structured Responses**: Each step integrates neatly into the conversation flow.

---

### Improvements:
1. **Error Handling**:
   - Add checks for missing/invalid `order_id`.
   - Handle cases where the tool returns no result.
2. **Dynamic Functionality**:
   - Replace the mock `get_delivery_date` function with an actual logic or API call.
3. **Testing**:
   - Simulate various user inputs and refine tool usage.
