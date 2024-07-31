## Message Service Project

### Overview
This project involves creating a simple HTTP API service to manage messages, setting up the service in a Kubernetes cluster on AWS using Terraform, and implementing CI/CD pipelines with Jenkins and GitLab. The project is structured into different folders for clear organization and management.

### Folder Structure

- **eks-with-terraform**: Contains Terraform scripts to set up the Kubernetes cluster on AWS.
- **message-service**: The Python Flask application that serves as the message service.
- **kubernetes**: Kubernetes manifests for deploying the message service, including configurations for zero downtime deployments, monitoring, and logging.
- **jenkins**: Jenkins pipeline script for CI/CD of the message service.
- **gitlab**: GitLab CI/CD configuration (if applicable) and related scripts.

### Message Service API

The message service implements a simple RESTful API with the following endpoints:

1. **Message Data Structure**:
   ```json
   {
     "account_id": "<id>",
     "message_id": "<random-uuid>",
     "sender_number": "<PHONE_NUMBER>",
     "receiver_number": "<PHONE_NUMBER>"
   }
   ```

2. **Endpoints**:
   - **GET /get/messages/{account_id}**: Returns all messages associated with the provided account ID.
   - **POST /create**: Saves a new message with the given sender and receiver details.
   - **GET /search**: Search for messages using query parameters like `message_id`, `sender_number`, and `receiver_number`.

### DevOps Setup

#### Kubernetes
- **Deployment Spec**: Manages the deployment of the message service with zero downtime, includes sidecars for logging (fluentd), and defines network policies, service accounts, and IAM roles.
- **Monitoring**: Uses Prometheus and Alertmanager for monitoring the service.
- **StatefulSet for Database**: Deploys a MySQL database using StatefulSet, along with persistent storage.

#### Terraform
- Terraform scripts in `eks-with-terraform` are used to set up the Elastic Kubernetes cluster on AWS.ules.

#### CI/CD
- **Jenkins**: The Jenkinsfile in the `jenkins` folder defines a pipeline for building the Docker image of the message service.
- **GitLab**: The `gitlab` folder contain CI configurations for GitLab, pipeline for testing and building the Docker image of the message service.

### Setup and Running

1. **Kubernetes Cluster Setup**:
   - Navigate to <a href= "https://github.com/bhanubokkasam/MsgHub/tree/main/eks-with-terraform#readme">eks-with-terraform</a> and follow the instructions to provision the EKS cluster using Terraform.
   - Ensure your AWS credentials are configured and the necessary permissions are set. 

2. **Deploying the Message Service**:
   - Go to the <a href= "https://github.com/bhanubokkasam/MsgHub/tree/main/kubernetes#readme">kubernetes</a> folder.
   - Apply the Kubernetes manifests using `kubectl apply -f <manifest_file>.yaml`.
   - This includes deploying the message service, database, monitoring, and logging configurations.

3. **CI/CD Pipeline Setup**:
   - For Jenkins, navigate to the <a href= "https://github.com/bhanubokkasam/MsgHub/tree/main/jenkins#readme">jenkins</a> folder and use the provided Jenkinsfile to set up the pipeline in your Jenkins instance.
   - As I am familiar with GitLab, to configure the CI/CD pipeline as per the scripts and instructions in the <a href= "https://github.com/bhanubokkasam/MsgHub/tree/main/gitlab#readme">gitlab</a> folder.

4. **Application Setup**:
   - Go to <a href= "https://github.com/bhanubokkasam/MsgHub/tree/main/message-service#readme">message-service</a> folder and follow the instructions to run the application in local.
   - Make sure python is installed in laptop.

### Architectural Diagram of AWS for deploying this application





