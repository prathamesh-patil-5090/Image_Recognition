from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image
import cv2
import numpy as np
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm   
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Denoising (optional)
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    # Resize for better OCR
    resized = cv2.resize(denoised, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    return resized

def perform_ocr(image):
    custom_config = r'--oem 1 --psm 6'  # LSTM OCR and segmentation for blocks of text
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def upload_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage(location='Image_Recognition/media')
        filename = fs.save(image.name, image)
        file_url = fs.url(filename) 

        # Preprocess the image
        preprocessed_image = preprocess_image(fs.path(filename))

        # Perform OCR on preprocessed image
        text = perform_ocr(preprocessed_image)

        # Redirect to result page with the extracted text
        return render(request, 'ocr/result.html', {'text': text})

    return render(request, 'ocr/upload.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ocr/signup.html', {'form': form})
