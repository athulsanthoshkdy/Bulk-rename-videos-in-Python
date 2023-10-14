import os
import ffmpeg

# Directory containing your videos
input_directory = 'D:/New folder (2)/input'

# Directory to save processed videos
output_directory = 'D:/New folder (2)/output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# List all video files in the input directory and sort them by creation date
video_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
video_files.sort(key=lambda x: os.path.getctime(os.path.join(input_directory, x)))

# Counter to generate incremented numbers

counter = 1

#print("List of video files to process:")
#print(video_files)

for video_file in video_files:
    input_path = os.path.join(input_directory, video_file)
    
    # Generate a custom name with an incremented number
    custom_name = f'Custom name {counter}.mp4'  # Modify the file extension as needed
    
    output_path = os.path.join(output_directory, custom_name)

    #you can also modify the videos using libraries like ffmpeg and save it to the different output folder if required.

    try:
        # Step 1: Rename the video
        os.rename(input_path, os.path.join(input_directory, custom_name))
        
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}. Skipping this file.")
    
    # Increment the counter for the next video
    counter += 1

print('All videos have been renamed with incremented numbers in order of creation date.')
