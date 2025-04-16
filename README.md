
# 🕵️‍♀️ Digital Forensics – Forged Document Classification System

> 🔐 A Deep Learning-Powered Web App to Detect Forged Documents using Image Analysis and OCR

---

## 📌 Introduction

**Digital Forensics** is a smart, Django-powered web application that detects **forged** or **tampered documents** using a **ResNet-based deep learning model**. It combines **image processing**, **optical character recognition (OCR)**, and **convolutional neural networks (CNNs)** to analyze scanned documents for visual and textual inconsistencies.

This tool is designed to **automate the verification process** of important documents — making it faster, more reliable, and scalable.

---

## 🎯 Features

- 📤 Upload and analyze scanned documents
- 🧠 ResNet-based forged document classifier
- 🔍 Optical Character Recognition with Tesseract
- 🎯 Visual and text-based inconsistency detection
- 🌐 Web interface built with Django

---

## 🧠 How It Works

1. 📄 Upload a scanned document through the web interface.
2. 🖼️ Image is preprocessed using **OpenCV** (grayscale, resizing, edge detection, etc.).
3. 🤖 A **ResNet model** predicts if the document is forged or genuine based on visual cues.
4. 🔡 **Tesseract OCR** extracts and evaluates text patterns, fonts, and alignment.
5. ✅ Classification result is returned: `Genuine` or `Forged`.

---

## ⚙️ Tech Stack

| Layer                 | Tools & Libraries              |
|-----------------------|-------------------------------|
| **Framework**         | Django (Python)               |
| **Deep Learning**     | ResNet (PyTorch / TensorFlow) |
| **OCR**               | Tesseract                     |
| **Image Processing**  | OpenCV                        |
| **Frontend**          | HTML5, CSS3                   |
| **Database**          | SQLite3                       |

---
