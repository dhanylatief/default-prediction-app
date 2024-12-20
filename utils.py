import requests
def encode(var=str, values=str):
    """Encode a variable into a list of values."""
    try:
        data = {"Gender": ("Male", "Female"),
                "Marital Status": ("Married", "Single", "Other"),
                "Education": ("Graduate School", "University", "High School", "Others")}
        if var == "Gender":
            return data[var].index(values)
        return data[var].index(values) + 1
    except:
        return
    
def predict(features):
    """Predict default risk using a trained model."""
    URL = "https://default-prediction.onrender.com"
    req = requests.get(URL)
    if req.status_code != 200:
        return 'Error: Cannot connect to server'
    URL += "/predict"
    result = requests.post(URL, json={"data": [features]})
    return result.json()