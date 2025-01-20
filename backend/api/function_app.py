import os
import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions

app = func.FunctionApp()

# Initialize the Cosmos client using the connection string from environment variables
connection_string = os.getenv('AzureResumeConnectionString')
client = CosmosClient.from_connection_string(connection_string)

database_name = "CloudResumeChallengejad"
container_name = "Counter"

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

        return func.HttpResponse(f"Counter value incremented to {new_value}", status_code=200)

    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occurred: {e}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)