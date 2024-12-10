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

  ```
response = openai.chat.completions.create(
    model='gpt-4o',
    messages=messages,
    tools=tools
)
import json

# Extract the arguments for get_delivery_date
# Note this code assumes we have already determined that the model generated a function call. See below for a more production ready example that shows how to check if the model generated a function call
tool_call = response.choices[0].message.tool_calls[0]


Input :
1. create

Output:

1. -> ChatCompletion | Stream[ChatCompletionChunk]:


# ChatComplectionChunk:
class ChatCompletionChunk(BaseModel):
id: str
"""A unique identifier for the chat completion. Each chunk has the same ID."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can contain more than one elements if `n` is greater than 1. Can also be empty
    for the last chunk if you set `stream_options: {"include_usage": true}`.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created.

    Each chunk has the same timestamp.
    """

    model: str
    """The model to generate the completion."""

    object: Literal["chat.completion.chunk"]
    """The object type, which is always `chat.completion.chunk`."""

    service_tier: Optional[Literal["scale", "default"]] = None
    """The service tier used for processing the request.

    This field is only included if the `service_tier` parameter is specified in the
    request.
    """

    system_fingerprint: Optional[str] = None
    """
    This fingerprint represents the backend configuration that the model runs with.
    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[CompletionUsage] = None
    """
    An optional field that will only be present when you set
    `stream_options: {"include_usage": true}` in your request. When present, it
    contains a null value except for the last chunk which contains the token usage
    statistics for the entire request.
    """

# Batch:
class ChatCompletion(BaseModel):
    id: str
"""A unique identifier for the chat completion."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the chat completion."""

    object: Literal["chat.completion"]
    """The object type, which is always `chat.completion`."""

    service_tier: Optional[Literal["scale", "default"]] = None
    """The service tier used for processing the request.

    This field is only included if the `service_tier` parameter is specified in the
    request.
    """

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[CompletionUsage] = None
    """Usage statistics for the completion request."""


class Choice(BaseModel):
finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
"""The reason the model stopped generating tokens.

    This will be `stop` if the model hit a natural stop point or a provided stop
    sequence, `length` if the maximum number of tokens specified in the request was
    reached, `content_filter` if content was omitted due to a flag from our content
    filters, `tool_calls` if the model called a tool, or `function_call`
    (deprecated) if the model called a function.
    """

    index: int
    """The index of the choice in the list of choices."""

    logprobs: Optional[ChoiceLogprobs] = None
    """Log probability information for the choice."""

    message: ChatCompletionMessage
    """A chat completion message generated by the model."""


class ChatCompletionMessage(BaseModel):
content: Optional[str] = None
"""The contents of the message."""

    refusal: Optional[str] = None
    """The refusal message generated by the model."""

    role: Literal["assistant"]
    """The role of the author of this message."""

    audio: Optional[ChatCompletionAudio] = None
    """
    If the audio output modality is requested, this object contains data about the
    audio response from the model.
    [Learn more](https://platform.openai.com/docs/guides/audio).
    """

    function_call: Optional[FunctionCall] = None
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
    """The tool calls generated by the model, such as function calls."""

class FunctionCall(BaseModel):
arguments: str
"""
The arguments to call the function with, as generated by the model in JSON
format. Note that the model does not always generate valid JSON, and may
hallucinate parameters not defined by your function schema. Validate the
arguments in your code before calling your function.
"""

    name: str
    """The name of the function to call."""


class Function(BaseModel):
arguments: str
"""
The arguments to call the function with, as generated by the model in JSON
format. Note that the model does not always generate valid JSON, and may
hallucinate parameters not defined by your function schema. Validate the
arguments in your code before calling your function.
"""

    name: str
    """The name of the function to call."""


class ChatCompletionMessageToolCall(BaseModel):
id: str
"""The ID of the tool call."""

    function: Function
    """The function that the model called."""

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""

```

