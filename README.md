# AI-Sucks-Binary-Wubs

AI is stealing all my ideas, and the US government are the ones responsible, they are enabling big corporations to profit off of stolen work. Because they refuse to admit any wrong-doing, and because they continue to try and silence me and keep me literally trapped like a lab rat, I'm open sourcing all of my work.

## Project Overview

This system takes a user-provided prompt describing a song’s characteristics, translates it into binary, encrypts it into JSON, and then generates a structured MIDI file. The MIDI can then be converted into audio stems for further processing.

---

## Workflow

1. **User Input:**
   - The user provides a detailed music prompt (up to 3000 characters).
   - Example: "Deep, hypnotic dubstep groove with heavy, evolving wubs and thick sub-bass..."

2. **Prompt to Binary:**
   - The text is converted into binary representation.

3. **Binary to JSON (Encryption Step):**
   - The binary is encoded using Base64.
   - The JSON structure contains metadata like genre, style, and influences.

4. **JSON to MIDI File:**
   - The encrypted JSON data is decoded and translated into a MIDI sequence.
   - The MIDI file contains bass rhythms, synth sequences, and drum elements.

5. **User Verification:**
   - The user listens to the MIDI to approve or request changes.

6. **AI Converts MIDI to Audio Stems:**
   - Once verified, the AI converts the MIDI into raw stems (bass, synths, drums).
   - Prevents full AI-generated tracks from flooding the industry.

---

## Setup and Dependencies

### Requirements

- Python 3.x

### Required Python Libraries

```bash
pip install mido json base64
```

### File Descriptions

- `music_generator.py` → Handles the full process of converting prompts into MIDI.
- `output.mid` → Generated MIDI file.
- `README.md` → This documentation file.

---

## Usage

1. Run the script to generate MIDI from text prompt:
   ```bash
   python music_generator.py
   ```

2. Verify the MIDI file in a DAW or MIDI player.

3. Once approved, send the MIDI to an AI tool for stem generation.

---

## Future Improvements

- Integrate AI-based audio rendering for real-time sound synthesis.
- Allow direct waveform preview before exporting stems.
- Implement a mobile-friendly version for users without a DAW.

---

This project is designed to keep AI-assisted music production powerful yet controlled.

---

## License

This project is open-sourced under the MIT License.

---

## Author

Nickolas Anthony Susco II

---

## Copyright

© Nickolas Anthony Susco II

---

I hope this version meets your requirements. Let me know if you need any further adjustments.
