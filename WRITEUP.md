# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

### Selected Deployment Option: Azure App Service

For the ArticleCMS application, Azure App Service was selected as the preferred deployment option over a Virtual Machine (VM). Since ArticleCMS is a relatively small web application, App Service provides a more cost-effective and efficient solution. Unlike a VM, App Service does not require managing the underlying operating system, networking configurations, virtual networks, subnets, or server maintenance, which significantly reduces operational complexity.

From a scalability perspective, App Service can easily scale up or out with minimal configuration, making it suitable for the current and future needs of the application. In terms of availability.

The deployment workflow is also simpler with App Service. The application can be directly integrated with GitHub, enabling automated deployments through a continuous integration and continuous delivery (CI/CD) pipeline. This streamlines development and reduces the effort required to publish updates.

Considering the lower cost, simplified management, built-in scalability, high availability, and straightforward deployment process, Azure App Service is the most appropriate choice for hosting the ArticleCMS application.

### Assess app changes that would change your decision.

1. Custom Server Software

If the application required software that is not supported by App Service, such as:

Custom Linux packages
Background services running continuously
Custom web server configurations (Nginx, Apache)
Third-party monitoring agents

A VM would provide full administrative control over the operating system.

2. Multiple Components on the Same Server

Suppose the application architecture was expanded to include:

ArticleCMS web application
Elasticsearch for search functionality
Redis cache
Custom scheduled jobs


3. Advanced Networking Requirements

If the application handled sensitive corporate data and required:

Private networking
Complex firewall rules
Direct communication with on-premises systems
Custom ports

A VM would provide greater networking flexibility.

4. Self-Hosted Services


A self-hosted database
A self-hosted file storage system
A custom authentication service

These are scenarios where a VM becomes more appropriate.

5. Long-Running Background Processes

For example:

Automatic article indexing
AI content analysis
Video processing
PDF generation services


