Quiz Craft AI

A full-stack web application that dynamically extracts quiz questions from formatted PDF documents and provides an interactive, responsive testing interface for users.

## Features
* **PDF Text Extraction & Parsing:** Automatically processes uploaded PDF files in-memory using `pdfplumber` and extracts structured quiz questions using robust Regular Expressions (`re`).
* **Interactive Quiz Interface:** Built with clean HTML, CSS, and JavaScript featuring instant answer validation, scoring, and real-time visual feedback.
* **RESTful API Backend:** Powered by `FastAPI` with CORS middleware enabled for seamless frontend-backend communication.
* **Production-Ready Hosting:** Designed to be easily deployed with the backend hosted on **Render** and the frontend hosted on **Vercel**.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn, pdfplumber
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Deployment:** Render (Backend), Vercel (Frontend)

## Local Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/anurag-cp/digitallibrary.git](https://github.com/anurag-cp/digitallibrary.git)
cd digitallibrary
