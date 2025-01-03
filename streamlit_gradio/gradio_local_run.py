# !pip install gradio --break-system-package

import gradio as gr

def get_travel_lan(query):
  "welcome to new Travel plan info"

def plan_trip(query):
    """Generate a travel plan based on user input"""
    return get_travel_plan(query)

demo = gr.Interface(
    fn=plan_trip,
    inputs=gr.Textbox(
        label="What kind of trip would you like to plan?",
        placeholder="E.g. 'Plan a 5-day trip to Paris focusing on art and cuisine'",
        lines=3
    ),
    outputs=gr.Textbox(
        label="Your Travel Plan",
        lines=10
    ),
    title="Travel Agent By Agentversity",
    description="Let me help you plan your perfect trip! Just describe what kind of trip you're looking for.",
    theme="soft",
    examples=[
        ["Plan a weekend getaway to the mountains with hiking and relaxation"],
        ["3-day food tour in Tokyo"]
    ]
)
    
demo.launch(share=True) 
