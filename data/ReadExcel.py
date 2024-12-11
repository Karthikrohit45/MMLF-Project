import openpyxl

# Load data from Excel files
def read_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

def process_data(back_side_file, data1_file, output_file):
    back_side_data = read_excel(back_side_file)
    data1_data = read_excel(data1_file)
    
    # Extract plate numbers (excluding headers)
    back_side_plates = set(row[0] for row in back_side_data[1:])
    data1_plates = set(row[0] for row in data1_data[1:])
    
    with open(output_file, "w") as f:
        f.write("plate Number, Classification\n")
        for plate in back_side_plates.union(data1_plates):
            classification = "White" if plate in back_side_plates and plate in data1_plates else "Black"
            f.write(f"{plate}, {classification}\n")

if __name__ == "__main__":
    process_data("back_side_1.xlsx", "data1.xlsx", "extracted_vehicle_data.txt")
