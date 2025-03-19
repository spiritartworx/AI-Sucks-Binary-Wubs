import json
import base64

# Function to convert text to binary
def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

# Function to encode binary to base64 JSON
def binary_to_json(binary_data):
    encoded_data = base64.b64encode(binary_data.encode()).decode()
    json_data = json.dumps({"music_data": encoded_data}, indent=4)
    return json_data

# Function to decode JSON back to binary
def json_to_binary(json_data):
    decoded_json = json.loads(json_data)
    binary_data = base64.b64decode(decoded_json["music_data"]).decode()
    return binary_data

# Example usage
text_prompt = "Deep, hypnotic dubstep groove with heavy, evolving wubs and thick sub-bass..."
binary_data = text_to_binary(text_prompt)
json_data = binary_to_json(binary_data)

# Save JSON data to file
json_path = "music_data.json"
with open(json_path, "w") as json_file:
    json.dump(json_data, json_file)

print(f"Binary Data: {binary_data}")
print(f"JSON Data saved to {json_path}")
