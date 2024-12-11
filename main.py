from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load data from Excel files
def load_data():
    try:
        # Load back_side_1.xlsx
        back_side_df = pd.read_excel('/Users/karthik/Desktop/MMLF_Project/data/back_side_1.xlsx')

        # Load data1.xlsx
        data1_df = pd.read_excel('/Users/karthik/Desktop/MMLF_Project/data/data1.xlsx')

        return back_side_df, data1_df  # Return DataFrames if loading is successful

    except Exception as e:
        # Raise a ValueError with details if there's an issue
        raise ValueError(f"Error loading data: {str(e)}")

# Define classification based on matching plate numbers
def classify_customer(plate_number, back_side_df, data1_df):
    # Check if the required column exists in both datasets
    if 'plate_number' not in back_side_df.columns or 'plate_number' not in data1_df.columns:
        raise ValueError("Missing 'plate_number' column in one of the files.")

    # Check if the plate_number exists in both files
    is_in_back_side = plate_number in back_side_df['plate_number'].values
    is_in_data1 = plate_number in data1_df['plate_number'].values

    # Determine classification
    if is_in_back_side and is_in_data1:
        return 'White'  # Both files have the plate number, classified as White
    else:
        return 'Black'  # One or both files don't have the plate number, classified as Black

@app.get("/test-load-data")
async def test_load_data():
    try:
        # Load datasets
        back_side_df, data1_df = load_data()

        # Return a preview of both datasets
        return {
            "back_side": back_side_df.head().to_dict(),
            "data1": data1_df.head().to_dict(),
        }

    except ValueError as ve:
        # Return specific error from data loading
        return {"error": str(ve)}

    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"Unexpected error: {str(e)}"}

# Endpoint to classify a vehicle based on its plate number
@app.get("/classify/{plate_number}")
async def classify_vehicle(plate_number: str):
    try:
        # Load datasets
        back_side_df, data1_df = load_data()

        # Classify the vehicle using the plate number
        classification = classify_customer(plate_number, back_side_df, data1_df)

        # Write the result to a file
        with open("camera/extracted_vehicle_data.txt", "w") as file:
            file.write("plate Number, Classification\n")
            file.write(f"{plate_number}, {classification}\n")

        return {"plate_number": plate_number, "classification": classification}

    except ValueError as ve:
        # Return specific error from data loading
        return {"error": str(ve)}

    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"Unexpected error: {str(e)}"}

