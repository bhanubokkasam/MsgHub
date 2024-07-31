## GitLab 

### Overview
The `gitlab` folder contains the GitLab CI/CD configuration for building and testing the Docker image of the `message-service` application. This configuration file defines the CI/CD pipeline stages and jobs necessary for automated testing and building of the Docker image.

### Folder Structure

```
gitlab/
└── .gitlab-ci.yml
```

### .gitlab-ci.yml Explanation

The `.gitlab-ci.yml` file is used by GitLab CI/CD to define and run pipeline jobs. The pipeline consists of different stages and jobs, each performing specific tasks in the CI/CD process.

#### Key Components

1. **Variables**
   - `IMAGE_NAME`: Defines the name of the Docker image, which is `bhanubokkasam/message-service`.

2. **Stages**
   - `test`: This stage is used for running tests on the application code.
   - `build`: This stage is used for building and pushing the Docker image.

3. **Jobs**

   - **test_job**
     - **stage**: `test`
     - **script**: Contains the commands to run tests using `pytest`. This ensures that the application code passes all tests before proceeding to the build stage.
     - **tags**: Used to specify the GitLab Runner tag to execute this job. Ensure that a runner with the `runner` tag is configured.

   - **build_job**
     - **stage**: `build`
     - **script**: Contains the commands to build and push the Docker image:
       - `export DATE_TAG=\`date '+%Y%m%d%H%M%S'\``: Generates a timestamp tag for the Docker image.
       - `docker build -t $IMAGE_NAME .`: Builds the Docker image with the `latest` tag.
       - `for t in latest $DATE_TAG; do docker tag "$IMAGE_NAME:latest" "$IMAGE_NAME:${t}"; done`: Tags the image with `latest` and the generated timestamp.
       - `for t in latest $DATE_TAG; do docker push "$IMAGE_NAME:latest" "$IMAGE_NAME:${t}"; done`: Pushes both tags to the Docker registry.
     - **tags**: Used to specify the GitLab Runner tag to execute this job. Ensure that a runner with the `runner` tag is configured.

### Setup Instructions

1. **GitLab Runner Configuration**
   - Ensure you have a GitLab Runner configured and tagged with `runner`. This runner will execute the jobs defined in the pipeline.

2. **Repository Configuration**
   - Add the `.gitlab-ci.yml` file to the root of your GitLab repository. GitLab will automatically detect this file and start the pipeline when changes are pushed to the repository.

3. **Pipeline Execution**
   - The pipeline will automatically trigger on code changes or manually through the GitLab CI/CD interface. It will run the `test_job` stage to execute tests and then proceed to the `build_job` stage to build and push the Docker image.

