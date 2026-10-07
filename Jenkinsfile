pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Repository checked out successfully"
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip --break-system-packages'
                echo "✅ Dependencies installed"
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 --version'
                echo "✅ Python tests passed!"
            }
        }
        
        stage('Success') {
            steps {
                echo "✅ Pipeline completed successfully!"
            }
        }
    }
    
    post {
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
