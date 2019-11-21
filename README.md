# esque-wire

A complete and user oriented implementation of the kafka wire protocol.

# Features
## Supports all Api endpoints
Since the code for the API endpoints is automatically generated, this library supports *all* of them.
If a new one comes along, its implementation is just one code execution away. Also the field documentation is extracted
from Kafka source code if there is one.

## Type annotations
Everything is annotated! Your IDE will help you find what you need!
```
# runner: mypy
from esque_wire import BrokerConnection, ApiVersionsRequestData

request_data = ApiVersionsRequestData()
connection = BrokerConnection("localhost:9092", "test_client")
call = connection.send(request_data)
reveal_type(call)
reveal_tyep(call.response_data)
```