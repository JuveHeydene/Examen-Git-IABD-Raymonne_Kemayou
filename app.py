import gradio as gr


def greet(name):
    return f"Hello World Juve is a king {name}!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()
