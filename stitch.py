import cv2
import os

def load_images(image_folder):
    images = []
    for filename in sorted(os.listdir(image_folder)):
        img = cv2.imread(os.path.join(image_folder, filename))
        if img is not None:
            images.append(img)
    return images

def stitch_images(images):
    # Initialize OpenCV's Stitcher
    stitcher = cv2.Stitcher_create()
    
    # Perform stitching
    (status, stitched_image) = stitcher.stitch(images)
    
    if status == cv2.Stitcher_OK:
        print("Panorama stitching completed successfully.")
        return stitched_image
    else:
        print(f"Error during stitching, status code: {status}")
        return None

if __name__ == "__main__":
    image_folder = "./processed_images"  # Folder containing images to stitch
    images = load_images(image_folder)

    if len(images) == 0:
        print("No images found in the specified folder.")
    else:
        panorama = stitch_images(images)

        if panorama is not None:
            cv2.imwrite("stitched_panorama.jpg", panorama)
            print("Panorama saved as 'stitched_panorama.jpg'.")
        else:
            print("Failed to create a panorama.")