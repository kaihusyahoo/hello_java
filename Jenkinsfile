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
            when {
                expression {
                    $env.BRANCH_NAME == 'dev' || $env.BRANCH_NAME == 'master'
                }
            }
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
    post {
        always {
            echo 'Jenkins Pipelin project is complete!'
        }
        success {
            echo 'sending success email to suce@yahoo.com'
        }
        failure {
            echo 'sending failure email to fail@yahoolcom'
        }
    }
}
