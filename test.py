# import cv2
# import pytesseract
# from PIL import Image
# import os

# # Optional: Configure Tesseract path if necessary (Windows users)
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def preprocess_image(image_path):
#     # Load the image
#     image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Apply GaussianBlur to reduce noise
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
#     # Apply adaptive thresholding for binarization
#     thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
#     # Save the preprocessed image temporarily
#     temp_filename = "temp_preprocessed_image.png"
#     cv2.imwrite(temp_filename, thresh)
    
#     return temp_filename

# def perform_ocr_on_images(image_paths):
#     results = []
    
#     for image_path in image_paths:
#         # Preprocess the image
#         processed_image_path = preprocess_image(image_path)
        
#         # Use Tesseract to do OCR on the preprocessed image
#         text = pytesseract.image_to_string(Image.open(processed_image_path))
        
#         # Append the result with image name and extracted text
#         results.append((image_path, text))
        
#         # Clean up by removing the temporary file
#         os.remove(processed_image_path)
    
#     return results

# # Example usage with a list of image paths
# image_paths = ["image1.png", "image2.jpg", "image3.png"]  # Replace with your list of image paths
# ocr_results = perform_ocr_on_images(image_paths)

# # Print the results for each image
# for image_path, text in ocr_results:
#     print(f"Extracted Text from {image_path}:\n{text}\n")
