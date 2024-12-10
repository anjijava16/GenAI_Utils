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
