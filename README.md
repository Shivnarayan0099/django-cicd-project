# 🛰️ NEXUS_CORE: AI-Powered Intelligent Urban Traffic Grid

Nexus Automated Deployment Pipeline System is a production-grade Intelligent Transportation System (ITS). The architecture seamlessly integrates a Machine Learning predictive engine, structured relational logging, containerized microservices, and an automated DevOps continuous integration/deployment pipeline.

Architected & Deployed by: **Shivnarayan (@shivnarayan)** Level: **CSE (Data Science) '27**

---

##  Core Architecture Overview

The system optimizes real-time urban traffic congestion matrices by processing telemetry data through an isolated multi-layered software pipeline:

1. **Source Layer (Frontend/UI):** A hyper-clean, responsive dashboard layout crafted using HTML5, Django Template Engine, and Tailwind CSS. Features active analytics charts powered by Chart.js and an automatic 15-second telemetry reload countdown script.
2. **Analytical Layer (Machine Learning Backend):** Built on Django 6.0 and Python 3.13. Incoming grid data is evaluated via a pre-trained **Scikit-Learn Random Forest Classifier Engine (`traffic_prediction_model.pkl`)** to predict real-time traffic density profiles (Low, Medium, High).
3. **Storage Layer (Database Logging):** All transactional entries, loop node statuses, vehicle counts, and model inference results are sequentially written to an isolated local SQLite database cluster for auditing.
4. **DevOps & Infrastructure Stack:** * **Docker:** Containerizes the entire environment into a lightweight, cross-platform layer using a custom `Dockerfile` based on `python:3.13-slim`.
   * **Jenkins:** Automated Declarative Pipeline (`Jenkinsfile`) manages continuous integration, image building, and production rolling deployment.
   * **Render Cloud Platform:** Hosted over an active Docker container layer for high availability and universal web accessibility.

---

## 🛠️ System Technology Stack

* **Core Framework:** Python 3.13.x, Django 6.0.5
* **Data Science & ML Suite:** Scikit-Learn, Pandas, NumPy
* **Data Visualization:** Chart.js (Line & Bar cluster vectors)
* **Styling & UI Components:** Tailwind CSS, Google Fonts
* **DevOps Orchestration:** Docker, Jenkins Pipeline Engine
* **Cloud Hosting Environment:** Render Container Fleet Services

---

## Repository Structure

```text
django-cicd-project/
├── app/                        # Main Django Application Module
│   ├── migration/              # DB Structural State Scripts
│   ├── templates/app/
│   │   ├── base.html           # Core Framework DOM Blueprint
│   │   └── index.html          # Dynamic Traffic Telemetry Interface
│   └── views.py                # ML Model Execution & Controller Logic
├── config/                     # Core Project Configuration Settings
│   ├── settings.py             # Allowed Hosts & System Midlleware Specs
│   └── urls.py                 # Core App Routing Vectors
├── Dockerfile                  # Container Compilation Instructions
├── Jenkinsfile                 # Declarative Automation Pipeline Script
├── manage.py                   # Django Administrative Entrypoint
├── requirements.txt            # System Pinpoint Dependencies
└── traffic_prediction_model.pkl # Trained Scikit-Learn Predictive Brain

stages {
    stage('Source Checkout') { 
        // Automatically fetches the fresh codebase commits from the GitHub repository.
    }
    stage('Environment Build') { 
        // Installs required python workspace dependencies mapped in requirements.txt.
    }
    stage('Docker Compilation') { 
        // Builds a fresh isolated microservice container image layers using Dockerfile.
    }
    stage('Live Micro-Deployment') { 
        // Drops legacy container stacks and deploys a fresh container instance on active routing ports.
    }
}
Architected & Deployed by: Shivnarayan Dwivedi
Data Scientist & DevOps Engineer
