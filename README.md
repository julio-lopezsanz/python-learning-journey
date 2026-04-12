# File Organizer (Python)

A Python-based utility to automatically organize local files into categorized folders by extension. Designed for efficiency and clean workspace management.

## Purpose
I built this project to automate the process of organizing directories (like the Downloads folder). This is a **learning project** focused on mastering Python fundamentals and file system automation.

## Features
- **Automatic Sorting:** Groups files into categories like `Images`, `Documents`, and `Media`.
- **Safety Checks:** Verifies directory existence before moving files.
- **Extensible:** Easy to add new file extensions and categories.

## How it works
The script scans a target directory and moves files into subfolders based on their extension:
- `.jpg, .png, .gif` -> **Images**
- `.pdf, .docx, .txt` -> **Documents**
- `.zip, .rar` -> **Archives**

## Technologies Used
* **Python 3.x**
* **OS Module** (for file system interaction)
* **Shutil Module** (for high-level file operations)

## Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/julio-lopezsanz/file-organizer.git
2. **Run the script:**
   ```bash 
   python main.py

## Learning Journey
**By building this project, I am practicing:**
- Using Python's standard library for real-world tasks.
- Managing code versions with Git and GitHub.
- Documentation best practices for developers.

---

Created with 💻 by [**Julio Cesar Lopez Sanchez**](https://github.com/julio-lopezsanz)
