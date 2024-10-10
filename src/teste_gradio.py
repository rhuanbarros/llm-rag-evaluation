import random

def random_response(message, history):
    return random.choice(["Yes", "No"])

import gradio as gr

demo = gr.ChatInterface(random_response, type="messages")

demo.launch()