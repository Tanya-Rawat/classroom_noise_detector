import streamlit as st
from streamlit_mic_recorder import mic_recorder
import numpy as np
import wave
import io

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Classroom Noise Detector",
    page_icon="🔊",
    layout="centered"
)

st.title("🔊 Classroom Noise Detection System")
st.subheader("A Python Project for Grades 8–10")

st.markdown("""
### Objective

This project measures classroom noise levels using a microphone and classifies the environment as:

- 🟢 Quiet
- 🟡 Moderate
- 🔴 Noisy

Press **Start Recording**, record classroom sounds, then press **Stop Recording**.
""")

# ---------------------------
# ANALYZE AUDIO
# ---------------------------

def get_volume(audio_bytes):
    try:
        wav_file = wave.open(io.BytesIO(audio_bytes), "rb")

        frames = wav_file.readframes(wav_file.getnframes())

        audio_array = np.frombuffer(frames, dtype=np.int16)

        rms = np.sqrt(np.mean(audio_array.astype(np.float64) ** 2))

        return rms

    except Exception:
        return 0


def classify_noise(volume):

    if volume < 500:
        return "🟢 QUIET"

    elif volume < 3000:
        return "🟡 MODERATE"

    else:
        return "🔴 NOISY"


# ---------------------------
# MICROPHONE
# ---------------------------

st.subheader("🎤 Record Classroom Sound")

audio = mic_recorder(
    start_prompt="▶️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=True,
    use_container_width=True
)

# ---------------------------
# RESULT
# ---------------------------

if audio:

    st.audio(audio["bytes"])

    volume = get_volume(audio["bytes"])

    status = classify_noise(volume)

    st.subheader("📊 Analysis Result")

    st.metric(
        label="Measured Noise Level",
        value=f"{volume:.0f}"
    )

    if "QUIET" in status:
        st.success(status)

    elif "MODERATE" in status:
        st.warning(status)

    else:
        st.error(status)

    st.markdown("---")

    st.markdown("### How the Result Was Calculated")

    st.write(
        "The recorded audio was analyzed and its average sound intensity "
        "was calculated. Higher intensity means a noisier classroom."
    )

# ---------------------------
# EDUCATIONAL SECTION
# ---------------------------

st.markdown("---")

st.header("📚 Working Principle")

st.markdown("""
### Input
Microphone records classroom audio.

### Processing
Python calculates the sound intensity of the recording.

### Decision
The sound level is compared against predefined thresholds.

### Output
The classroom is classified as:

- Quiet
- Moderate
- Noisy
""")

st.markdown("---")

st.header("🚀 Future Improvements")

st.markdown("""
- Live noise monitoring
- Daily noise reports
- Graphs and statistics
- Teacher alerts
- AI-based sound classification
""")
