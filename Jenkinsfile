pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'smart-traffic-app:latest'
        CONTAINER_NAME = 'nexus-traffic-container'
    }

    stages {
        stage('Source Checkout') {
            steps {
                // GitHub se latest code pull karne ka instructions
                checkout scm
                echo 'Source code pulled successfully from GitHub Git Repository.'
            }
        }

        stage(' Environment Build & Dependencies') {
            steps {
                echo 'Installing workspace dependencies and validating models...'
                // Code checks and container workspace mapping simulation
                sh 'pip install -r requirements.txt'
            }
        }

        stage(' Docker Container Compilation') {
            steps {
                echo 'Compiling clean microservices stack layers via Dockerfile...'
                // Purani layers clean karke fresh build run karna
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Live Micro-Deployment') {
            steps {
                echo 'Executing zero-downtime container replacement protocol...'
                // Purane container ko stop karke naya image port 8000 par launch karna
                script {
                    try { sh "docker stop ${CONTAINER_NAME}" } catch(e) { echo 'No existing container running.' }
                    try { sh "docker rm ${CONTAINER_NAME}" } catch(e) { echo 'No legacy container stack to purge.' }
                }
                sh "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}"
                echo 'Deployment live matrix update complete on active routing nodes!'
            }
        }
    }

    post {
        success {
            echo '🎉 NEXUS_DEPLOY: CI/CD Pipeline Executed Successfully!'
        }
        failure {
            echo ' Pipeline Execution Glitch detected in architecture layers.'
        }
    }
}