pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main',
                    url: 'https://github.com/AzizArfaoui1/two-tier-app.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker images...'
                sh 'docker compose build --no-cache'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stopping any existing containers...'
                sh 'docker stop mysql_db flask_app || true'
                sh 'docker rm mysql_db flask_app || true'
                sh 'docker compose up -d'
                echo 'Waiting for MySQL to be ready...'
                sh 'sleep 40'
            }
        }

        stage('Test') {
            steps {
                echo 'Running integration tests...'
                sh 'pip3 install -q pytest requests'
                sh 'python3 -m pytest tests/ -v --tb=short'
            }
        }

    }

    post {
        success {
            echo '=== BUILD SUCCESSFUL ==='
            echo 'App is live at http://localhost:5000'
        }
        failure {
            echo '=== BUILD FAILED ==='
            sh 'docker stop mysql_db flask_app || true'
            sh 'docker rm mysql_db flask_app || true'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
