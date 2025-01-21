# Azure Cloud Resume Challenge
In this project I built out a static website to host my resume in Azure! You can see my website here: https://resume.jaedyndamms.com/

![image](https://github.com/user-attachments/assets/6440a2fd-3fdd-47cd-afdc-5681805824aa)


## Objective
I created this project to complete the cloud resume challenge which is designed to demonstrate my full-stack cloud skills by creating a resume site hosted on Azure. Key elements of my solution include:
- Azure Storage: Hosts my resume as a static website.
- Serverless Backend: Azure Functions handle backend logic, such as a visitor count.
- Database Integration: Visitor counts and other data stored/retrieved fro Cosmos DB.
- CI/CD Pipeline: Automated builds and deployments via GitHub Actions

### Skills Learned

- Cloud Architecture: Designing and deploying a fully-functional, serverless application on Azure.
- Azure Services: Setting up and configuring key services like Azure Storage, Azure CDN, Functions, Cosmos DB, Azure DNS
- CI/CD Pipeline: Implementing automated builds, and deployments through GitHub Actions.
- Full-Stack Development: Creating a modern, responsive frontend (HTML/CSS/JS) backed by serverless APIs.
- Security & Access Control: Managing roles, permissions, and secure deployments in Azure.
- Continuous Learning: Strengthening problem-solving and debugging skills through hands-on cloud project work.

### Tools Used

- Azure Portal
- Visual Studio
- Programming: Python, HTML, CSS, JS, YML

### Prerequisites 

- Azure Subscription
- Code Editor
- Registered Domain

## Steps
### Step 1 - Create Static Website using HTML & CSS

The first step in this challenge is to create your resume using HTML/CSS. Now since this project isn't focused on any UI/UX design it doesn't have to be anything fancy. However if you're like me I wanted it to look nice. There are some great templates online that you can grab and start with, for me I used the template create by the team at [A Cloud Guru](https://github.com/ACloudGuru-Resources/acg-project-azure-resume-starter)

### Step 2 - Use Azure Storage account to deploy your website as a Azure Storage static website.

Now that the static website is created I now need to deploy this somewhere so other can see it. I chose to use [Azure Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website).

From Visual Studio you can right click the folder which is hosting your front end and select Deploy to Static Website via Azure Storage and go through the configuration steps.

![image](https://github.com/user-attachments/assets/8a64b6b8-f6c6-4461-95d3-002e8f9a4368)


### Step 3 - Configure [Azure CDN](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal#map-a-custom-domain-with-https-enabled) to serve your static website and enable HTTPS for security.

Now I configured Azure CDN as an endpoint for my static website. I am using Azure CDN as it uses POPs located all around the world to cache and serve my website content, improving the performance of the website. Step by steps can be found on the [MS Learn docs](https://learn.microsoft.com/en-us/azure/cdn/cdn-create-new-endpoint)


### Step 4 - Point a custom DNS domain name to your Azure CDN endpoint

Now I have a Azure CDN endpoint for the static website I will add a DNS CNAME record to point subdomains to the Azure CDN endpoint. For experience I moved my domain registry to use Azure DNS Zones and created the DNS records there, however this is optional you can use your current domain registar if you prefer.

![image](https://github.com/user-attachments/assets/e89852f3-9da8-417a-8f1a-a56012b72cce)

With the CNAME record pointing to my CDN endpoint I can also add a custom domain to my CDN endpoint and enable HTTPS traffic

![image](https://github.com/user-attachments/assets/9458e7c8-27da-45e8-9f7f-9de5cf162e4d)

Details steps can be found on the [MS Learn docs](https://learn.microsoft.com/en-us/azure/cdn/cdn-custom-ssl?tabs=option-1-default-enable-https-with-a-cdn-managed-certificate)

### Step 5 - Create Azure CosmosDB to store view count for your website

### Step 6 - Create API using Azure Function App to get and increment view count stored in CosmosDB

### Step 7 - Write some JavaScript to call Azure function and display view count on your website

### Step 8 - CI/CD for Front End

### Step 9 - CI/CD for Back End









