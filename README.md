# MMLF Project (Multi-Modal Lane Following)

## Overview
The **MMLF Project** is a FastAPI-based application that classifies vehicles into "White" or "Black" customers based on their license plate numbers. It processes and compares vehicle data from two `.xlsx` files (`data1.xlsx` and `back_side_1.xlsx`) and generates results in an output file `extracted_vehicle_data.txt`.

## Features
- **File Processing**: Reads data from Excel files.
- **Vehicle Classification**: Classifies vehicles based on matching criteria between the two files.
- **REST API**: Provides endpoints to classify vehicles and verify the data.
- **FastAPI Documentation**: Includes Swagger UI and ReDoc for API exploration.

## Technologies Used
- **Python**: Core programming language.
- **FastAPI**: Framework for building the API.
- **Pandas**: For data manipulation and processing.
- **OpenPyXL**: To handle Excel files.
- **Uvicorn**: ASGI server for running the application.

## Prerequisites
- Python 3.8 or later
- Virtual environment (recommended)
- Required Python libraries:
  - fastapi
  - uvicorn
  - pandas
  - openpyxl

## Project Directory Structure
```
MMLF_Project/
|-- camera/
|   |-- extracted_vehicle_data.txt
|
|-- data/
|   |-- data1.xlsx
|   |-- back_side_1.xlsx
|   |-- ReadExcel.py
|
|-- main.py
|-- venv/
|-- README.md
```

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd MMLF_Project
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the Required Files Are in Place**
   - Place `data1.xlsx` and `back_side_1.xlsx` in the `data` folder.

5. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. Classify Vehicle
**Endpoint:** `/classify/{plate_number}`

- **Description:** Classifies a vehicle based on its plate number.
- **Method:** `GET`
- **Parameters:**
  - `plate_number` (string, required): The license plate number of the vehicle.

**Example Curl Command:**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/classify/KA79B6527' -H 'accept: application/json'
```

**Expected Output:**
- For matching vehicles in both files:
  ```json
  {
    "plate_number": "KA79B6527",
    "classification": "White"
  }
  ```
- For non-matching vehicles:
  ```json
  {
    "plate_number": "KA79B6527",
    "classification": "Black"
  }
  ```

### 2. Test Load Data
**Endpoint:** `/test-load-data`

- **Description:** Tests the loading of the Excel files.
- **Method:** `GET`

**Example Curl Command:**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/test-load-data' -H 'accept: application/json'
```

**Expected Output:**
Preview of the data from the two Excel files.

## Usage Instructions

1. **Access Swagger UI**
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to test the API endpoints interactively.

2. **Access ReDoc**
   Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) for a detailed API documentation.

3. **Check the Output**
   After classifying a vehicle, the results will be written to `camera/extracted_vehicle_data.txt`.

## Common Issues and Solutions

- **Missing File Error:** Ensure that `data1.xlsx` and `back_side_1.xlsx` exist in the `data` folder.
- **Format Issues:** Verify that the Excel files are in proper `.xlsx` format. Use tools like Microsoft Excel or Google Sheets to save the files correctly.
- **Port Already in Use:** Kill any existing process using port 8000:
  ```bash
  lsof -i :8000
  kill -9 <PID>
  ```

## Contributing
Contributions are welcome! Feel free to open issues or create pull requests to improve the project.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

-----

