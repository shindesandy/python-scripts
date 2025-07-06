import pyautogui
import time

def capture_screenshots(region, count, delay=1):
    for i in range(count):
        filename = f"screenshot_{i + 1:03}.png"
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(filename)
        print(f"Captured: {filename}")
        time.sleep(delay)
        pyautogui.press('pagedown')  # simulate Page Down key
        time.sleep(delay)

if __name__ == "__main__":
    print("Go to the page you want to start (e.g., Page 5), and place the PDF in focus.")
    time.sleep(5)  # gives you 5 seconds to switch to the PDF viewer

    count = int(input("How many pages to capture? "))
    
    print("Move your mouse to the TOP-LEFT corner of the region you want to capture. You have 5 seconds...")
    time.sleep(5)
    x1, y1 = pyautogui.position()
    
    print("Now move your mouse to the BOTTOM-RIGHT corner. You have 5 seconds...")
    time.sleep(5)
    x2, y2 = pyautogui.position()
    
    width = x2 - x1
    height = y2 - y1

    region = (x1, y1, width, height)

    print(f"Starting capture of {count} screenshots in region: {region}")
    capture_screenshots(region, count)
    print("Done.")
