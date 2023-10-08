# Streamlit Azure Container App
Example for Python Streamlit app with Azure Function backend deployed as Azure Container App

## Developing in codespaces

Install the Functions Core tooling with the following command in the Terminal window:

    npm i -g azure-functions-core-tools@4 --unsafe-perm true

The Function Core Tool is already installed in the corresponding codespace by enabling a feature (see devcontainer.json).

To start the Function App locally (inside the codespace):

    dotnet restore
    dotnet build
    func start

Split the Terminal window, go to the Frontend directory and start Streamlit

    streamlit run Start.py

## Azure Container App

### General approach

To get the application deployed in an Azure Container App follow these steps:
- Create an Azure Container Registry.
- Create an Azure Container Environment and two Azure Container Apps in it (with the default image).
- Create a Dockerfile for the frontend and the API.
- Create the docker images locally (in the codespace) and test them.
- Publish the images to the Azure Container Registry
- Reference the images in the Azure Container App
- Create CI/CD workflow files from the Azure Container App

### Creating the containers

#### Frontend

https://code.visualstudio.com/docs/containers/quickstart-python explains how to build a docker container for a python project. See Dockerfile in folder "Frontend" for the details. To get this adapted to Streamlit see https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

The Streamlit App is listening on port 8501 (that's the default). Set Target Port in Ingress to 8501.


#### Functions APi

See https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-custom-container for details.
In directory ./src/FunctionsApi call

    func init --docker-only
#### Azure Container Registry

Publish the two docker images to Azure Container Registry:

    cd ./src/Frontend
    az acr build --registry <REGISTRY_NAME> --image frontend .
    cd ./src/FunctionsApi
    az acr build --registry <REGISTRY_NAME> --image functionsapi .


