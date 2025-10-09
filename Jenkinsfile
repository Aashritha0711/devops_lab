pipeline {
    agent any

    triggers {
        // Poll SCM trigger: adjust interval if needed
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo "Running build..."
                sh 'echo Build logic goes here'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo Test logic goes here'
            }
        }
    }
}
