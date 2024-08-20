

#### INSTRUCTION 
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------

`pyttsx3` does not natively support saving text to an audio file in formats like MP3. Instead, you can use the `gtts` (Google Text-to-Speech) library for this purpose. Here's how you can modify the assignments to incorporate `gtts` for saving the text to an audio file.

### **Saving Text to Audio Using `gtts`**

For **Assignment** where saving output to mp3 please   following this instructions:


1. **Install `gtts` Library**: Guide the students to install the `gtts` library by running the following command:
   ```bash
   pip install gtts
   ```

2. **Save Text as Audio Using `gtts`**:
   Replace the `pyttsx3` code snippet for saving text to audio with the following `gtts` code:
   ```python
   from gtts import gTTS

   text = "This is a text to speech example."
   tts = gTTS(text=text, lang='en')
   tts.save("output.mp3")
   ```

3. **Example of Combining `pyttsx3` for Voice Control with `gtts` for Saving Audio**:
   If you still want to use `pyttsx3` for selecting voices and controlling speech rate, you can combine it with `gtts` like this:

   ```python
   import pyttsx3
   from gtts import gTTS

   def get_text_from_file(filename):
       with open(filename, "r") as file:
           return file.read()

   def change_voice(engine, voice_index=0):
       voices = engine.getProperty('voices')
       engine.setProperty('voice', voices[voice_index].id)

   def convert_text_to_speech(text, voice_index=0, rate=130):
       engine = pyttsx3.init()
       change_voice(engine, voice_index)
       engine.setProperty('rate', rate)
       engine.say(text)
       engine.runAndWait()

   def save_speech_to_file(text, filename="output.mp3", lang='en'):
       tts = gTTS(text=text, lang=lang)
       tts.save(filename)

   if __name__ == "__main__":
       # Example text
       text = get_text_from_file("data.txt")

       # Convert to speech and play
       convert_text_to_speech(text, voice_index=0, rate=130)

       # Save to audio file
       save_speech_to_file(text, filename="output.mp3")
   ```

**Deliverables Update:**  
- **Assignment 1**: Submit the Python script and the generated audio file using `gtts`.
- **Assignment 2 and beyond**: Include both the `pyttsx3` and `gtts` code in the deliverables, demonstrating how you control the voice and rate with `pyttsx3` and save the final output with `gtts`.





------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
### ASSIGNMENT 

references 1: [Click here to view examples and reference for pyttsx3](https://github.com/nateshmbhat/pyttsx3)
references 2: [Click here to view examples and reference for gTTS](https://github.com/pndurette/gTTS)

### **Assignment 1: Basic Text-to-Speech Conversion**
**Objective:** Familiarize with the basic usage of `pyttsx3` for converting text to speech.

**Tasks:**
1. Install the `pyttsx3` library in your Python environment. using ``` pip install pyttsx3```
2. Write a Python script that initializes the `pyttsx3` engine.
3. Convert a simple text string (e.g., "Hello, world!") into speech using `pyttsx3`.
4. Save the speech output to a file (`output.mp3`).
5. Run your script and listen to the generated speech file.

**Deliverable:** Submit the Python script and the generated audio file.

### **Assignment 2: Exploring and Changing Voice Properties**
**Objective:** Learn to change the voice and rate of speech.

**Tasks:**
1. Modify the script from Assignment 1 to print all available voices on your system.
2. Experiment with different voice options. Select at least two different voices and use them to convert a text string into speech.
3. Adjust the speech rate (speed) to be faster and slower. Experiment with at least three different rates.
4. Save each variation (voice and rate) as a separate audio file.

**Deliverable:** Submit the Python script, along with audio files for each voice and rate variation.

### **Assignment 3: Reading from a File and Advanced Voice Manipulation**
**Objective:** Integrate file handling and more advanced voice settings.

**Tasks:**
1. Write a Python script that reads the content of a text file (`data.txt`) and converts the entire content into speech.
2. Implement a function that allows the user to select a voice and rate before converting the text to speech.
3. Allow the user to save the output in a specified audio format (e.g., `.mp3` or `.wav`).
4. Test your script with a sample text file and save the output.

**Deliverable:** Submit the Python script, the sample text file, and the resulting audio file.

### **Assignment 4: Creating a Voice-Based Application**
**Objective:** Develop a small voice-based application that demonstrates practical use of TTS.

**Tasks:**
1. Build a command-line application that prompts the user to input a text string or select a text file.
2. The application should allow the user to:
   - Choose a voice.
   - Adjust the speech rate.
   - Save the output as an audio file.
   - Play the generated speech immediately after conversion.
3. Include error handling for scenarios like invalid file paths, unsupported formats, etc.
4. Optionally, add a feature that allows the user to change the volume of the speech.

**Deliverable:** Submit the complete Python application and documentation explaining how to use it.

### **Assignment 5: Integrating TTS with a GUI**
**Objective:** Create a graphical user interface (GUI) for a TTS application using `tkinter` or another GUI framework.

**Tasks:**
1. Design a simple GUI that allows users to:
   - Input text or select a text file.
   - Choose a voice from a dropdown menu.
   - Adjust the speech rate and volume using sliders.
   - Convert the text to speech and save the output.
2. Ensure the GUI is user-friendly and provides real-time feedback (e.g., displaying the selected voice name).
3. Implement a “Preview” button that plays the generated speech without saving it.
4. Test the application thoroughly to ensure it works smoothly.

**Deliverable:** Submit the Python script for the GUI application and a short video demonstrating its usage.

### **Assignment 6: Advanced Features - Multi-Language Support and Custom Voice Integration**
**Objective:** Implement advanced features such as multi-language support and integration of custom voices.

**Tasks:**
1. Modify the existing TTS application to support multiple languages.
2. Research how to integrate custom voices or third-party TTS engines (e.g., Google TTS) into your application.
3. Add a feature that allows users to switch between different languages and voices dynamically.
4. Document the process of integrating a custom voice or external TTS engine.

**Deliverable:** Submit the enhanced Python application, a report detailing the integration process, and an example output for each supported language.

### **Final Project: Voice-Enabled Digital Assistant**
**Objective:** Combine all the skills learned to create a fully functional voice-enabled digital assistant.

**Tasks:**
1. Build a digital assistant that can:
   - Respond to user queries (using pre-defined text responses).
   - Read news headlines or information from a web source using web scraping.
   - Provide weather updates by integrating with an external API.
   - Save important reminders or notes as speech files.
2. Implement voice recognition to trigger the assistant with a specific phrase (optional).
3. Test the assistant in various scenarios and document its features.

**Deliverable:** Submit the complete digital assistant application, along with documentation and a demonstration video.

---
