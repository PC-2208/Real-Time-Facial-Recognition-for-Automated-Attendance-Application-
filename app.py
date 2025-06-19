import streamlit as st
import cv2
import numpy as np
import pandas as pd
import datetime
import os
import time
from deepface import DeepFace

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = []
if "scanning" not in st.session_state:
    st.session_state.scanning = False

# Define student images directory
students_dir = r"C:/Users/user/OneDrive/Desktop/priyanshi/major_project_hcst/UI_Development/grayscale_images/Devesh"

# Function to validate student images
def get_valid_student_images():
    student_images = [
        img for img in os.listdir(students_dir)
        if img.lower().endswith(('.jpg', '.png', '.jpeg'))
    ]
    
    valid_students = {}
    for img in student_images:
        img_path = os.path.join(students_dir, img)
        if cv2.imread(img_path) is not None:  # Check if file is a valid image
            student_name = os.path.splitext(img)[0]  # Remove extension
            valid_students[student_name] = img_path
        else:
            st.warning(f"Invalid student image: {img_path}")

    return valid_students

# Function to stop scanning
def stop_scanning():
    st.session_state.scanning = False
    st.session_state.page = "Attendance Sheet"

# **SCREEN 1: Login Page**
if st.session_state.page == "Login":
    st.title("🔐 Teacher Login")

    st.session_state.teacher_id = st.text_input("Enter Teacher ID")
    st.session_state.password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if st.session_state.teacher_id == "admin" and st.session_state.password == "1234":
            st.session_state.page = "Faculty Details"
        else:
            st.error("Invalid ID or Password!")

# **SCREEN 2: Faculty & Subject Details**
elif st.session_state.page == "Faculty Details":
    st.title("📚 Faculty & Subject Details")

    faculty_name = st.text_input("Faculty Name")
    subject_name = st.text_input("Subject Name")
    subject_code = st.text_input("Subject Code")
    class_time = st.time_input("Lecture Start Time")
    class_date = st.date_input("Lecture Date")

    if st.button("Start Attendance"):
        st.session_state.faculty_name = faculty_name
        st.session_state.subject_name = subject_name
        st.session_state.subject_code = subject_code
        st.session_state.class_time = class_time
        st.session_state.class_date = class_date
        st.session_state.page = "Attendance System"
        st.session_state.scanning = True  # Start scanning

# **SCREEN 3: Face Scanning & Attendance**
elif st.session_state.page == "Attendance System":
    st.title("📸 Face Recognition Attendance System")

    # Open webcam
    cap = cv2.VideoCapture(0)
    time.sleep(2)  # Add a small delay to initialize the camera properly

    if not cap.isOpened():
        st.error("Error: Camera not found. Please check camera permissions and try again.")
        st.stop()

    # Load student images
    known_students = get_valid_student_images()
    
    if not known_students:
        st.error("No valid student images found! Please check the folder.")
        st.stop()

    stframe = st.empty()  # Streamlit placeholder for camera feed

    def scan_faces():
        start_time = time.time()
        while time.time() - start_time < 10 and st.session_state.scanning:  # Stop when user clicks "Stop"
            ret, frame = cap.read()
            if not ret:
                break

            # Show camera feed in Streamlit
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB", use_container_width=True)

            # Save temporary frame
            temp_img_path = "temp_frame.jpg"
            cv2.imwrite(temp_img_path, frame)

            # Compare with known students
            for name, img_path in known_students.items():
                try:
                    result = DeepFace.verify(temp_img_path, img_path, model_name="Facenet", enforce_detection=True)
                    if result["verified"]:
                        if name not in [entry["Name"] for entry in st.session_state.attendance_data]:
                            st.session_state.attendance_data.append({
                                "Name": name,
                                "Time": datetime.datetime.now().strftime("%H:%M:%S"),
                                "Date": datetime.datetime.now().strftime("%Y-%m-%d")
                            })
                            st.success(f"Attendance Marked for {name}")
                except Exception as e:
                    st.error(f"Face recognition Error: {str(e)}")
                    continue

            time.sleep(1)  # Reduce CPU usage

    # **Start Scanning**
    if st.session_state.scanning:
        st.write("📡 Scanning for students...")
        scan_faces()
        st.write("✅ Scan 1 Completed! Next scan in 10 minutes...")

    # **Stop Scanning Button**
    if st.button("Stop Scanning"):
        stop_scanning()

    cap.release()
    cv2.destroyAllWindows()

# **SCREEN 4: Show Attendance Sheet**
elif st.session_state.page == "Attendance Sheet":
    st.title("📊 Attendance Records")

    # Ensure filename is always defined
    if "subject_code" in st.session_state and "class_date" in st.session_state:
        filename = f"attendance_{st.session_state.subject_code}_{st.session_state.class_date}.xlsx"
    else:
        filename = "attendance.xlsx"

    df = pd.DataFrame(st.session_state.attendance_data)
    df.to_excel(filename, index=False)

    st.success(f"Attendance Marked & Saved as {filename}")

    # **Show Excel Data**
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        st.dataframe(df)
    else:
        st.error("No attendance record found!")

    if st.button("Close Window"):
        st.session_state.page = "Login"
