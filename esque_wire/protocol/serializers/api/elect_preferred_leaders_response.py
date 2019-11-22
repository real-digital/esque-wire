###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.elect_preferred_leaders_response import (
    ElectPreferredLeadersResponseData,
    PartitionResult,
    ReplicaElectionResult,
)
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)

partitionResultSchemas: Dict[int, Schema] = {
    0: [
        ("partition_id", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
    ]
}


partitionResultSerializers: Dict[int, ClassSerializer[PartitionResult]] = {
    version: ClassSerializer(PartitionResult, schema) for version, schema in partitionResultSchemas.items()
}

partitionResultSerializers[-1] = partitionResultSerializers[0]


replicaElectionResultSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partition_result", ArraySerializer(partitionResultSerializers[0]))]
}


replicaElectionResultSerializers: Dict[int, ClassSerializer[ReplicaElectionResult]] = {
    version: ClassSerializer(ReplicaElectionResult, schema) for version, schema in replicaElectionResultSchemas.items()
}

replicaElectionResultSerializers[-1] = replicaElectionResultSerializers[0]


electPreferredLeadersResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("replica_election_results", ArraySerializer(replicaElectionResultSerializers[0])),
    ]
}


electPreferredLeadersResponseDataSerializers: Dict[int, ClassSerializer[ElectPreferredLeadersResponseData]] = {
    version: ClassSerializer(ElectPreferredLeadersResponseData, schema)
    for version, schema in electPreferredLeadersResponseDataSchemas.items()
}

electPreferredLeadersResponseDataSerializers[-1] = electPreferredLeadersResponseDataSerializers[0]
