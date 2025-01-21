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


### Step 3 - Configure Azure CDN to serve your static website and enable HTTPS for security.

Now I configured Azure CDN as an endpoint for my static website. I am using Azure CDN as it uses POPs located all around the world to cache and serve my website content, improving the performance of the website. Step by steps can be found on the [MS Learn docs](https://learn.microsoft.com/en-us/azure/cdn/cdn-create-new-endpoint)


### Step 4 - Point a custom DNS domain name to your Azure CDN endpoint

Now I have a Azure CDN endpoint for the static website I will add a DNS CNAME record to point subdomains to the Azure CDN endpoint. For experience I moved my domain registry to use Azure DNS Zones and created the DNS records there, however this is optional you can use your current domain registrar if you prefer.

![image](https://github.com/user-attachments/assets/e89852f3-9da8-417a-8f1a-a56012b72cce)

With the CNAME record pointing to my CDN endpoint I can also add a custom domain to my CDN endpoint and enable HTTPS traffic

![image](https://github.com/user-attachments/assets/9458e7c8-27da-45e8-9f7f-9de5cf162e4d)

Details steps can be found on the [MS Learn docs](https://learn.microsoft.com/en-us/azure/cdn/cdn-custom-ssl?tabs=option-1-default-enable-https-with-a-cdn-managed-certificate)

### Step 5 - Create Azure CosmosDB to store view count for your website

Create a Azure CosmosDB to store the view count for our webpage. Steps followed on [MS Learn docs](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal)

### Step 6 - Create API using Azure Function App to get and increment view count stored in CosmosDB

Now it's time to create Azure function. For this I used visual studio extension "Azure Function". In Visual Studio select the Azure Functions extension and create a new Azure function and select your language of choice, I selected Python.

![image](https://github.com/user-attachments/assets/0bbbd453-cb7f-422b-ba75-cd5cbce3cd8e)

Note: For Python I had issues setting this up using new Python versions so I installed Python 3.9 and it worked :)

Essentially what we want our function app to do is connect to the CosmosDB, retrieve the view count, increment the view count and store the new value back in CosmosDB. There are many ways to accomplish this but below is my Python code for completing this

```
import os
import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions
import json

app = func.FunctionApp()

# Initialize the Cosmos client using the connection string from environment variables
connection_string = os.getenv('AzureResumeConnectionString')
client = CosmosClient.from_connection_string(connection_string)

database_name = <DB-NAME>
container_name = <CONTAINER-NAME>

@app.function_name(name="IncrementCounter")
@app.route(route="increment-counter", auth_level=func.AuthLevel.ANONYMOUS)
def increment_counter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        # Retrieve the item with id '1'
        item = container.read_item(item='1', partition_key='1')
        current_value = item.get('value', 0)

        # Increment the value by 1
        new_value = current_value + 1
        item['value'] = new_value

        # Save the updated item back to the container
        container.upsert_item(item)

        return func.HttpResponse(
            json.dumps({"count": new_value}),
            mimetype="application/json",
            status_code=200
        )

    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occurred: {e}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)
```

With a working function to deploy this to Azure go into Visual Studio code, right click on your Azure Function local project and select deploy to Azure.

![image](https://github.com/user-attachments/assets/d462c120-16f6-4ab2-8ff6-a3a81a9f4b2a)


### Step 7 - Write some JavaScript to call Azure function and display view count on your website

With a deployed funcation app now I can write some JS code to call the function app to get the view count and display that on my website. Again there's many ways to achieve this, below is my way assuming there is an html element with the id of 'counter' in index.html

```
window.addEventListener('DOMContentLoaded', (event) => {
    getVistitCount();
});

const functionApi = '<FUNCTION-APP-ENDPOINT>;

const getVistitCount = () => {
    let count = 0;
    fetch(functionApi).then(response => {
        return response.json();
    }).then(response => {
        console.log('Website called function API.');
        count = response.count;
        document.getElementById('counter').innerText = count;
    }).catch(err => {
        console.error(err);
    });
    return count;
}
```

### Step 8 - CI/CD for Front End

Now to setup the CI/CD for the front end I used Github actions to push my files to my Azure storage account whenever I push to the main branch from my frontend folder. Below is my yml file to achieve this which is based of the [MS Learn guide](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-static-site-github-actions?tabs=userlevel)

```
name: Blob storage website CI

on:
    push:
        branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: azure/login@v1
      with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Upload to blob storage
      uses: azure/CLI@v1
      with:
        inlineScript: |
            az storage blob upload-batch --account-name <STORAGE_ACCOUNT_NAME> --auth-mode key -d '$web' -s .
    - name: Purge CDN endpoint
      uses: azure/CLI@v1
      with:
        inlineScript: |
           az cdn endpoint purge --content-paths  "/*" --profile-name "CDN_PROFILE_NAME" --name "CDN_ENDPOINT" --resource-group "RESOURCE_GROUP"

  # Azure logout
    - name: logout
      run: |
            az logout
      if: always()
```

### Step 9 - CI/CD for Back End

Simillar to the front end I used Github actions to push my Azure function to Azure whenever I push to the main branch from my backend folder. Below is my yml file to achieve this which is based of the [MS Learn guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions?tabs=linux%2Cdotnet&pivots=method-template)

```
name: Deploy Python project to Azure Function App

on:
  [push]

env:
  AZURE_FUNCTIONAPP_NAME: 'your-app-name'   # set this to your function app name on Azure
  AZURE_FUNCTIONAPP_PACKAGE_PATH: '.'       # set this to the path to your function app project, defaults to the repository root
  PYTHON_VERSION: '3.9'                     # set this to the python version to use (e.g. '3.6', '3.7', '3.8')

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment: dev
    steps:
    - name: 'Checkout GitHub Action'
      uses: actions/checkout@v3

    - name: Setup Python ${{ env.PYTHON_VERSION }} Environment
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}

    - name: 'Resolve Project Dependencies Using Pip'
      shell: bash
      run: |
        pushd './${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}'
        python -m pip install --upgrade pip
        pip install -r requirements.txt --target=".python_packages/lib/site-packages"
        popd

    - name: 'Run Azure Functions Action'
      uses: Azure/functions-action@v1
      id: fa
      with:
        app-name: ${{ env.AZURE_FUNCTIONAPP_NAME }}
        package: ${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}
        publish-profile: ${{ secrets.AZURE_FUNCTIONAPP_PUBLISH_PROFILE }}
        scm-do-build-during-deployment: true
        enable-oryx-build: true
```




