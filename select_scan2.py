import csv
import datetime
import os
from pathlib import Path
from tkinter import filedialog, Tk
from tqdm import tqdm


def get_directory_paths():
    """Prompt the user for the paths to the directories to scan and validate them."""
    root = Tk()
    root.withdraw()
    directories = []
    while True:
        dir_path = filedialog.askdirectory(title="Select a directory to scan", mustexist=True)
        if not dir_path:
            break  # user cancelled
        path = Path(dir_path).resolve()
        if path.is_dir():
            directories.append(path)
        else:
            print(f"{path} is not a valid directory.")
    return directories


if __name__ == "__main__":
    # Validate the user input for the drive paths
    while True:
        try:
            drive_paths = get_directory_paths()
            if len(drive_paths) == 0:
                print("No valid directories selected. Program will exit.")
                exit()
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
        # Define the writer object
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Loop through the directories and write data to a separate CSV tab for each directory
        for drive_path in drive_paths:
            # Initialize the directory-specific tab and write the header row
            directory_tab = csv.writer(f, quoting=csv.QUOTE_ALL)
            directory_tab.writerow(["file_path", "file_name", "file_size"])

            # Walk through the directory tree and write data to the directory-specific tab
            num_files = 0
            for root, dirs, files in os.walk(drive_path):
                num_files += len(files)
            with tqdm(total=num_files, desc=f'Progress for {drive_path}', unit=' files', leave=True) as pbar:
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

                            # Write the file path, name, and size to the directory-specific tab
                            data = [str(file_dir), str(file_name), file_size]
                            directory_tab.writerow(data)

                            pbar.update(1)

                except Exception as e:
                    print(f"Error: {e}")
                    exit()

    print(f"All file names have been recorded and written to {filename}")
