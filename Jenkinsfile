pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', url: 'https://github.com/subhmmisra/my_planner_be.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    echo 'Setting up Python virtual environment...'
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    echo 'Running migrations...'
                    sh '''
                    source environment/bin/activate
                    python manage.py migrate
                    '''
                }
            }
        }


    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Please check the logs for details.'
        }
    }
}
