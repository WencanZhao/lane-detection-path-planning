import os
import cv2
import numpy as np

def detect_lanes(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    lines = cv2.HoughLinesP(
        edges, 1, np.pi/180, threshold=50,
        minLineLength=40, maxLineGap=100
    )

    out = img_bgr.copy()
    if lines is not None:
        for x1, y1, x2, y2 in lines[:, 0]:
            cv2.line(out, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return out, edges

if __name__ == "__main__":
    # 确保输出目录存在
    os.makedirs("outputs", exist_ok=True)

    img = cv2.imread("data/road.jpg")
    if img is None:
        raise FileNotFoundError("请先上传一张测试图到 data/road.jpg")

    lanes_img, edges = detect_lanes(img)
    cv2.imwrite("outputs/edges.jpg", edges)
    cv2.imwrite("outputs/lanes.jpg", lanes_img)
    print("✅ 结果已保存到 outputs/edges.jpg 和 outputs/lanes.jpg")
