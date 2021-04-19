pipeline {
    
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python --version'
                sh 'java -version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the applicationi...'
                sh 'route'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'ls -ltr'
            }
        }      
    }
}
