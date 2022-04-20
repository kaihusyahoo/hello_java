def gv
pipeline {
    
    agent any 
    stages {
        stage('init') {
            steps {
                script {
                    gv = load 'script.groovy'
                }
            }
        }
        stage('Build') {        
            steps {
                script {
                    gv.buildApp()
                }
                echo 'Building...'
                sh 'python --version'
                sh 'java -version'
            }
        }
        stage('Unit Testing') { // Perform unit testing
            steps {
               sh 'python basic_python.py'
            }
          }
        }
        stage('Test') {
            when {
                expression {
                    "${env.BRANCH_NAME}" == 'dev' || "${env.BRANCH_NAME}" == 'master'
                }
            }
            steps {
                script {
                    gv.testApp()
                }                
                echo 'Testing...'
                sh 'route'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    gv.deployApp()
                }                
                echo 'Deploying...'
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
