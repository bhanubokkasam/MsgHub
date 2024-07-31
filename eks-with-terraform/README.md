## EKS with Terraform

### Overview
The `terraform` folder contains all the necessary Terraform configurations to provision and manage an Amazon EKS (Elastic Kubernetes Service) cluster on AWS. The setup includes creating a VPC, subnets, and other necessary resources to support the Kubernetes cluster.

### Folder Structure

```plaintext
.
├── eks.tf                   # Terraform configuration for EKS cluster resources
├── providers.tf             # Provider configuration for AWS and other providers
├── terraform.tfstate        # State file tracking the current state of the infrastructure
├── terraform.tfstate.backup # Backup of the state file
├── tf.plan                  # Terraform plan output file (binary format)
├── tfplan.txt               # Human-readable format of the Terraform plan
├── variables.tf             # Variable definitions for the Terraform configuration
└── vpc.tf                   # Configuration for VPC and related networking resources
```

### Files Explanation

1. **eks.tf**
   - Defines the resources required to set up an EKS cluster, including the EKS control plane, node groups, and associated IAM roles and policies.

2. **providers.tf**
   - Specifies the providers used in this Terraform setup. Primarily, it configures the AWS provider with the necessary region and credentials setup.

3. **terraform.tfstate**
   - This file tracks the current state of the managed infrastructure. It helps Terraform know what resources are being managed and their current state, enabling accurate and safe updates.

4. **terraform.tfstate.backup**
   - A backup of the state file created before the latest `terraform apply` command. It ensures that you have a recent backup of the state in case something goes wrong.

5. **tf.plan**
   - The output of the `terraform plan` command in a binary format, used to review changes before applying them. It shows what actions Terraform will take when applying the configuration.

6. **tfplan.txt**
   - A human-readable version of the Terraform plan, providing detailed information about the proposed changes to the infrastructure.

7. **variables.tf**
   - Contains variable declarations used throughout the Terraform configurations. This includes parameters like VPC CIDR blocks, EKS cluster settings, and node group configurations.

8. **vpc.tf**
   - Configures the VPC (Virtual Private Cloud) and networking resources, including subnets, route tables, internet gateways, and security groups. This setup isolates the Kubernetes resources and controls inbound and outbound traffic.

### Setup and Usage

1. **Install Terraform**:
   - Ensure that Terraform is installed on your local machine. You can download it from the [Terraform website](https://www.terraform.io/downloads.html).

2. **Initialize Terraform**:
   - Navigate to the `terraform` folder and initialize the configuration with:
     ```bash
     terraform init
     ```

3. **Configure Variables**:
   - Update the `variables.tf` file for variables such as VPC CIDR, EKS cluster name, and node instance types.

4. **Plan the Infrastructure**:
   - Generate an execution plan to preview the changes Terraform will make:
     ```bash
     terraform plan -out tf.plan
     terraform show -no-color tf.plan > tfplan.txt
     ```
   - Review the plan in `tfplan.txt` or directly from the console output.

5. **Apply the Configuration**:
   - Apply the changes to create or update the infrastructure:
     ```bash
     terraform apply
     ```

6. **Review and Manage State**:
   - Regularly review the `terraform.tfstate` file to understand the current state of the managed resources. Use `terraform state` commands for advanced state management tasks.

