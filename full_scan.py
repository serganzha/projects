import csv
import datetime
import os
from pathlib import Path
from tqdm import tqdm


def get_directory_path():
    """Prompt the user for the path to the directory to scan and validate it."""
    while True:
        drive_path = input("Enter the path to the directory to scan: ")
        path = Path(drive_path).resolve()
        if path.is_dir():
            return path
        else:
            print("The specified path is not a directory.")


if __name__ == "__main__":
    # Import the datetime module
    # Validate the user input for the drive path
    while True:
        try:
            drive_path = get_directory_path()
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received. Program will exit.")
            exit()
        except Exception as e:
            print(f"Error: {e}")

    # Generate a unique filename for the output CSV file
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"file_names_{timestamp}.csv"

    # Open the CSV file for writing and define the fieldnames
    with open(filename, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["file_path", "file_name", "file_size"])

        # Walk through the directory tree and write data to the CSV file
        num_files = 0
        for root, dirs, files in os.walk(drive_path):
            num_files += len(files)
        with tqdm(total=num_files, desc='Progress', unit=' files', leave=True) as pbar:
            try:
                for root, dirs, files in os.walk(drive_path):
                    for file_name in files:
                        file_path = Path(root) / file_name
                        if not file_path.is_file():
                            continue  # skip directories

                        # Get the file size in gigabytes and round to two decimal places
                        file_size = round(file_path.stat().st_size / (1024 * 1024 * 1024), 2)

                        # Split the file path into directory and file components
                        file_dir, file_name = os.path.split(file_path)

                        # Write the file path, name, and size to the CSV file
                        data = [str(file_dir), str(file_name), file_size]
                        csv_writer.writerow(data)

                        pbar.update(1)

            except Exception as e:
                print(f"Error: {e}")
                exit()

    print(f"{num_files} file names have been recorded and written to {filename}")
