import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3.2"  # Replace with your model name
prompt = "What is semantic documenting?"

try:
    # Send the query to the model
    response = client.generate(model=model, prompt=prompt)

    # Print the response from the model
    print("Response from Ollama:")
    print(response.response)
except ollama.ResponseError as e:
    if "model not found" in str(e).lower():
        print(f"Error: The model '{model}' was not found. Please check the model name or ensure it is available.")
    else:
        print(f"An error occurred: {e}")
