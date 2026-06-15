from datetime import datetime
import os

# TODO: Implement log generation logic
def generate_log(data, directory=None):
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")
        return
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
            file_path = os.path.join(directory, filename)
        else:
            file_path = filename
            
    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    with open(file_path, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    absolute_path = os.path.abspath(file_path)
    print(f"Success: Log written to {absolute_path}")

    return file_path

if __name__ == "__main__":
    sample_log = ["Test log is working"]
    generate_log(sample_log)

