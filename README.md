# 🔒 Deep Learning Image & Text Steganography

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-orange?style=for-the-badge&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📌 Overview

Deep Learning Image & Text Steganography is an AI-powered application that securely hides **images** and **text messages** inside cover images using deep learning and encryption techniques.

The application provides an intuitive Streamlit interface for encoding and decoding hidden information while preserving high image quality.

---

## ✨ Features

### 🖼️ Image Steganography

- Hide one image inside another image
- Recover the hidden image
- High-quality reconstruction
- PSNR & SSIM evaluation
- Download generated stego image

### 📝 Text Steganography

- Hide secret text inside an image
- Recover hidden messages
- Password-based encryption
- Download stego image

### 📊 Performance Evaluation

- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)

### 🎨 Modern Interface

- Dark Theme
- Responsive Layout
- Interactive Dashboard
- Real-time Image Preview

---

# 📂 Project Structure

```text
deep-steganography/
│
├── .streamlit/
│   └── config.toml
│
├── app/
│   ├── app.py
│   ├── image_utils.py
│   ├── text_utils.py
│   ├── utils.py
│   └── style.css
│
├── checkpoints/
│   └── adversarial_best.pth
│
├── models/
├── training/
├── evaluation/
├── results/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/deep-learning-steganography.git

cd deep-learning-steganography
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Ubuntu

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

If app.py is inside the **app** folder:

```bash
cd app

streamlit run app.py
```

or

```bash
streamlit run app/app.py
```

---

# 🖥️ Application Workflow

## Image Steganography

```
Cover Image
        │
        ▼
Deep Learning Encoder
        │
        ▼
Stego Image
        │
        ▼
Deep Learning Decoder
        │
        ▼
Recovered Secret Image
```

---

## Text Steganography

```
Secret Message
        │
Encryption
        │
Embedding
        │
Stego Image
        │
Extraction
        │
Decryption
        │
Recovered Message
```

---

# 📈 Evaluation Metrics

| Metric | Description |
|----------|-------------|
| PSNR | Peak Signal-to-Noise Ratio |
| SSIM | Structural Similarity Index |
| Image Quality | Visual similarity between original and reconstructed image |

---

# 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- Pillow
- NumPy
- OpenCV
- TorchVision
- Cryptography (Fernet)

---

# 📸 Screenshots

## Home Page

> Add screenshot here

---

## Image Encoding

> Add screenshot here

---

## Image Decoding

> Add screenshot here

---

## Text Encoding

> Add screenshot here

---

## Text Decoding

> Add screenshot here

---

# 🚀 Future Improvements

- Video Steganography
- Audio Steganography
- Batch Processing
- Cloud Deployment
- User Authentication
- Drag & Drop Upload
- Model Comparison Dashboard

---

# 👨‍💻 Author

**Sampati Dotasara**

B.Tech Computer Science Engineering

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
