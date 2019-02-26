[![CircleCI](https://circleci.com/gh/fabinhojorge/OCR_web.svg?style=svg)](https://circleci.com/gh/fabinhojorge/OCR_web)

# OCR web
This project is an OCR (tesseract) web interface to upload images. 
The idea of this project is to study technologies like Python, Django, Tesseract(OCR), Continuous Integration, Celery, etc...


## How to install and Run
After activate your Python Virtual Environment (_venv_) run the below command:

```
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

So you can access in the local URL: _[localhost:8000](localhost:8000/)_


Inside the _requirements.txt_ there are a package called __pytesseract__. 
It´s the wrapper to communicate with the Tesseract library (C/C++ code). 
So, the next step is to install the Tesseract itself. 

For this, please follow the below instructions for your SO:
* [Windows](https://github.com/UB-Mannheim/tesseract/wiki)
* [Mac and Linux](https://github.com/tesseract-ocr/tesseract/wiki)



## How to use
1. _TBD_


## Libraries
* Django
* Pillow
* Bootstrap
* JQuery
* Tesseract (pytesseract)
* Celery


## To Do
* [X] Create an initial project
* [X] Add the continuous integration build and test (Circleci)
* [ ] Create the upload media system: models, forms, templates, media url, etc... 
* [X] Call the OCR to process the image
* [X] Add image link in the home page. Click the image open a modal to check the image
* [ ] Add support to different languages. OCR have a parameter to select the language of the text. User to inform this while uploading the image.
* [X] Create a model to store and an interface to return the text generated by the OCR.
* [ ] Model to handle a copy of the original image. This copy that will be used to run the OCR. The idea is to in the future use this copy to apply some image treatments (all triggered by interface).
* [ ] After the core is working, enhance the BE with Celery.



## Screen Shots

__Home Page__
![Home page](project_assets/home_page.jpg)

__Image Zoom__
![Image Zoom](project_assets/image_zoom.jpg)