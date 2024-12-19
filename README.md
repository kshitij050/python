# python
GTP Collage Admission Form
This project is a simple GUI-based application built using Python's Tkinter library. The application simulates an admission form for a college, where users can enter their details such as name, address, mobile number, gender, and year of study, and select their subjects accordingly. The user inputs are saved into a text file upon submission.

Features
User Input Fields:
Name
Address
Mobile Number
Gender Selection:
Radio buttons for Male and Female.
Year of Study Selection:
Radio buttons for First Year (FY), Second Year (SY), and Third Year (TY).
Subject Selection:
The subjects available are dynamically updated based on the selected year.
Save Information:
User inputs are saved into a text file (admissionform.txt), including name, address, mobile number, gender, year, and selected subjects.
Installation
To run the application on your machine, follow these steps:

Ensure Python is installed:

You need Python 3.x installed on your computer.
If Python is not installed, you can download it from here.
Install Tkinter:

Tkinter is usually included with Python by default. If it's not installed, you can install it using:
On Ubuntu/Debian: sudo apt-get install python3-tk
On Windows: Tkinter should be included with the Python installer.
Download the Project:

Clone or download the repository to your local machine.
Run the Application:

Navigate to the project directory and run the following command:
bash
Copy code
python your_file_name.py
The GUI will open where you can enter your details and save them.
How It Works
Name: Enter your full name in the provided input field.
Address: Enter your address in the multiline text field.
Mobile Number: Enter your mobile number in the provided input field.
Gender: Choose your gender using the radio buttons.
Year of Study: Select your year (FY, SY, or TY). Based on your selection, available subjects are listed in the listbox.
Subjects: Select the subjects corresponding to your year. The available subjects change dynamically depending on the selected year.
Save Information: Click the "Save Info" button to save the entered information into a text file (admissionform.txt).
Example Output
The admissionform.txt file will contain:

output
Copy code
Name: John Doe
Address: 123 Main St, Some City, Some Country
Contact no: 1234567890
Gender: MALE
Year: 1
Selected subjects: ['Maths', 'English']
Contributing
Feel free to contribute to the project by submitting pull requests or opening issues.

License
This project is open-source and available under the MIT License.

Acknowledgements
Python and Tkinter for providing the framework to build the GUI.
All contributors to the project.
