import streamlit as st
import pickle
import numpy as np

with open("C:\\Users\\Kiruthika Karthikeya\\Desktop\\Project-3 Carprice\\car_price_model.pkl", 'rb') as f:
    model = pickle.load(f)

features = ['Mileage_km', 'Number owner', 'Mileage', 'Engine', 'Torque', 'Max Power',  
            'Seats', 'Age of car', 'Body_Type', 'Fuel_Type', 'Transmission type']

categorical_mappings = {
    'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'Cng': 2, 'Electric': 3, 'Lpg': 4},
    'Body_Type': {'Hatchpack': 0, 'SUV': 1, 'Sedan': 2, 'MUV': 3, 'Minivans': 4, 'Coupe': 5,
                  'Pickup Trucks': 6, 'Convertibles': 7, 'Hybrids': 9, 'Wagon': 10},  
    'Transmission type': {'Manual': 0, 'Automatic': 1},
}

st.title("CAR DHEKO - CAR PRICE PREDICTION APPLICATION")

st.sidebar.title("Please provide the car details below:")

input_data = {}

for feature in features:
    if feature in categorical_mappings:
        selected_option = st.sidebar.selectbox(
            f"Select {feature.replace('_', ' ').capitalize()}:",
            options=list(categorical_mappings[feature].keys()),
            help=f"Choose the {feature.replace('_', ' ').capitalize()} of the car."
        )
        input_data[feature] = categorical_mappings[feature][selected_option]
    else:
        if feature == 'Mileage_km':
            input_data[feature] = st.sidebar.number_input(
                f"{feature.replace('_', ' ').capitalize()}:",
                help="Enter the car's mileage in kilometers."
            )
        elif feature == 'Engine':
            input_data[feature] = st.sidebar.number_input(
                f"{feature.replace('_', ' ').capitalize()}:",
                help="Enter the engine capacity in CC (e.g., 1500 for 1.5L)."
            )
        else:
            input_data[feature] = st.sidebar.number_input(
                f"{feature.replace('_', ' ').capitalize()}:",
                help=f"Enter the value for {feature.replace('_', ' ').capitalize()}."
            )

if st.sidebar.button("CLICK"):
    input_array = np.array([input_data[feature] for feature in features]).reshape(1, -1)

    prediction = model.predict(input_array)
    formatted_prediction = f"INR {prediction[0]:,.2f}"
    
    st.subheader("Selected Feature Values:")
    for feature, value in input_data.items():
        st.write(f"{feature.replace('_', ' ').capitalize()}: {value}")
    
    st.subheader("Prediction Result:")
    st.write(f"***THE ESTIMATED CAR PRICE*** : {formatted_prediction}")