from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# Define a Gradio UI function
def greet(name):
    return f"Hello, {name}!"

# Create a Gradio Interface
gr_interface = gr.Interface(fn=greet, inputs="text", outputs="text")

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

@app.get("/gradio")
def gradio_app():
    return gr_interface.launch(share=False, server_name="0.0.0.0", server_port=8000)

# Run locally: uvicorn app:app --host 0.0.0.0 --port 8000
