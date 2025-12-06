pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
        GITHUB_TOKEN = credentials('github-token')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YHasaanRaza2/taskcafe.git'
            }
        }
        
        stage('Code Linting') {
            steps {
                script {
                    echo 'Running Go Linting...'
                    sh '''
                        # Lint Go files
                        cd server
                        golangci-lint run ./...
                        
                        # Lint frontend files (if needed)
                        cd ../frontend
                        npm install
                        npm run lint
                    '''
                }
            }
        }
        
        stage('Code Build') {
            steps {
                script {
                    echo 'Building Taskcafe...'
                    sh '''
                        # Build Go backend
                        cd server
                        go build -o taskcafe .
                        
                        # Build React frontend
                        cd ../frontend
                        npm install
                        npm run build
                    '''
                }
            }
        }
        
        stage('Unit Testing') {
            steps {
                script {
                    echo 'Running Unit Tests...'
                    sh '''
                        # Run Go tests
                        cd server
                        go test ./... -v
                        
                        # Run frontend tests
                        cd ../frontend
                        npm test -- --watchAll=false
                    '''
                }
            }
        }
        
        stage('Build Docker Images') {
            steps {
                script {
                    echo 'Building Docker images...'
                    sh '''
                        # Build backend image
                        docker build -t taskcafe-backend -f server/Dockerfile.server .
                        
                        # Build frontend image
                        docker build -t taskcafe-frontend -f frontend/Dockerfile.frontend .
                        
                        # Build Selenium test image
                        docker build -t taskcafe-selenium-tests -f selenium_tests/Dockerfile selenium_tests/
                    '''
                }
            }
        }
        
        stage('Containerized Deployment') {
            steps {
                script {
                    echo 'Deploying with Docker Compose...'
                    sh '''
                        # Stop existing containers
                        docker-compose -f docker-compose.jenkins.yml down || true
                        
                        # Start new containers
                        docker-compose -f docker-compose.jenkins.yml up -d
                        
                        # Wait for services to be ready
                        sleep 30
                    '''
                }
            }
        }
        
        stage('Selenium Testing') {
            steps {
                script {
                    echo 'Running Selenium Tests...'
                    sh '''
                        # Run Selenium tests against deployed application
                        docker run --network host taskcafe-selenium-tests
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            sh '''
                docker-compose -f docker-compose.jenkins.yml down
                docker system prune -f
            '''
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
