import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Neural network functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Function to train the neural network
def train_neural_network(X, y, hidden_size=4, learning_rate=0.1, epochs=10000):
    input_size = X.shape[1]
    output_size = 1

    # Initialize weights and biases
    np.random.seed(42)
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))

    # Lists to store loss values
    loss_history = []

    # Training loop
    for epoch in range(epochs):
        # Forward pass
        z1 = np.dot(X, W1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)

        # Calculate the loss (mean squared error)
        loss = np.mean((y - a2) ** 2)
        loss_history.append(loss)

        # Backward pass
        dloss_da2 = -(y - a2)
        da2_dz2 = sigmoid_derivative(a2)
        dz2_dW2 = a1
        dz2_da1 = W2
        da1_dz1 = sigmoid_derivative(a1)
        dz1_dW1 = X

        dloss_dz2 = dloss_da2 * da2_dz2
        dloss_dW2 = np.dot(dz2_dW2.T, dloss_dz2)
        dloss_db2 = np.sum(dloss_dz2, axis=0, keepdims=True)

        dloss_da1 = np.dot(dloss_dz2, dz2_da1.T)
        dloss_dz1 = dloss_da1 * da1_dz1
        dloss_dW1 = np.dot(dz1_dW1.T, dloss_dz1)
        dloss_db1 = np.sum(dloss_dz1, axis=0, keepdims=True)

        # Update weights and biases
        W1 -= learning_rate * dloss_dW1
        b1 -= learning_rate * dloss_db1
        W2 -= learning_rate * dloss_dW2
        b2 -= learning_rate * dloss_db2

    return W1, b1, W2, b2, loss_history

# Function to make predictions
def predict(X, W1, b1, W2, b2):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    return (a2 > 0.5).astype(int)

# Function to plot confusion matrix
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_true))
    return disp

# Streamlit app
st.title('Simple Neural Network with Text Data')

st.sidebar.header('User Input Parameters')

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())  # Display first few rows of the uploaded CSV
    
    text_column = st.sidebar.selectbox("Select text column for tokenization", df.columns)
    target_column = st.sidebar.selectbox("Select target column", df.columns)

    if st.sidebar.button('Train Neural Network'):
        # Get selected columns
        X_text = df[text_column].astype(str).values
        y = df[target_column].values.reshape(-1, 1)

        # Tokenize the text
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(X_text).toarray()

        # Train the neural network
        W1, b1, W2, b2, loss_history = train_neural_network(X, y, hidden_size=4, learning_rate=0.1, epochs=10000)
        
        # Plot the loss history
        st.subheader('Loss History')
        plt.figure(figsize=(10, 5))
        plt.plot(loss_history)
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title('Loss History')
        st.pyplot(plt)
        
        # Make predictions
        predictions = predict(X, W1, b1, W2, b2)
        
        # Display predictions
        st.subheader('Predictions vs True Labels')
        results = pd.DataFrame({'Predicted': predictions.flatten(), 'True': y.flatten()})
        st.write(results)
        
        # Plot confusion matrix
        st.subheader('Confusion Matrix')
        cm = plot_confusion_matrix(y.flatten(), predictions.flatten())
        cm.plot()
        st.pyplot()
else:
    st.info('Please upload a CSV file.')
