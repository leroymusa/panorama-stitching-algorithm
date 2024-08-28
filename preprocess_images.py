import cv2
import os

def preprocess_image(img):
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) in each color channel
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))
    final_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    return final_img

def preprocess_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        
        if img is not None:
            processed_img = preprocess_image(img)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, processed_img)
            print(f"Processed and saved: {output_path}")
        else:
            print(f"Failed to load image: {img_path}")

if __name__ == "__main__":
    input_folder = "./images"
    output_folder = "./processed_images"
    preprocess_images(input_folder, output_folder)