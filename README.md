# Image Recognition

## Description
The Image Recognition project is an OCR-based image recognition system using Django and PyTesseract to convert images into readable text. This application provides easy methods to upload images, extract text, and view recognized data.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Technologies Used
- Python
- Django (Backend)
- PyTesseract (OCR Engine)
- HTML/CSS (Frontend)

## Usage
1.  Upload Image: Use the upload page to submit images.
2.  Extract Text: View recognized text on the result page.

## Project Structure
```plaintext
Image_Recognition/
├── ocr/
│   ├── views.py
│   ├── templates/
│   │   ├── upload.html
│   │   └── result.html
├── manage.py
├── db.sqlite3
└── requirements.txt
```
## Setup Instructions
1. Set Up Virtual Environment
```bash
 
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
```
2. Install Dependencies
```bash
 
pip install -r requirements.txt
```
3. Database Migration
```bash
 
python manage.py migrate
```
4. Run the Server
```bash
 
python manage.py runserver
```

## Contribution Guidelines
1.  Fork the repository.
2.  Create a feature branch (git checkout -b feature/AmazingFeature).
3.  Commit your changes (git commit -m 'Add some AmazingFeature').
4.  Push to the branch (git push origin feature/AmazingFeature).
5.  Open a pull request.
## License
This project is licensed under the MIT License.

## Screenshots:

![image](https://github.com/user-attachments/assets/040018dc-23d2-4ed1-a32a-bbf2ee0832f2)

![image](https://github.com/user-attachments/assets/3e9196dc-c9a3-41d7-935c-03b60a6a912f)

![image](https://github.com/user-attachments/assets/ce17da80-e116-44a4-8545-30975da8c268)




