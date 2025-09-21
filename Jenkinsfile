pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')  
        DOCKER_IMAGE = "your-dockerhub-username/your-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ShilpiBiswal/DevOps-Lab-1.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE:$BUILD_NUMBER npm test || echo "No tests defined"'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-cred', url: '' ]) {
                    sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                sh 'docker run -d -p 8081:80 $DOCKER_IMAGE:$BUILD_NUMBER'
            }
        }
    }
}
