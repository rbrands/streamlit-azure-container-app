# streamlit-azure-container-app
Example for Python Streamlit app with Azure Function backend deployed as Azure Container App

## Developing in codespaces

Install the Functions Core tooling with the following command in the Terminal window:

    npm i -g azure-functions-core-tools@4 --unsafe-perm true

To start the Function App locally (inside the codespace):

    dotnet restore
    dotnet build
    func start

Split the Terminal window, go to the Frontend directory and start Streamlit

    streamlit run Start.py



