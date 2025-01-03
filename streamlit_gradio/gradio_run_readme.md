import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()  



<img width="1164" alt="image" src="https://github.com/user-attachments/assets/240fbdec-7ec2-464f-9c34-9b2c258a0dfb" />


