# 🔊 Classroom Noise Detection System

A simple Python project that detects and measures classroom noise levels using a microphone. The system classifies the environment as **Quiet**, **Moderate**, or **Noisy** and displays the result through a Streamlit web application.

## 📌 Objective

To help students understand how sound data can be collected, processed, and analyzed using Python.

## 🚀 Features

* Real-time noise measurement using a microphone
* Noise level classification

  * 😊 Quiet
  * 😐 Moderate
  * 🔊 Noisy
* User-friendly Streamlit interface
* Displays noise level and classroom status

## 🛠 Technologies Used

* Python
* Streamlit
* NumPy
* SoundDevice
* Pandas

## 📂 Project Structure

```text
ClassroomNoiseDetector/
│
├── app.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open the link shown in the terminal to view the application in your browser.

## ⚙️ How It Works

1. The microphone records sound from the classroom.
2. Python calculates the sound intensity.
3. The sound level is compared with predefined thresholds.
4. The classroom is classified as Quiet, Moderate, or Noisy.
5. The result is displayed on the screen.

## 👨‍🎓 Educational Value

This project demonstrates the **Input → Process → Output** model and introduces students to:

* Audio sensing
* Data processing
* Python programming
* Basic data analysis
* Real-world problem solving
