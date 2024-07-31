## Jenkins 

### Overview
The `jenkins` folder contains the Jenkins pipeline configuration for building and deploying the Docker image of the `message-service` application. The pipeline automates the processes of checking out the code, building the Docker image, pushing the image to a Docker registry, and cleaning up after the build.

### Folder Structure

```
jenkins/
└── Jenkinsfile
```

### Jenkinsfile Explanation

The `Jenkinsfile` defines a declarative pipeline with multiple stages to handle the continuous integration (CI) process for the `message-service` application.

#### Key Components

1. **Pipeline Agent**
   - `agent any`: Specifies that the pipeline can run on any available Jenkins agent.

2. **Environment Variables**
   - `DOCKER_REGISTRY`: The Docker registry to which the image will be pushed, e.g., `docker.io`.
   - `IMAGE_NAME`: The name of the Docker image, in this case, `bhanubokkasam/message-service-py`.
   - `TAG`: The tag for the Docker image, set to `latest`.
   - `DOCKER_CREDENTIALS_ID`: The Jenkins credentials ID for Docker, used for authenticating with the Docker registry.

3. **Stages**

   - **Checkout**
     - Clones the repository from GitHub. Replace the repository URL with your actual Git repository URL.

   - **Build**
     - Builds the Docker image using the Dockerfile in the repository. The image is tagged with `IMAGE_NAME:TAG`.

   - **Push**
     - Pushes the Docker image to the specified Docker registry. It uses the credentials identified by `DOCKER_CREDENTIALS_ID` for authentication.

   - **Cleanup**
     - Removes the Docker image from the local Docker environment to free up space.

4. **Post-Build Actions**
   - **always**
     - Executes the `cleanWs()` function, which cleans the Jenkins workspace after the build, ensuring that no files are left behind between builds.

### Setup Instructions

1. **Jenkins Configuration**
   - Ensure Jenkins has Docker installed and configured.
   - Set up the `DOCKER_CREDENTIALS_ID` in Jenkins by creating a new credential in the Jenkins credentials store. This credential should have the necessary permissions to push images to your Docker registry.

2. **Pipeline Job Setup**
   - Create a new pipeline job in Jenkins.
   - In the job configuration, point the pipeline to the `Jenkinsfile` in your Git repository, either by using a pipeline script from SCM or by directly pasting the script.

3. **Running the Pipeline**
   - Once the job is configured, you can manually trigger a build or set up triggers based on changes in the Git repository or on a schedule.

