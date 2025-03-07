import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

# Load datasets
training_data = pd.read_csv("Data/Training.csv")
testing_data = pd.read_csv("Data/Testing.csv")
symptom_desc = pd.read_csv("MasterData/symptom_Description.csv")
symptom_precaution = pd.read_csv("MasterData/symptom_precaution.csv")
symptom_severity = pd.read_csv("MasterData/Symptom_severity.csv")

# Prepare training data
X_train = training_data.iloc[:, :-1]  # Symptoms
y_train = training_data.iloc[:, -1]   # Disease (Prognosis)

# Encode disease labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)

# Train models
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train_encoded)

svm_classifier = SVC()
svm_classifier.fit(X_train, y_train_encoded)

# Symptom List
symptom_list = list(X_train.columns)

# Function to predict disease
def predict_disease():
    selected_symptoms = [symptom_var.get() for symptom_var in symptom_vars if symptom_var.get() != "None"]
    
    if not selected_symptoms:
        messagebox.showwarning("Warning", "Please select at least one symptom.")
        return

    # Convert symptoms into input vector
    input_vector = [0] * len(symptom_list)
    for symptom in selected_symptoms:
        if symptom in symptom_list:
            input_vector[symptom_list.index(symptom)] = 1

    # Predict disease
    dt_prediction = dt_classifier.predict([input_vector])[0]
    svm_prediction = svm_classifier.predict([input_vector])[0]

    # Decode predictions
    dt_disease = label_encoder.inverse_transform([dt_prediction])[0]
    svm_disease = label_encoder.inverse_transform([svm_prediction])[0]

    # Display results
    disease_label.config(text=f"Predicted Disease: {dt_disease}")

    # Get description
    desc = symptom_desc[symptom_desc.iloc[:, 0] == dt_disease].iloc[:, 1].values
    desc_label.config(text=f"Description: {desc[0]}" if len(desc) > 0 else "Description: Not Available")

    # Get precautions
    precautions = symptom_precaution[symptom_precaution.iloc[:, 0] == dt_disease].values
    if len(precautions) > 0:
        precautions_text = "\n".join([f"- {p}" for p in precautions[0][1:] if str(p) != "nan"])
    else:
        precautions_text = "Not Available"

    precaution_label.config(text=f"Precautions:\n{precautions_text}")

# GUI Setup
root = tk.Tk()
root.title("HealthMate - AI Disease Predictor")
root.geometry("500x500")

# Title
title_label = tk.Label(root, text="HealthMate - AI Disease Predictor", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Symptom Selection
symptom_vars = [tk.StringVar(root) for _ in range(5)]
for var in symptom_vars:
    var.set("None")

symptom_frames = tk.Frame(root)
symptom_frames.pack()

for i in range(5):
    ttk.Label(symptom_frames, text=f"Symptom {i+1}:").grid(row=i, column=0, padx=5, pady=2)
    ttk.Combobox(symptom_frames, textvariable=symptom_vars[i], values=["None"] + symptom_list, width=30).grid(row=i, column=1, padx=5, pady=2)

# Predict Button
predict_button = tk.Button(root, text="Predict Disease", command=predict_disease, font=("Arial", 12), bg="green", fg="white")
predict_button.pack(pady=10)

# Results
disease_label = tk.Label(root, text="Predicted Disease: ", font=("Arial", 12, "bold"))
disease_label.pack(pady=5)

desc_label = tk.Label(root, text="Description: ", wraplength=400, justify="left")
desc_label.pack(pady=5)

precaution_label = tk.Label(root, text="Precautions:", wraplength=400, justify="left")
precaution_label.pack(pady=5)

# Run GUI
root.mainloop()
