# 🛠️ Automation Python Scripts

A collection of Python scripts created for automating everyday tasks like capturing screenshots from PDFs, navigating repetitive processes, and simplifying workflows. Ideal for developers, students, or professionals looking to improve productivity using Python.

---

## 📌 Features

- 🎯 **Targeted Screenshot Automation**Automatically take repeated screenshots of a specific region of your screen (e.g., pages from a PDF), with support for user-defined loop count and region selection.
- 📂 **Organized Script Repository**
  All Python scripts are grouped for easy reference and future expansion.

---

## 🧑‍💻 Scripts Included

### 1. `screenshot_automation.py`

> Automates screenshot capturing of a defined screen region and simulates page navigation (Page Down key) between each capture.

#### ✅ Use Case:

- Capture pages 5 to 30 from a PDF without manual effort.
- Great for books, reports, or scrolling UIs.

#### 🛠️ Features:

- Define number of iterations (e.g., 26 pages)
- Select region with mouse (Top-Left to Bottom-Right)
- Automatically navigates using Page Down key
- Saves images as `screenshot_001.png`, `screenshot_002.png`, etc.

---

## 🧰 Requirements

- Python 3.x
- `pyautogui` for automation

Install dependencies using:

```bash
pip install pyautogui
```
