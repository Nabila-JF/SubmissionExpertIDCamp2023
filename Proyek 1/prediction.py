import pandas as pd
import joblib

def load_model(model_path):
    return joblib.load(model_path)

def load_encoders(encoder_path):
    return joblib.load(encoder_path)

def load_data(data_path):
    return pd.read_csv(data_path)

def encode_data(data, encoders):
    for column, encoder in encoders.items():
        if column in data.columns:
            data[column] = encoder.transform(data[column])
    return data

def make_predictions(model, data):
    predictions = model.predict(data)
    return predictions

def save_predictions(predictions, output_path):
    output_df = pd.DataFrame({'Prediction': predictions})
    output_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    model_path = 'model/trained_model.pkl'
    encoder_path = 'model/label_encoders.pkl'
    data_path = 'data/new_data.csv'
    output_path = 'data/predictions.csv'
    
    model = load_model(model_path)
    encoders = load_encoders(encoder_path)
    data = load_data(data_path)
    
    # Drop target column if it exists in new data
    if 'Attrition' in data.columns:
        data = data.drop(columns=['Attrition'])
    
    # Drop columns that were not used in model training
    if 'EmployeeId' in data.columns:
        data = data.drop(columns=['EmployeeId'])
    if 'StandardHours' in data.columns:
        data = data.drop(columns=['StandardHours'])
    
    # Encode data
    data = encode_data(data, encoders)
    
    # Make predictions
    predictions = make_predictions(model, data)
    
    # Save predictions
    save_predictions(predictions, output_path)
    
    print(f"Predictions saved to {output_path}")
