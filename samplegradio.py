import gradio as gr

# Define a simple text classification function
def classify_text(text):
    positive_keywords = ['happy', 'joy', 'love', 'excited', 'great']
    negative_keywords = ['sad', 'angry', 'hate', 'frustrated', 'bad']

    positive_count = sum(word in text.lower() for word in positive_keywords)
    negative_count = sum(word in text.lower() for word in negative_keywords)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# Create a Gradio interface
interface = gr.Interface(
    fn=classify_text,                  # Function to interface with
    inputs=gr.Textbox(lines=5, placeholder="Enter text here..."),  # Input type: textbox for multi-line text input
    outputs=gr.Textbox(),              # Output type: textbox for the classification result
    title="Text Classifier",           # Title of the interface
    description="This model classifies text as Positive, Negative, or Neutral based on the presence of keywords."  # Description
)

# Launch the interface
interface.launch()

