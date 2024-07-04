import gradio as gr
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

# Load a pre-trained ResNet model
model = models.resnet18(pretrained=True)
model.eval()

# Define a function to make predictions
def classify_image(input_image):
    # Convert NumPy array to PIL Image
    input_image = Image.fromarray(input_image.astype('uint8'))

    # Preprocess the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_image = preprocess(input_image).unsqueeze(0)

    # Make a prediction
    with torch.no_grad():
        output = model(input_image)

    # Get the class label with the highest probability
    _, predicted_class = output.max(1)
    return str(predicted_class.item())

# Create a Gradio interface
iface = gr.Interface(
    fn=classify_image,  # Function to make predictions
    inputs=gr.inputs.Image(type="numpy"),  # Input: NumPy array representing an image
    outputs=gr.outputs.Label(),  # Output: Label
    live=True,
)

# Launch the Gradio app
iface.launch()
