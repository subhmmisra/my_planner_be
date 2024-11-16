pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', url: 'https://your-repository-url.git'
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
                    source venv/bin/activate
                    python manage.py migrate
                    '''
                }
            }
        }

        stage('Collect Static Files') {
            steps {
                script {
                    echo 'Collecting static files...'
                    sh '''
                    source venv/bin/activate
                    python manage.py collectstatic --noinput
                    '''
                }
            }
        }

        stage('Archive Build') {
            steps {
                script {
                    echo 'Archiving build artifacts...'
                    sh '''
                    tar -czf build.tar.gz venv/ myproject/ manage.py
                    '''
                    archiveArtifacts artifacts: 'build.tar.gz', fingerprint: true
                }
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
