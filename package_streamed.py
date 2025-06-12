from ollama import chat

# Define the model and the input prompt
model = "llama3.2"  # Replace with your model name
prompt = "What is semantic documenting?"

# Send the query to the model
stream = chat(
    model=model, 
    messages=[{"role": "user", "content": "What is the square root of 16?"}], 
    stream=True
)

# Print the response from the model
print("Response from Ollama:")
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
