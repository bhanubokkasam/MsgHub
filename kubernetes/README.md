## Kubernetes

### Overview
The `kubernetes` folder contains Kubernetes manifest files necessary for deploying and managing the message service application in a Kubernetes cluster. These manifests include configurations for deployments, services, autoscaling, network policies, monitoring, logging, and persistent storage.

### Folder Structure

```
kubernetes/
├── autoscaling.yaml           # Horizontal Pod Autoscaler configuration
├── deployment.yaml            # Deployment configuration for the message service
├── fluentbit-cm.yaml          # ConfigMap for Fluent Bit, used for logging
├── ingress.yaml               # Ingress resource for external access to the service
├── network-policy.yaml        # Network policy for controlling traffic in the cluster
├── prometheus.yaml            # ServiceMonitor configuration for Prometheus monitoring
├── pv.yaml                    # Persistent Volume configuration
├── rbac.yaml                  # Role-Based Access Control (RBAC) configuration
├── service-account.yaml       # Service account with appropriate permissions
├── service.yaml               # Service configuration for internal/external access
├── statefulset.yaml           # StatefulSet configuration for the database
├── storage.yaml               # Persistent Volume Claim for the database
└── storageclass.yaml          # StorageClass configuration for dynamic provisioning
```

### Files Explanation

1. **autoscaling.yaml**
   - Configures a Horizontal Pod Autoscaler (HPA) for the message service, allowing the application to scale based on resource usage metrics like CPU and memory.

2. **deployment.yaml**
   - Defines the Deployment resource for the message service, specifying the number of replicas, container image, environment variables, and other deployment parameters. It ensures that the desired state of the application is maintained, with automatic updates and rollbacks.

3. **fluentbit-cm.yaml**
   - Contains the ConfigMap for Fluent Bit, a lightweight log processor. This configuration sets up log parsing and forwarding to a centralized log management system.

4. **ingress.yaml**
   - Configures an Ingress resource to manage external access to the message service. It defines routing rules, SSL/TLS settings, and hostnames for the service.

5. **network-policy.yaml**
   - Defines NetworkPolicies to control traffic flow within the Kubernetes cluster. This includes rules for allowing or denying traffic between pods based on labels, namespaces, and other criteria.

6. **prometheus.yaml**
   - Specifies a ServiceMonitor resource for Prometheus to scrape metrics from the message service pods. This enables monitoring of application performance and resource usage.

7. **pv.yaml**
   - Defines a Persistent Volume (PV) for persistent storage, typically used by the database in the StatefulSet. This file specifies the storage capacity, access modes, and storage backend.

8. **rbac.yaml**
   - Configures Role-Based Access Control (RBAC) for the message service, including roles, role bindings, and permissions required to access Kubernetes resources securely.

9. **service-account.yaml**
   - Creates a ServiceAccount for the message service pods, granting specific permissions and associating the pods with IAM roles in AWS for access to cloud resources.

10. **service.yaml**
    - Defines a Service resource to expose the message service internally within the cluster or externally to the internet. This includes service type (e.g., ClusterIP, NodePort, LoadBalancer) and port configurations.

11. **statefulset.yaml**
    - Configures a StatefulSet for deploying the database used by the message service. StatefulSets manage the deployment and scaling of a set of pods with persistent identities and stable storage.

12. **storage.yaml**
    - Contains the Persistent Volume Claim (PVC) for the database storage, specifying the desired storage size and access modes. This claim binds to an available PV to provide the necessary storage.

13. **storageclass.yaml**
    - Defines a StorageClass for dynamic provisioning of Persistent Volumes. It specifies the storage backend and parameters for creating new PVs as needed.

### Deployment Steps

1. **Apply Kubernetes Manifests**:
   - Navigate to the `kubernetes` directory and apply the manifests using `kubectl`:
     ```
     kubectl apply -f .
     ```

2. **Verify Resources**:
   - Ensure that all resources (deployments, services, ingress, etc.) are created successfully and are in the desired state:
     ```
     kubectl get all
     ```

3. **Monitor and Log**:
   - Use the Prometheus and Fluent Bit configurations to monitor the service's performance and collect logs.

4. **Scaling and Updates**:
   - Utilize the Horizontal Pod Autoscaler and RollingUpdate strategy in the Deployment for seamless scaling and updates.

