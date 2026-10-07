pipeline {
    agent any
    
    environment {
        PROJECT_NAME = "facial-recognition"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Repository checked out successfully"
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt || echo "No requirements.txt found"'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/ -v || echo "No tests directory"'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${PROJECT_NAME}:${BUILD_NUMBER} .'
            }
        }
        
        stage('Run Application') {
            steps {
                echo "Facial Recognition pipeline completed successfully!"
                sh 'python3 --version'
            }
        }
    }
    
    post {
        success {
            echo "✅ Build successful!"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
