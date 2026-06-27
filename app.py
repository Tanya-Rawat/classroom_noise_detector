import streamlit as st
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
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

This project measures classroom noise levels using the microphone and classifies the classroom as:

- 🟢 Quiet
- 🟡 Moderate
- 🔴 Noisy

Click **Start Recording**, record classroom sounds for a few seconds, and then click **Stop Recording**.
""")

# ---------------------------
# AUDIO ANALYSIS
# ---------------------------

def get_volume(audio_bytes):
    try:
        audio = AudioSegment.from_file(
            io.BytesIO(audio_bytes),
            format="webm"
        )

        # Average loudness in dBFS
        db = audio.dBFS

        return db

    except Exception as e:
        st.error(f"Error reading audio: {e}")
        return -90


# ---------------------------
# CLASSIFICATION
# ---------------------------

def classify_noise(db):

    if db < -40:
        return "🟢 QUIET"

    elif db < -25:
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

    db = get_volume(audio["bytes"])

    # Convert dBFS to a 0–100 scale
    meter = max(0, min(100, ((db + 60) / 60) * 100))

    status = classify_noise(db)

    st.subheader("📊 Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Noise Level",
            f"{meter:.1f}/100"
        )

    with col2:
        st.metric(
            "Average Loudness",
            f"{db:.1f} dBFS"
        )

    st.progress(meter / 100)

    if "QUIET" in status:
        st.success(status)

    elif "MODERATE" in status:
        st.warning(status)

    else:
        st.error(status)

    audio_clip = AudioSegment.from_file(
        io.BytesIO(audio["bytes"]),
        format="webm"
    )

    duration = len(audio_clip) / 1000

    st.info(f"🎤 Recording Duration: {duration:.1f} seconds")

    st.markdown("---")

    st.markdown("### 📖 How the Result Was Calculated")

    st.write("""
The microphone records classroom sound.

The application measures the average loudness (dBFS) of the recording.

Based on this value, the classroom is classified as Quiet, Moderate or Noisy.
""")

# ---------------------------
# EDUCATIONAL SECTION
# ---------------------------

st.markdown("---")

st.header("📚 Working Principle")

st.markdown("""
### Input
The microphone records classroom sounds.

### Processing
The recorded audio is analyzed to calculate its average loudness (dBFS).

### Decision
The loudness is compared with predefined thresholds.

### Output
The classroom is classified as:

- 🟢 Quiet
- 🟡 Moderate
- 🔴 Noisy
""")
