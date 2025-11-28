import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import csv_parser

def gpa_to_midpoint(gpa_str):
    mapping = {
        "2.0–2.7": 2.35, "2.7–3.0": 2.85, "3.0–3.3": 3.15,
        "3.3–3.7": 3.5, "3.7–4.0": 3.85
    }
    return mapping.get(str(gpa_str).strip(), 3.5)

def extract_features(row):
    
    # Mapping
    att_map = {"0–60%": 0, "60–80%": 1, "80–90%": 2, "90–100%": 3}
    study_map = {"0-5": 3, "6-10": 8, "11-15": 13, "16-20": 18, "21+": 25}
    load_map = {"8-12 units": 0, "13-14 units": 1, "15-16 units": 4, 
                "17-18 units": 3, "19+ units": 2}
    water_map = {"Less than 1 liter (about 3 cups)": 0, "1–2 liters": 1, 
                 "2–3 liters": 2, "More than 3 liters": 3}
    app_map = {"None": 0, "Paper planner": 1, "Google Calendar": 2, 
               "Todoist or another task manager app": 3, "Other": 4}
    
    # Extracting features by column indices
    features = [
        # 0. Extracurricular (column 1)
        float(row.iloc[1]) if str(row.iloc[1]).replace('.','').isdigit() else 0,
        
        # 1. Attendance (column 2)
        att_map.get(str(row.iloc[2]).strip(), 2),
        
        # 2. Study hours (column 3)
        study_map.get(str(row.iloc[3]).strip(), 10),
        
        # 3. Course load (column 4)
        load_map.get(str(row.iloc[4]).strip(), 2),
        
        # 4. Sleep hours (column 6)
        float(row.iloc[6]) if str(row.iloc[6]).replace('.','').isdigit() else 7,
        
        # 5. Languages (column 8)
        float(row.iloc[8]) if str(row.iloc[8]).isdigit() else 1,
        
        # 6. Water (column 9)
        water_map.get(str(row.iloc[9]).strip(), 1),
        
        # 7. App usage (column 10)
        app_map.get(str(row.iloc[10]).strip(), 2),
        
        # 8. School GPA (column 11) 
        gpa_to_midpoint(row.iloc[11])
    ]
    
    return features

def train_model(df):
    """Trains the model and returns the trained objects"""
    print("Preparing data...")
    
    # Creating features and a target variable
    X = []
    y = []
    
    for i in range(len(df)):
        X.append(extract_features(df.iloc[i]))
        y.append(gpa_to_midpoint(df.iloc[i, -1]))  # College GPA is the last column
    
    X = np.array(X)
    y = np.array(y)
    
    print(f"Data set: {X.shape[0]} notes, {X.shape[1]} features")
    
    # Train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Training the model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    # Evaluatiom
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel trained ✅")
    print(f"MAE (error): {mae:.3f}")
    print(f"R² (quality): {r2:.3f}")
    
    return model, scaler

def predict_gpa(model, scaler, user_row):
    """Predicts GPA for a single user row"""
    user_features = np.array([extract_features(user_row)])
    user_features_scaled = scaler.transform(user_features)
    prediction = model.predict(user_features_scaled)[0]
    return round(prediction, 2)




# main
if __name__ == "__main__":
    try:
        # load
        print("🔄 Loading data...")
        df = csv_parser.load_data()
        user = csv_parser.load_user()
        
        # training
        model, scaler = train_model(df)
        
        # prediction
        predicted_gpa = predict_gpa(model, scaler, user.iloc[0])
        
        print(f"\nPrediction:")
        print(f"Expected College GPA: {predicted_gpa}")
        print(f"Get disappointed in your life!")
        
    except Exception as e:
        print(f"❌❌❌❌ ERROR ❌❌❌❌{e}")
        print("Check for the presence of data files and the csv_parser")
