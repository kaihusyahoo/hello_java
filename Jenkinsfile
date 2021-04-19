pipeline {
    
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'java -version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'route'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'ls -ltr'
            }
        }      
    }
}
