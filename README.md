# 📦 Flask App CI/CD Pipeline with Jenkins and Docker

This project demonstrates a simple Flask web application deployed using a complete CI/CD pipeline with **Jenkins**, **Docker**, and **GitHub Integration**.

---

## 🚀 Project Overview

This application is a basic Python Flask app with two endpoints:

- `GET /info` → Returns a basic info string
- `GET /phone` → Returns a sample phone number

The entire pipeline includes:

- Pulling source code from GitHub
- Installing dependencies (Flask, Pytest)
- Running automated unit tests
- Building a Docker image
- Pushing image to Docker Hub
- Deploying the container

---

## 🧰 Tech Stack Used

| Tool         | Purpose                           |
|--------------|------------------------------------|
| Python 3.12  | Backend language                   |
| Flask        | Web framework                      |
| Pytest       | Unit testing                       |
| Docker       | Containerization                   |
| Jenkins      | CI/CD automation                   |
| GitHub       | Version control & source repo      |

---

## 🔧 File Structure


├── app.py # Flask application
├── test_app.py # Pytest test file for endpoint function
├── Dockerfile # Docker build instructions
├── Jenkinsfile / Job # Jenkins freestyle job
└── README.md # Project documentation


---

## 🧪 Test Case

Unit test is written using `pytest`:

```python
from app import usphone

def test_usphone():
    assert usphone() == "12345678"

🐳 Dockerfile

FROM redhat/ubi9

WORKDIR /app

RUN yum install -y python3 python3-pip && \
    pip3 install flask && \
    yum clean all && \
    rm -rf /var/cache/yum

COPY app.py .

CMD ["python3", "app.py"]


🔁 Jenkins Pipeline (Freestyle Job)

    Source Code Management: Git → GitHub

    Build Triggers: Poll SCM (H * * * *)

    Build Steps:

     ->   Install dependencies using pip

     ->  Run pytest

     ->  Build Docker image

     ->  Push image to Docker Hub

     ->  Run Docker container

# Jenkins Execute Shell Example
pip3 install -r requirements.txt
pytest

docker build -t ujjwalshivhare/ujjwals_app:v1 .
docker push ujjwalshivhare/ujjwals_app:v1

docker rm -f ujjwalos1
docker run -dit --name ujjwalos1 -p 5000:5000 ujjwalshivhare/ujjwals_app:v1


🌐 How to Access

Once the container is running:

curl http://<your-server-ip>:5000/info
curl http://<your-server-ip>:5000/phone
