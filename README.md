# HealthMate

HealthMate is a **Python-based AI-driven healthcare chatbot** that helps users identify potential diseases based on their symptoms. It utilizes **machine learning models** to predict diseases and provides relevant precautions, making healthcare assistance more accessible.

## Features
- **AI-Powered Disease Prediction**: Uses **Decision Tree Classifier** and **Support Vector Machine (SVM)** to diagnose diseases.
- **Interactive Chatbot Interface**: Built using **Tkinter** for a user-friendly desktop GUI.
- **Symptom-Based Diagnosis**: Accepts user-reported symptoms and suggests possible diseases.
- **Severity Analysis**: Determines the urgency of symptoms and suggests if a doctor consultation is necessary.
- **Text-to-Speech Support**: Uses **pyttsx3** to read out diagnoses and precautions.
- **Precaution & Description Database**: Provides explanations and preventive measures for diagnosed diseases.

## Tech Stack
- **Programming Language**: Python
- **Libraries Used**:
  - `pandas`, `numpy` - Data Processing
  - `scikit-learn` - Machine Learning (Decision Tree, SVM)
  - `Tkinter` - GUI Development
  - `pyttsx3` - Text-to-Speech
- **Data Storage**: CSV files (`Training.csv`, `Testing.csv`, `symptom_Description.csv`, `symptom_severity.csv`)

## Installation & Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/shruti110503/HealthMate.git
   cd HealthMate
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```sh
   python chat_bot.py
   ```

## How It Works
1. The user is prompted to enter symptoms.
2. The chatbot analyzes symptoms using a trained **Decision Tree model**.
3. If uncertain, a secondary prediction is made.
4. The chatbot provides:
   - A possible disease diagnosis
   - A description of the disease
   - Suggested precautions
5. If the symptoms indicate severity, it recommends consulting a doctor.

## Screenshots
![Screenshot 2025-03-07 150034](https://github.com/user-attachments/assets/ea23e399-d45d-4e86-b876-ccfb49ca3bf2)
![Screenshot 2025-03-07 150145](https://github.com/user-attachments/assets/c7a6f3b3-a099-471b-8361-8163e394e5e7)


## Future Enhancements
- Improve GUI for better user experience.
- Integrate an API for real-time symptom checking.

## License
This project is licensed under the **MIT License**.

---

Feel free to contribute and improve HealthMate! 🚀


