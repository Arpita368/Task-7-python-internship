# Task 7: Image Resizer Tool

## Objective
Resize images in batch while maintaining the aspect ratio. This script allows you to resize all images in a folder to a specific width automatically.

## Tools Used
- Python 3.x
- Pillow library (`pip install Pillow`)

## How It Works
1. Place all images you want to resize in a folder (e.g., `images`).
2. The script reads all image files with extensions: `png, jpeg, jpg, iso, gif`.
3. Each image is resized to a specified width (e.g., `400` pixels) while maintaining the original aspect ratio.
4. Resized images are saved in the same folder with `_resized` added to the filename.

## Setup Instructions
1. Install Python 3 if not already installed.
   
2. Install Pillow library:
   ```bash
   pip install Pillow

3. Place your images in a folder and update the path in the script:
```
files = os.listdir(r'C:\path\to\your\images')
```

4. Set the desired new width in the script:
```
resized_image = resize(im, 2100)
```

5.Run the script:
```
python image_resizer.py
```

6. Check the folder — resized images will appear with _resized in their filenames.

## Notes
1. The aspect ratio of images is maintained to avoid stretching.
2. Only files with the extensions mentioned above will be resized.
3. You can modify the script to save resized images in a separate folder to avoid overwriting originals.

## Author
Created by Arpita Jitendra Sonparote
