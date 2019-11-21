# esque-wire

A complete and user oriented implementation of the kafka wire protocol.

# Features
## Supports all Api endpoints
Since the code for the API endpoints is automatically generated, this library supports *all* of them.
If a new one comes along, its implementation is just one code execution away. Also the field documentation is extracted
from Kafka source code if there is one.

## Type annotations
Everything is annotated! Enjoy autocomplete all the way to the last field.
```
# run with mypy
from esque_wire import BrokerConnection, ApiVersionsRequestData

request_data = ApiVersionsRequestData()
connection = BrokerConnection("localhost:9092", "test_client")
response = connection.send(request_data)
reveal_type(response)  # Revealed type is '... AnsweredApiCall[... ApiVersionsRequestData, ... ApiVersionsResponseData]'
reveal_type(response.response_data)  # Revealed type is '... ApiVersionsResponseData*'
```