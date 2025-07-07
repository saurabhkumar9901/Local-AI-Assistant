# Importing the libraries
import gradio as gr
from Sequence import *
from chat import *
from model import *
from chunks import *
from embedding import *


# All Wrapped in a Gradio Framework
theme = gr.themes.Soft()
with gr.Blocks(theme=theme) as demo:
    with gr.Tab("Ask me Anything"):
        gr.ChatInterface(
            chat,
            chatbot=gr.Chatbot(
                elem_id="chatbot",
                bubble_full_width=False,
                autoscroll=True,
                avatar_images=("source/information.png", "source/chat-bot.png"),
                show_copy_all_button=True,
                type="messages"
            ),
            multimodal=True,
            type='messages',
            textbox=gr.MultimodalTextbox(
                placeholder="Enter message or upload file...",
                show_label=True
            )
        )

    with gr.Tab("Challenge Me"):
        gr.ChatInterface(
            challenge,
            chatbot=gr.Chatbot(
                elem_id="chatbot",
                bubble_full_width=False,
                autoscroll=True,
                avatar_images=("source/information.png", "source/chat-bot.png"),
                show_copy_all_button=True,
                type="messages"
            ),
            multimodal=True,
            type='messages',
            textbox=gr.MultimodalTextbox(
                placeholder="Enter message or upload file...",
                show_label=True
            )
        )

demo.launch(inbrowser=True)
