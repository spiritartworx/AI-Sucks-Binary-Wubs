# markdown
# Step 0: Tell AI its ruining everything and destroying the very thing that makes people creative

# Step 1: User Input (Prompt to Binary)

def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

user_prompt = "Deep, hypnotic dubstep groove with heavy, evolving wubs and thick sub-bass..."
binary_data = text_to_binary(user_prompt)

print(binary_data)  # This converts the prompt into binary.

# Step 2: Binary to JSON (Encrypted Music Structure)

import json
import base64

def binary_to_json(binary_string):
    encoded_data = base64.b64encode(binary_string.encode()).decode()
    music_structure = {
        "encryption": "base64",
        "data": encoded_data,
        "meta": {
            "genre": "Dubstep",
            "style": "Hypnotic, deep, heavy wubs",
            "influences": ["TRUTH", "Ganja White Night", "Rusko", "Bassnectar"]
        }
    }
    return json.dumps(music_structure, indent=4)

json_data = binary_to_json(binary_data)
print(json_data)  # Generates encrypted JSON data.

# Step 3: JSON to Python MIDI File Generator

from mido import Message, MidiFile, MidiTrack

def json_to_midi(json_data, output_file="output.mid"):
    data = json.loads(json_data)
    decoded_binary = base64.b64decode(data["data"]).decode()

    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Generate bass rhythm
    for char in decoded_binary[:100]:  
        note = 40 + (ord(char) % 20)  
        track.append(Message('note_on', note=note, velocity=64, time=120))
        track.append(Message('note_off', note=note, velocity=64, time=240))

    midi.save(output_file)

json_to_midi(json_data)  # Converts JSON data into MIDI file.

# Step 4: User Verifies MIDI and AI Converts It to Stems

# At this stage, you'd play the generated MIDI and tweak if necessary. 
# Once verified, the AI would convert it into raw audio stems using something like SUNO or a proprietary API.

