pipeline {
    agent any

    environment {
        REPO_URL        = 'https://github.com/manpritsingh-mod/Python-Testing.git'
        REPO_BRANCH     = 'master'
        HEALING_WEBHOOK = 'http://healing-engine:5000/webhook/jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.REPO_BRANCH}", url: "${env.REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                    pip3 install -e .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/ --verbose --tb=short --junit-xml=test-results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                    sh """
                    echo "BUILD FAILED — Sending webhook to Self-Healing Engine..."
                    curl -s -X POST \
                        -H 'Content-Type: application/json' \
                        -d '{"name": "${env.JOB_NAME}", "build": {"number": ${env.BUILD_NUMBER}, "status": "FAILURE", "url": "${env.BUILD_URL}"}}' \
                        ${env.HEALING_WEBHOOK} || echo "Webhook call failed (non-critical)"
            """
                }
            }
        }
    }

    post {
        failure {
            sh """
                echo "BUILD FAILED — Sending webhook to Self-Healing Engine..."
                curl -s -X POST \
                    -H 'Content-Type: application/json' \
                    -d '{"name": "${env.JOB_NAME}", "build": {"number": ${env.BUILD_NUMBER}, "status": "FAILURE", "url": "${env.BUILD_URL}"}}' \
                    ${env.HEALING_WEBHOOK} || echo "Webhook call failed (non-critical)"
            """
        }
        success {
            echo "BUILD SUCCESSFUL — No healing needed."
        }
    }
}
