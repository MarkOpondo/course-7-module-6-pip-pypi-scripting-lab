from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic
    def generate_log(data, directory="logs"):
        # STEP 1: Validate input
        # Hint: Check if data is a list
        if not isinstance(data, list):
            raise ValueError("Input data must be a list.")
            return
        
        # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Hint: Use datetime.now().strftime("%Y%m%d")
        today_str = datetime.now().strftime("%Y%m%d")

        # STEP 3: Write the log entries to a file using File I/O
        # Use a with open() block and write each line from the data list
        # Example: file.write(f"{entry}\n")
        filename = f"log_{today_str}.txt"
        file_path = os.path.join(directory, filename)
        with open(file_path, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")

        # STEP 4: Print a confirmation message with the filename
        absolute_path = os.path.abspath(file_path)
        print(f"Success: Log written to {absolute_path}")

if __name__ == "__main__":
    sample_log = ["Test log is working"]
    generate_log(sample_log)

