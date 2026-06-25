import streamlit as st
import sounddevice as sd
import numpy as np
import pandas as pd
from datetime import datetime

# -------------------------
# PAGE TITLE
# -------------------------

st.set_page_config(
    page_title="Classroom Noise Detector",
    page_icon="🔊",
    layout="centered"
)

st.title("🔊 Classroom Noise Detection System")
st.subheader("A Python Project for Grades 8–10")

st.markdown("""
### Project Objective
This project monitors classroom noise levels using a microphone.

The system classifies the environment as:

- 😊 Quiet
- 😐 Moderate
- 🔊 Noisy

Click the button below to measure the current noise level.
""")

# -------------------------
# NOISE DETECTION FUNCTION
# -------------------------

def get_noise_level():

    duration = 5
    sample_rate = 44100

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    volume = np.linalg.norm(recording)

    return volume

# -------------------------
# CLASSIFICATION FUNCTION
# -------------------------

def classify_noise(volume):

    if volume < 10:
        return "😊 QUIET"

    elif volume < 30:
        return "😐 MODERATE"

    else:
        return "🔊 NOISY"

# -------------------------
# BUTTON
# -------------------------

if st.button("Measure Classroom Noise"):

    with st.spinner("Listening..."):

        volume = get_noise_level()

        status = classify_noise(volume)

    st.success("Measurement Complete")

    st.metric(
        label="Noise Level",
        value=f"{volume:.2f}"
    )

    st.subheader("Classroom Status")

    if "QUIET" in status:
        st.success(status)

    elif "MODERATE" in status:
        st.warning(status)

    else:
        st.error(status)

    # Save data

    data = pd.DataFrame({
        "Time": [datetime.now()],
        "Noise Level": [round(volume, 2)],
        "Status": [status]
    })

    st.subheader("Recorded Reading")
    st.dataframe(data)

# -------------------------
# HOW IT WORKS
# -------------------------

st.markdown("""
---
## How It Works

### Step 1
The microphone records sound from the classroom.

### Step 2
Python calculates the sound intensity.

### Step 3
The program compares the value with predefined limits.

### Step 4
The classroom is classified as:

- Quiet
- Moderate
- Noisy

### Output
The result is displayed on the screen.
""")

st.markdown("""
---
### Developed Using

- Python
- Streamlit
- NumPy
- SoundDevice
""")