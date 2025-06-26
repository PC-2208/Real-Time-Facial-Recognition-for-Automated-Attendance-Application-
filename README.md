# Real-Time-Facial-Recognition-for-Automated-Attendance-Application-
Real-Time Facial Recognition System for taking automated attendance in classrooms. It uses a webcam to scan students' faces, recognizes them using AI, and marks their attendance in an Excel sheet, without needing any manual work.

# Features of the Project
1. Teacher Login Screen: Teachers log in securely to start attendance.
2. Faculty & Subject Details Page: Shows which subject is being taught, the time, and the teacher's info.
3. Live Camera Scanning: Opens for 30 minutes and scans every 3 seconds.
4. Rescans every 10 minutes to catch latecomers.
5. Auto Shutdown: Closes the camera after 55 minutes.
6. Attendance Sheet: Saves data in Excel files.
7. Streamlit Interface: Clean and easy-to-use UI.

# Required Libraries for Installation
1. Install OpenCV (for camera and image processing)
   ```python
   pip install opencv-python
2. Install face recognition (for recognizing student faces)
   ```python
    pip install face-recognition'
3. Install NumPy (for numeric operations)
   ```python
   pip install numpy
4. Install Pandas (for handling Excel sheets/dataframes)
   ```python
   pip install pandas
5. Install Streamlit (for building the UI)
   ```python
   pip install streamlit
6. Install datetime

The datetime module is part of Python’s standard library, so you don’t need to install it.

    'import datetime'
7. You can install them all using:
      ```python
      pip install -r requirements.txt

# How It Works
1. Teacher logs in and enters subject details.
2. The camera starts and scans student faces every 3 seconds.
3. If a face is recognized, attendance is marked as “Present”.
4. It rescans every 10 minutes to capture any new students.
5. Attendance is marked and saved in an Excel file.
6. Camera closes after 30 minutes, and the UI closes after 55 minutes.

# What Makes Our App Better Than Others
| Our App                           | Other Apps            |
| ---------------------------------- | --------------------- |
| Real-time scanning every 3 seconds | Mostly one-time scan  |
| Auto-rescan every 10 minutes       | Not available         |
| Automatically stops after 55 mins  | Requires manual stop  |
| Simple Streamlit interface         | Often complex or none |
| Works offline                      | Many need internet    |

# Example of Output (Excel File)

| Name         | Subject | Date       | Time     | Status  |
| ------------ | ------- | ---------- | -------- | ------- |
| Aayush Singh | AI      | 2025-06-26 | 10:00 AM | Present |
| Neha Verma   | AI      | 2025-06-26 | 10:00 AM | Present |

# Future Scope of the Project
1. Can be linked with college ERP or databases.
2. Notification via Email/SMS to absentees.
3. Real-time dashboard with graphs.
4. Can be made into a mobile app.
5. Voice confirmation when attendance is marked.

# Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Contact
Project Owner: Priyanshi Chaudhary

Email: priyanshichaudhary2015@gmail.com 



