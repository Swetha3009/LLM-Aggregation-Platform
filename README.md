# 🧠 LLM Aggregation Platform

A unified platform to interact with multiple large language models (LLMs) like GPT, Claude, Gemini, LLaMa, and even **custom-trained models** — all in one place.

> 🚀 Built for the Cloud Computing Course Project - CS-GY 9223  
> 👩‍💻 By: Swetha Jagadeesan, Abhishek Srikumar, Devak Somaraj, Sumanth Subramanian Ramesh

---

## 🧩 Problem Statement

As the adoption of LLMs grows across industries, organizations face several challenges:

- Lack of flexibility in integrating and managing multiple LLMs (especially custom ones)
- Inefficient switching between models for specific tasks or domains
- Absence of a centralized platform for seamless interaction, data preprocessing, and post-processing
- High operational cost and complexity in scaling LLM-powered apps

**This platform aims to address all the above through a scalable, pluggable solution.**

---

## 🧱 Features

✅ Unified Interface to Query Multiple LLMs  
✅ Integration of APIs like OpenAI (GPT), Google Gemini, Anthropic Claude, Meta LLaMa  
✅ Upload and Interact with Custom Fine-tuned Models  
✅ Clean Chat UI with Response Comparison  
✅ Option to Select Preferred Response (for fine-tuning feedback)  
✅ Scalable Backend with Docker and Kubernetes  
✅ Easy-to-Extend Architecture for Adding More Models

---

## 🖼️ System Architecture

Frontend (React.js) ↓ Backend (Flask API) ↓ LLM Interface Layer ├── OpenAI API ├── Google Gemini API ├── Anthropic Claude API ├── Meta LLaMa (Hosted) └── Custom Model Pod (User Uploaded)

MongoDB for chat history storage
AWS EKS for container orchestration


---

## 🧪 Models Integrated

| Model Name       | Source            |
|------------------|-------------------|
| GPT              | OpenAI API        |
| Claude           | Anthropic API     |
| Gemini           | Google API        |
| LLaMa            | Meta (self-hosted)|
| Custom Models    | User-uploaded     |

---

## 📦 Tech Stack

- **Frontend:** React.js
- **Backend:** Flask, REST APIs
- **Database:** MongoDB
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube / AWS EKS)
- **Cloud Provider:** AWS
- **CI/CD:** GitHub Actions

---

## 🚀 Setup Instructions

### Prerequisites
- Docker & Kubernetes (Minikube or AWS EKS)
- Node.js & Python 3.8+
- MongoDB instance (local or remote)


## 1. Clone the Repository:

git clone https://github.com/Swetha3009/LLM-Aggregation-Platform.git
cd LLM-Aggregation-Platform

## 2. Backend Setup:

cd backend
pip install -r requirements.txt
python app.py

## 3. Frontend Setup:

cd frontend
npm install
npm start



