import cv2
import pytesseract

# If on Windows, uncomment and set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = fr'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the camera (0 = default webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show the live camera feed
    cv2.imshow("Camera - Press 's' to scan, 'q' to quit", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # press 's' to capture and extract text
        # Convert to grayscale for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        print("Detected text:\n", text)

    elif key == ord('q'):  # press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()





# import cv2
# import pytesseract

# # Point pytesseract to the tesseract executable (adjust path if you installed elsewhere)
# pytesseract.pytesseract.tesseract_cmd = fr"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def preprocess(frame):
#     """Improve OCR accuracy with basic preprocessing."""
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Increase contrast / threshold to make text stand out
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#     return thresh

# def main():
#     cap = cv2.VideoCapture(0)  # 0 = default laptop webcam

#     if not cap.isOpened():
#         print("Error: Could not open webcam.")
#         return

#     print("Press 'c' to capture and read text, 'q' to quit.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame.")
#             break

#         cv2.imshow("Live Camera - press 'c' to capture, 'q' to quit", frame)

#         key = cv2.waitKey(1) & 0xFF

#         if key == ord('c'):
#             processed = preprocess(frame)
#             text = pytesseract.image_to_string(processed)
#             print("\n--- Detected Text ---")
#             print(text.strip() if text.strip() else "(No text detected)")
#             print("---------------------\n")

#             # Optional: show what OCR actually saw
#             cv2.imshow("Processed for OCR", processed)

#         elif key == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     main()