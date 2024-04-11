import os
import random
from tkinter import filedialog
# Define the directory to search
directory = filedialog.askdirectory()

# Define the subdirectory name (create it if it doesn't exist)
subdirectory_name = "randomized_files"

# Function to check file type (modify based on your needs)
def is_desired_type(file):
  return file.endswith(".mp3")  # Example: Check for MP3 files

def swap_filenames_and_move(filenames):
  # Create the subdirectory if it doesn't exist
  os.makedirs(os.path.join(directory, subdirectory_name), exist_ok=True)

  # Shuffle the list of filenames randomly
  random.shuffle(filenames)

  # Rename and move files based on the shuffled order
  for i in range(len(filenames)):
    old_path = os.path.join(directory, filenames[i])
    new_filename = filenames[random.randint(0, len(filenames)-1)]
    # Ensure different filenames before moving (avoid overwriting)
    while os.path.exists(os.path.join(directory, subdirectory_name, new_filename)):
      # Choose another random filename from the shuffled list
      new_filename = filenames[random.randint(0, len(filenames)-1)]
    new_path = os.path.join(directory, subdirectory_name, new_filename)
    os.rename(os.path.join(directory, filenames[i]), new_path)

# Find all files of the desired type
filenames = [filename for filename in os.listdir(directory) if is_desired_type(filename)]

# Check if any files found
if filenames:
  print(f"Found {len(filenames)} files. Swapping names and moving to '{subdirectory_name}'...")
  swap_filenames_and_move(filenames)
  print("Done!")
else:
  print("No files of the desired type found.")

def is_desired_type(file):
  return file.endswith(".ogg")  # Example: Check for MP3 files

def swap_filenames_and_move(filenames):
  # Create the subdirectory if it doesn't exist
  os.makedirs(os.path.join(directory, subdirectory_name), exist_ok=True)

  # Shuffle the list of filenames randomly
  random.shuffle(filenames)

  # Rename and move files based on the shuffled order
  for i in range(len(filenames)):
    old_path = os.path.join(directory, filenames[i])
    new_filename = filenames[random.randint(0, len(filenames)-1)]
    # Ensure different filenames before moving (avoid overwriting)
    while os.path.exists(os.path.join(directory, subdirectory_name, new_filename)):
      # Choose another random filename from the shuffled list
      new_filename = filenames[random.randint(0, len(filenames)-1)]
    new_path = os.path.join(directory, subdirectory_name, new_filename)
    os.rename(os.path.join(directory, filenames[i]), new_path)

# Find all files of the desired type
filenames = [filename for filename in os.listdir(directory) if is_desired_type(filename)]

# Check if any files found
if filenames:
  print(f"Found {len(filenames)} files. Swapping names and moving to '{subdirectory_name}'...")
  swap_filenames_and_move(filenames)
  print("Done!")
else:
  print("No files of the desired type found.")