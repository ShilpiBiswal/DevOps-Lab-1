pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
        DOCKER_IMAGE = "your-dockerhub-username/my-flask-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ShilpiBiswal/DevOps-Lab-1.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building project..."'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -d -p 5000:5000 --name test_app $DOCKER_IMAGE:$BUILD_NUMBER & sleep 5'
                sh 'curl -f http://localhost:5000 || (echo "Test failed!" && exit 1)'
                sh 'docker stop test_app'
            }
        }

        stage('Push') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-cred', url: '' ]) {
                    sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8081:5000 $DOCKER_IMAGE:$BUILD_NUMBER'
            }
        }
    }
}

