import cv2
import numpy as np
import matplotlib.pyplot as plt

def run_image_basics_with_input():
    # [1] Get image size from user
    height = int(input("Enter image height (e.g., 300): "))
    width = int(input("Enter image width (e.g., 300): "))
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # [2] First rectangle
    print("\n-- Red Rectangle --")
    x1, y1 = map(int, input("Enter top-left (x1 y1): ").split())
    x2, y2 = map(int, input("Enter bottom-right (x2 y2): ").split())
    img[y1:y2, x1:x2] = [0, 0, 255]  # Red in BGR
    print("Added red rectangle.")

    # [3] Second rectangle
    print("\n-- Blue Rectangle --")
    x3, y3 = map(int, input("Enter top-left (x3 y3): ").split())
    x4, y4 = map(int, input("Enter bottom-right (x4 y4): ").split())
    img[y3:y4, x3:x4] = [255, 0, 0]  # Blue in BGR
    print("Added blue rectangle.")

    # [4] Color Space Conversion
    convert_gray = input("Convert to Grayscale? (y/n): ").lower() == 'y'
    convert_hsv = input("Convert to HSV? (y/n): ").lower() == 'y'

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if convert_gray else None
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) if convert_hsv else None

    # [5] Image Properties
    print(f"\nImage Properties: Height={height}, Width={width}, Channels=3")

    # [6] Save and Show
    save = input("Save image and show plots? (y/n): ").lower() == 'y'
    if save:
        cv2.imwrite("user_image.png", img)
        print("Image saved as user_image.png")

        plt.figure(figsize=(10, 8))
        plt.subplot(1, 3, 1)
        plt.title("Original (BGR)")
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if convert_gray:
            plt.subplot(1, 3, 2)
            plt.title("Grayscale")
            plt.imshow(img_gray, cmap="gray")
        if convert_hsv:
            plt.subplot(1, 3, 3)
            plt.title("HSV")
            plt.imshow(cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB))

        plt.tight_layout()
        plt.savefig("user_output.png")
        print("Visualization saved as user_output.png")
        plt.show()

# Run the interactive demo
if __name__ == "__main__":
    run_image_basics_with_input()
