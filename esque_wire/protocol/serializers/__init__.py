###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ..constants import ApiKey
from ..structs.api.api_versions_response import ApiVersion
from .api import (
    addOffsetsToTxnRequestDataSerializers,
    addOffsetsToTxnResponseDataSerializers,
    addPartitionsToTxnRequestDataSerializers,
    addPartitionsToTxnResponseDataSerializers,
    alterConfigsRequestDataSerializers,
    alterConfigsResponseDataSerializers,
    alterReplicaLogDirsRequestDataSerializers,
    alterReplicaLogDirsResponseDataSerializers,
    apiVersionsRequestDataSerializers,
    apiVersionsResponseDataSerializers,
    controlledShutdownRequestDataSerializers,
    controlledShutdownResponseDataSerializers,
    createAclsRequestDataSerializers,
    createAclsResponseDataSerializers,
    createDelegationTokenRequestDataSerializers,
    createDelegationTokenResponseDataSerializers,
    createPartitionsRequestDataSerializers,
    createPartitionsResponseDataSerializers,
    createTopicsRequestDataSerializers,
    createTopicsResponseDataSerializers,
    deleteAclsRequestDataSerializers,
    deleteAclsResponseDataSerializers,
    deleteGroupsRequestDataSerializers,
    deleteGroupsResponseDataSerializers,
    deleteRecordsRequestDataSerializers,
    deleteRecordsResponseDataSerializers,
    deleteTopicsRequestDataSerializers,
    deleteTopicsResponseDataSerializers,
    describeAclsRequestDataSerializers,
    describeAclsResponseDataSerializers,
    describeConfigsRequestDataSerializers,
    describeConfigsResponseDataSerializers,
    describeDelegationTokenRequestDataSerializers,
    describeDelegationTokenResponseDataSerializers,
    describeGroupsRequestDataSerializers,
    describeGroupsResponseDataSerializers,
    describeLogDirsRequestDataSerializers,
    describeLogDirsResponseDataSerializers,
    electPreferredLeadersRequestDataSerializers,
    electPreferredLeadersResponseDataSerializers,
    endTxnRequestDataSerializers,
    endTxnResponseDataSerializers,
    expireDelegationTokenRequestDataSerializers,
    expireDelegationTokenResponseDataSerializers,
    fetchRequestDataSerializers,
    fetchResponseDataSerializers,
    findCoordinatorRequestDataSerializers,
    findCoordinatorResponseDataSerializers,
    heartbeatRequestDataSerializers,
    heartbeatResponseDataSerializers,
    incrementalAlterConfigsRequestDataSerializers,
    incrementalAlterConfigsResponseDataSerializers,
    initProducerIdRequestDataSerializers,
    initProducerIdResponseDataSerializers,
    joinGroupRequestDataSerializers,
    joinGroupResponseDataSerializers,
    leaderAndIsrRequestDataSerializers,
    leaderAndIsrResponseDataSerializers,
    leaveGroupRequestDataSerializers,
    leaveGroupResponseDataSerializers,
    listGroupsRequestDataSerializers,
    listGroupsResponseDataSerializers,
    listOffsetsRequestDataSerializers,
    listOffsetsResponseDataSerializers,
    metadataRequestDataSerializers,
    metadataResponseDataSerializers,
    offsetCommitRequestDataSerializers,
    offsetCommitResponseDataSerializers,
    offsetFetchRequestDataSerializers,
    offsetFetchResponseDataSerializers,
    offsetForLeaderEpochRequestDataSerializers,
    offsetForLeaderEpochResponseDataSerializers,
    produceRequestDataSerializers,
    produceResponseDataSerializers,
    renewDelegationTokenRequestDataSerializers,
    renewDelegationTokenResponseDataSerializers,
    saslAuthenticateRequestDataSerializers,
    saslAuthenticateResponseDataSerializers,
    saslHandshakeRequestDataSerializers,
    saslHandshakeResponseDataSerializers,
    stopReplicaRequestDataSerializers,
    stopReplicaResponseDataSerializers,
    syncGroupRequestDataSerializers,
    syncGroupResponseDataSerializers,
    txnOffsetCommitRequestDataSerializers,
    txnOffsetCommitResponseDataSerializers,
    updateMetadataRequestDataSerializers,
    updateMetadataResponseDataSerializers,
    writeTxnMarkersRequestDataSerializers,
    writeTxnMarkersResponseDataSerializers,
)
from .base import BaseSerializer
from .constants import (
    aclOperationSerializer,
    aclPermissionTypeSerializer,
    apiKeySerializer,
    errorCodeSerializer,
    resourcePatternTypeSerializer,
    resourceTypeSerializer,
)
from .generic import ArraySerializer, ClassSerializer, DummySerializer, Schema
from .primitive import (
    booleanSerializer,
    bytesSerializer,
    int8Serializer,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    nullableBytesSerializer,
    nullableStringSerializer,
    recordsSerializer,
    stringSerializer,
    uint32Serializer,
    varIntSerializer,
    varLongSerializer,
)

REQUEST_SERIALIZERS: Dict[ApiKey, Dict[int, ClassSerializer]] = {
    ApiKey.PRODUCE: produceRequestDataSerializers,
    ApiKey.FETCH: fetchRequestDataSerializers,
    ApiKey.LIST_OFFSETS: listOffsetsRequestDataSerializers,
    ApiKey.METADATA: metadataRequestDataSerializers,
    ApiKey.LEADER_AND_ISR: leaderAndIsrRequestDataSerializers,
    ApiKey.STOP_REPLICA: stopReplicaRequestDataSerializers,
    ApiKey.UPDATE_METADATA: updateMetadataRequestDataSerializers,
    ApiKey.CONTROLLED_SHUTDOWN: controlledShutdownRequestDataSerializers,
    ApiKey.OFFSET_COMMIT: offsetCommitRequestDataSerializers,
    ApiKey.OFFSET_FETCH: offsetFetchRequestDataSerializers,
    ApiKey.FIND_COORDINATOR: findCoordinatorRequestDataSerializers,
    ApiKey.JOIN_GROUP: joinGroupRequestDataSerializers,
    ApiKey.HEARTBEAT: heartbeatRequestDataSerializers,
    ApiKey.LEAVE_GROUP: leaveGroupRequestDataSerializers,
    ApiKey.SYNC_GROUP: syncGroupRequestDataSerializers,
    ApiKey.DESCRIBE_GROUPS: describeGroupsRequestDataSerializers,
    ApiKey.LIST_GROUPS: listGroupsRequestDataSerializers,
    ApiKey.SASL_HANDSHAKE: saslHandshakeRequestDataSerializers,
    ApiKey.API_VERSIONS: apiVersionsRequestDataSerializers,
    ApiKey.CREATE_TOPICS: createTopicsRequestDataSerializers,
    ApiKey.DELETE_TOPICS: deleteTopicsRequestDataSerializers,
    ApiKey.DELETE_RECORDS: deleteRecordsRequestDataSerializers,
    ApiKey.INIT_PRODUCER_ID: initProducerIdRequestDataSerializers,
    ApiKey.OFFSET_FOR_LEADER_EPOCH: offsetForLeaderEpochRequestDataSerializers,
    ApiKey.ADD_PARTITIONS_TO_TXN: addPartitionsToTxnRequestDataSerializers,
    ApiKey.ADD_OFFSETS_TO_TXN: addOffsetsToTxnRequestDataSerializers,
    ApiKey.END_TXN: endTxnRequestDataSerializers,
    ApiKey.WRITE_TXN_MARKERS: writeTxnMarkersRequestDataSerializers,
    ApiKey.TXN_OFFSET_COMMIT: txnOffsetCommitRequestDataSerializers,
    ApiKey.DESCRIBE_ACLS: describeAclsRequestDataSerializers,
    ApiKey.CREATE_ACLS: createAclsRequestDataSerializers,
    ApiKey.DELETE_ACLS: deleteAclsRequestDataSerializers,
    ApiKey.DESCRIBE_CONFIGS: describeConfigsRequestDataSerializers,
    ApiKey.ALTER_CONFIGS: alterConfigsRequestDataSerializers,
    ApiKey.ALTER_REPLICA_LOG_DIRS: alterReplicaLogDirsRequestDataSerializers,
    ApiKey.DESCRIBE_LOG_DIRS: describeLogDirsRequestDataSerializers,
    ApiKey.SASL_AUTHENTICATE: saslAuthenticateRequestDataSerializers,
    ApiKey.CREATE_PARTITIONS: createPartitionsRequestDataSerializers,
    ApiKey.CREATE_DELEGATION_TOKEN: createDelegationTokenRequestDataSerializers,
    ApiKey.RENEW_DELEGATION_TOKEN: renewDelegationTokenRequestDataSerializers,
    ApiKey.EXPIRE_DELEGATION_TOKEN: expireDelegationTokenRequestDataSerializers,
    ApiKey.DESCRIBE_DELEGATION_TOKEN: describeDelegationTokenRequestDataSerializers,
    ApiKey.DELETE_GROUPS: deleteGroupsRequestDataSerializers,
    ApiKey.ELECT_PREFERRED_LEADERS: electPreferredLeadersRequestDataSerializers,
    ApiKey.INCREMENTAL_ALTER_CONFIGS: incrementalAlterConfigsRequestDataSerializers,
}

RESPONSE_SERIALIZERS: Dict[ApiKey, Dict[int, ClassSerializer]] = {
    ApiKey.PRODUCE: produceResponseDataSerializers,
    ApiKey.FETCH: fetchResponseDataSerializers,
    ApiKey.LIST_OFFSETS: listOffsetsResponseDataSerializers,
    ApiKey.METADATA: metadataResponseDataSerializers,
    ApiKey.LEADER_AND_ISR: leaderAndIsrResponseDataSerializers,
    ApiKey.STOP_REPLICA: stopReplicaResponseDataSerializers,
    ApiKey.UPDATE_METADATA: updateMetadataResponseDataSerializers,
    ApiKey.CONTROLLED_SHUTDOWN: controlledShutdownResponseDataSerializers,
    ApiKey.OFFSET_COMMIT: offsetCommitResponseDataSerializers,
    ApiKey.OFFSET_FETCH: offsetFetchResponseDataSerializers,
    ApiKey.FIND_COORDINATOR: findCoordinatorResponseDataSerializers,
    ApiKey.JOIN_GROUP: joinGroupResponseDataSerializers,
    ApiKey.HEARTBEAT: heartbeatResponseDataSerializers,
    ApiKey.LEAVE_GROUP: leaveGroupResponseDataSerializers,
    ApiKey.SYNC_GROUP: syncGroupResponseDataSerializers,
    ApiKey.DESCRIBE_GROUPS: describeGroupsResponseDataSerializers,
    ApiKey.LIST_GROUPS: listGroupsResponseDataSerializers,
    ApiKey.SASL_HANDSHAKE: saslHandshakeResponseDataSerializers,
    ApiKey.API_VERSIONS: apiVersionsResponseDataSerializers,
    ApiKey.CREATE_TOPICS: createTopicsResponseDataSerializers,
    ApiKey.DELETE_TOPICS: deleteTopicsResponseDataSerializers,
    ApiKey.DELETE_RECORDS: deleteRecordsResponseDataSerializers,
    ApiKey.INIT_PRODUCER_ID: initProducerIdResponseDataSerializers,
    ApiKey.OFFSET_FOR_LEADER_EPOCH: offsetForLeaderEpochResponseDataSerializers,
    ApiKey.ADD_PARTITIONS_TO_TXN: addPartitionsToTxnResponseDataSerializers,
    ApiKey.ADD_OFFSETS_TO_TXN: addOffsetsToTxnResponseDataSerializers,
    ApiKey.END_TXN: endTxnResponseDataSerializers,
    ApiKey.WRITE_TXN_MARKERS: writeTxnMarkersResponseDataSerializers,
    ApiKey.TXN_OFFSET_COMMIT: txnOffsetCommitResponseDataSerializers,
    ApiKey.DESCRIBE_ACLS: describeAclsResponseDataSerializers,
    ApiKey.CREATE_ACLS: createAclsResponseDataSerializers,
    ApiKey.DELETE_ACLS: deleteAclsResponseDataSerializers,
    ApiKey.DESCRIBE_CONFIGS: describeConfigsResponseDataSerializers,
    ApiKey.ALTER_CONFIGS: alterConfigsResponseDataSerializers,
    ApiKey.ALTER_REPLICA_LOG_DIRS: alterReplicaLogDirsResponseDataSerializers,
    ApiKey.DESCRIBE_LOG_DIRS: describeLogDirsResponseDataSerializers,
    ApiKey.SASL_AUTHENTICATE: saslAuthenticateResponseDataSerializers,
    ApiKey.CREATE_PARTITIONS: createPartitionsResponseDataSerializers,
    ApiKey.CREATE_DELEGATION_TOKEN: createDelegationTokenResponseDataSerializers,
    ApiKey.RENEW_DELEGATION_TOKEN: renewDelegationTokenResponseDataSerializers,
    ApiKey.EXPIRE_DELEGATION_TOKEN: expireDelegationTokenResponseDataSerializers,
    ApiKey.DESCRIBE_DELEGATION_TOKEN: describeDelegationTokenResponseDataSerializers,
    ApiKey.DELETE_GROUPS: deleteGroupsResponseDataSerializers,
    ApiKey.ELECT_PREFERRED_LEADERS: electPreferredLeadersResponseDataSerializers,
    ApiKey.INCREMENTAL_ALTER_CONFIGS: incrementalAlterConfigsResponseDataSerializers,
}

SUPPORTED_API_VERSIONS: Dict[ApiKey, ApiVersion] = {
    api_key: ApiVersion(api_key, min(serializers.keys()), max(serializers.keys()))
    for api_key, serializers in REQUEST_SERIALIZERS.items()
}
