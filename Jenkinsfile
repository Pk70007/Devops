pipeline {
    agent any

    environment {
        // Replace with your Docker Hub credentials ID stored in Jenkins
        DOCKER_CREDENTIALS = 'dockerhub-creds'
        // Docker image name
        DOCKER_IMAGE = 'pk372/app:latest'
    }

    stages {

        stage('Checkout Code') {
            steps {
                // Checkout the main branch from your GitHub repo
                git branch: 'main',
                    url: 'https://github.com/Pk70007/Devops.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build App') {
            steps {
                // Build Maven project
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Run Maven tests
                sh 'mvn test'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Login to Docker Hub and build + push image
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS) {
                        def appImage = docker.build(DOCKER_IMAGE)
                        appImage.push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Run Ansible playbook to deploy to K8s
                ansiblePlaybook credentialsId: 'ansible-key',
                    inventory: 'inventory.ini',
                    playbook: 'deploy-to-k8s.yml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for errors.'
        }
    }
}
