@Library('unified-ci-library') _

pipeline {
    agent any
    
    environment {
        PROJECT_LANGUAGE = 'python'
        BUILD_TOOL = 'pip'
        TEST_TOOL = 'pytest'
        LINT_TOOL = 'pylint'
    }
    
    stages {
        stage('Execute Python Pipeline') {
            steps {
                script {
                    // Load configuration from ci-config.yaml
                    def config = readYaml file: 'ci-config.yaml'
                    
                    // Execute the Python template pipeline
                    python_template(config)
                }
            }
        }
    }
    
    post {
        always {
            // Archive test results
            archiveArtifacts artifacts: '**/*.xml,**/*.html,**/*.txt', allowEmptyArchive: true
            
            // Publish test results
            publishTestResults testResultsPattern: 'test-results.xml'
            
            // Publish coverage reports
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])
        }
        
        failure {
            script {
                notify.sendFailureNotification()
            }
        }
        
        success {
            script {
                notify.sendSuccessNotification()
            }
        }
    }
}