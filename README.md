# Classroom Noise Detection System

A simple Streamlit application that records classroom audio using the browser microphone and classifies the classroom as **Quiet**, **Moderate**, or **Noisy** based on the recorded sound level.


## Project Structure

```
Classroom_Noise_Detector/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
```

---

## Technologies Used

- Python
- Streamlit
- streamlit-mic-recorder
- PyDub
- NumPy
- FFmpeg

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/classroom-noise-detector.git

cd classroom-noise-detector
```

### 2. Install Python packages

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Ubuntu / Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS

```bash
brew install ffmpeg
```

#### Windows

Download FFmpeg from:

https://ffmpeg.org/download.html

---

## Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your web browser.

---

## How It Works

1. Click **Start Recording**.
2. Record classroom sounds for a few seconds.
3. Click **Stop Recording**.
4. The application analyzes the recorded audio.
5. The average loudness is calculated.
6. The classroom is classified as:

- Quiet
- Moderate
- Noisy

---

## Noise Classification

| Loudness (dBFS) | Classroom Status |
|-----------------|------------------|
| Less than -40 | Quiet |
| -40 to -25 | Moderate |
| Greater than -25 | Noisy |

---

## Requirements

Python 3.9 or later

Packages used:

- streamlit
- streamlit-mic-recorder
- pydub
- numpy

System dependency:

- FFmpeg

---

## License

This project is created for educational purposes and may be freely used and modified for learning.
