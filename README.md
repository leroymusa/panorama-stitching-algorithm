# Panorama Stitching Algorithm

This project provides a set of Python scripts for capturing images from different video streams, preprocessing them, and stitching them into a panorama. The project supports various camera types and allows for dynamic camera selection.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
  - [1. Capture Frames](#1-capture-frames)
  - [2. Preprocess Images](#2-preprocess-images)
  - [3. Stitch Images](#3-stitch-images)
- [Camera Configuration](#camera-configuration)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project includes three main scripts:

1. **Capture Frames**: Captures frames from a selected video stream and saves them as images.
2. **Preprocess Images**: Enhances the captured images using CLAHE (Contrast Limited Adaptive Histogram Equalization).
3. **Stitch Images**: Stitches the preprocessed images into a single panorama.

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/leroymusa/panorama-stitching-algorithm.git
cd panorama-stitching-algorithm
```

### 2. Install Dependencies

Ensure you have Python installed, along with the required libraries. You can install the necessary Python libraries using `pip`:

```bash
pip install opencv-python
```

## Usage

### 1. Capture Frames

Use the `capture_frames.py` script to capture images from a selected camera. The script supports multiple cameras and allows you to select which camera to use. Camera paths should be configured in the script based on your system's setup.

Run the following command to start capturing frames:

```bash
python capture_frames.py
```

The script will prompt you to select a camera from a predefined list. After selecting a camera, you can start capturing images, switch cameras, or exit the script.

### 2. Preprocess Images

Once you have captured the frames, you can preprocess them to enhance image quality using `preprocess_images.py`:

```bash
python preprocess_images.py
```

This script will read images from the `./images` directory, apply CLAHE, and save the processed images in the `./processed_images` directory.

### 3. Stitch Images

Finally, use the `stitch_images.py` script to stitch the preprocessed images into a panorama:

```bash
python stitch_images.py
```

This will create a stitched panorama and save it as `stitched_panorama.jpg`.

## Camera Configuration

The `capture_frames.py` script uses a dictionary to map camera names to their device paths. For security and privacy reasons, dummy camera IDs are used in the public version of the script. To use the script with your specific cameras:

1. Identify the camera device paths on your system.
2. Update the `CAMERAS` dictionary in the script with the appropriate paths.

Example:

```python
CAMERAS = {
    "my_camera": "/dev/v4l/by-id/usb-Your_Camera_ID-video-index0"
}
```

## Requirements

- Python 3.x
- OpenCV
- A camera device (e.g., DroidCam, USB webcams) connected to the system