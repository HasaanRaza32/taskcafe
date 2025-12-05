pipeline {
  agent any
  stages {
    stage('Lint') {
      steps { sh 'echo Linting...' }
    }
    stage('Build') {
      steps { sh 'echo Building Docker image...' }
    }
    stage('Unit Tests') {
      steps { sh 'echo Running unit tests...' }
    }
    stage('Deploy Container') {
      steps { sh 'echo Deploying with docker-compose...' }
    }
    stage('Selenium Tests') {
      steps { sh 'echo Running Selenium tests...' }
    }
  }
}
