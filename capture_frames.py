import cv2
import os

# Dictionary of camera names and their device paths (dummy paths for example)
CAMERAS = {
    "camera_1": "/dev/v4l/by-id/usb-CAMERA_1_ID-video-index0",
    "camera_2": "/dev/v4l/by-id/usb-CAMERA_2_ID-video-index0",
    "camera_3": "/dev/v4l/by-id/usb-CAMERA_3_ID-video-index0",
    "camera_4": "/dev/v4l/by-id/usb-CAMERA_4_ID-video-index0",
    "camera_5": "/dev/v4l/by-id/usb-CAMERA_5_ID-video-index0",
    "camera_6": "/dev/v4l/by-id/usb-CAMERA_6_ID-video-index0",
    "camera_7": "/dev/v4l/by-id/usb-CAMERA_7_ID-video-index0"
}

def capture_frames_from_camera(output_folder, camera_name, num_frames=1000):
    device_path = CAMERAS.get(camera_name)

    if not device_path:
        print(f"Error: Camera '{camera_name}' not found.")
        return

    cap = cv2.VideoCapture(device_path)

    if not cap.isOpened():
        print(f"Error: Could not open video device {device_path}.")
        return

    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        frame_filename = os.path.join(output_folder, f"{camera_name}_frame_{i}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Captured {frame_filename}")
        
        cv2.waitKey(1000)  # Wait 1 second between captures

    cap.release()
    print("Image capture complete.")

if __name__ == "__main__":
    output_folder = "./images"
    selected_camera = None
    
    while True:
        if not selected_camera:
            print("Available cameras:")
            for idx, cam in enumerate(CAMERAS.keys()):
                print(f"{idx}: {cam}")

            print("Select a camera index from the list above:")
            camera_index = int(input().strip())
            
            camera_names = list(CAMERAS.keys())
            if 0 <= camera_index < len(camera_names):
                selected_camera = camera_names[camera_index]
                print(f"Selected camera: {selected_camera}")
            else:
                print("Invalid camera index. Please try again.")
        
        else:
            print("Press 'a' to start capturing images, 'c' to change camera, or 'q' to quit.")
            choice = input().strip().lower()
            
            if choice == 'a':
                capture_frames_from_camera(output_folder, selected_camera, num_frames=1000)
            elif choice == 'c':
                selected_camera = None
            elif choice == 'q':
                break
            else:
                print("Invalid choice. Please try again.")