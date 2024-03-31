# Image and Video Forgery Detection System

## Overview

The Image and Video Forgery Detection System (IFAKE) is a project aimed at detecting forged images and videos using convolutional neural networks (CNN) and the ResNet-50 model. This system provides a comprehensive solution for identifying various types of forgeries such as copy-move, splicing, and image retouching.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AbhishekBelagavi/fypr2024.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fypr2024
    ```

3. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    .\venv\Scripts\activate      # for Windows
    source venv/bin/activate     # for Unix/Mac
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Train and test the CNN and ResNet-50 models using the provided Jupyter notebooks.
2. Run the web application using Django:

    ```bash
    cd IFAKE_WebApp
    python manage.py runserver
    ```

3. Access the web application through a web browser at `http://localhost:8000`.

## Contribution

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## Repo structure
IFAKE_Project/
│
├── IFAKE_AI/
│   ├── IMAGEWEIGHTS/
│   │   ├── proposed_ela_50_casia_fidac.h5
│   │   └── segmenter_weights.h5
│   │
│   ├── VideoForgeryClassification/
│   │   ├── Data_Preprocessing.ipynb
│   │   ├── Model_Training.ipynb
│   │   ├── Model_Testing.ipynb
│   │   ├── VideoForgeryDetection.ipynb
│   │   └── ImageForgeryClassification.ipynb
│   │
│   ├── models/
│   │   ├── neural_nets.py
│   │   ├── fake_image_detector.py
│   │   └── other_model_files.py
│   │
│   └── scripts/
│       ├── copy_move_cfa.py
│       ├── copy_move_sift.py
│       └── other_scripts.py
│
├── IFAKE_WebApp/
│   ├── IFAKE_WebApp/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── website/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── image.html
│   │   ├── pdf.html
│   │   └── video.html
│   │
│   └── manage.py
│
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
