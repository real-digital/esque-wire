from typing import overload

from .protocol.api_call import ApiCall
from .protocol.structs.api import (
    AddOffsetsToTxnRequestData,
    AddOffsetsToTxnResponseData,
    AddPartitionsToTxnRequestData,
    AddPartitionsToTxnResponseData,
    AlterConfigsRequestData,
    AlterConfigsResponseData,
    AlterReplicaLogDirsRequestData,
    AlterReplicaLogDirsResponseData,
    ApiVersionsRequestData,
    ApiVersionsResponseData,
    ControlledShutdownRequestData,
    ControlledShutdownResponseData,
    CreateAclsRequestData,
    CreateAclsResponseData,
    CreateDelegationTokenRequestData,
    CreateDelegationTokenResponseData,
    CreatePartitionsRequestData,
    CreatePartitionsResponseData,
    CreateTopicsRequestData,
    CreateTopicsResponseData,
    DeleteAclsRequestData,
    DeleteAclsResponseData,
    DeleteGroupsRequestData,
    DeleteGroupsResponseData,
    DeleteRecordsRequestData,
    DeleteRecordsResponseData,
    DeleteTopicsRequestData,
    DeleteTopicsResponseData,
    DescribeAclsRequestData,
    DescribeAclsResponseData,
    DescribeConfigsRequestData,
    DescribeConfigsResponseData,
    DescribeDelegationTokenRequestData,
    DescribeDelegationTokenResponseData,
    DescribeGroupsRequestData,
    DescribeGroupsResponseData,
    DescribeLogDirsRequestData,
    DescribeLogDirsResponseData,
    ElectPreferredLeadersRequestData,
    ElectPreferredLeadersResponseData,
    EndTxnRequestData,
    EndTxnResponseData,
    ExpireDelegationTokenRequestData,
    ExpireDelegationTokenResponseData,
    FetchRequestData,
    FetchResponseData,
    FindCoordinatorRequestData,
    FindCoordinatorResponseData,
    HeartbeatRequestData,
    HeartbeatResponseData,
    IncrementalAlterConfigsRequestData,
    IncrementalAlterConfigsResponseData,
    InitProducerIdRequestData,
    InitProducerIdResponseData,
    JoinGroupRequestData,
    JoinGroupResponseData,
    LeaderAndIsrRequestData,
    LeaderAndIsrResponseData,
    LeaveGroupRequestData,
    LeaveGroupResponseData,
    ListGroupsRequestData,
    ListGroupsResponseData,
    ListOffsetsRequestData,
    ListOffsetsResponseData,
    MetadataRequestData,
    MetadataResponseData,
    OffsetCommitRequestData,
    OffsetCommitResponseData,
    OffsetFetchRequestData,
    OffsetFetchResponseData,
    OffsetForLeaderEpochRequestData,
    OffsetForLeaderEpochResponseData,
    ProduceRequestData,
    ProduceResponseData,
    RenewDelegationTokenRequestData,
    RenewDelegationTokenResponseData,
    SaslAuthenticateRequestData,
    SaslAuthenticateResponseData,
    SaslHandshakeRequestData,
    SaslHandshakeResponseData,
    StopReplicaRequestData,
    StopReplicaResponseData,
    SyncGroupRequestData,
    SyncGroupResponseData,
    TxnOffsetCommitRequestData,
    TxnOffsetCommitResponseData,
    UpdateMetadataRequestData,
    UpdateMetadataResponseData,
    WriteTxnMarkersRequestData,
    WriteTxnMarkersResponseData,
)
from .protocol.structs.base import RequestData


class BaseBrokerConnection:
    @overload
    def send(self, request_data: ProduceRequestData) -> ApiCall[ProduceRequestData, ProduceResponseData]:
        ...

    @overload
    def send(self, request_data: FetchRequestData) -> ApiCall[FetchRequestData, FetchResponseData]:
        ...

    @overload
    def send(self, request_data: ListOffsetsRequestData) -> ApiCall[ListOffsetsRequestData, ListOffsetsResponseData]:
        ...

    @overload
    def send(self, request_data: MetadataRequestData) -> ApiCall[MetadataRequestData, MetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: LeaderAndIsrRequestData
    ) -> ApiCall[LeaderAndIsrRequestData, LeaderAndIsrResponseData]:
        ...

    @overload
    def send(self, request_data: StopReplicaRequestData) -> ApiCall[StopReplicaRequestData, StopReplicaResponseData]:
        ...

    @overload
    def send(
        self, request_data: UpdateMetadataRequestData
    ) -> ApiCall[UpdateMetadataRequestData, UpdateMetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: ControlledShutdownRequestData
    ) -> ApiCall[ControlledShutdownRequestData, ControlledShutdownResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetCommitRequestData
    ) -> ApiCall[OffsetCommitRequestData, OffsetCommitResponseData]:
        ...

    @overload
    def send(self, request_data: OffsetFetchRequestData) -> ApiCall[OffsetFetchRequestData, OffsetFetchResponseData]:
        ...

    @overload
    def send(
        self, request_data: FindCoordinatorRequestData
    ) -> ApiCall[FindCoordinatorRequestData, FindCoordinatorResponseData]:
        ...

    @overload
    def send(self, request_data: JoinGroupRequestData) -> ApiCall[JoinGroupRequestData, JoinGroupResponseData]:
        ...

    @overload
    def send(self, request_data: HeartbeatRequestData) -> ApiCall[HeartbeatRequestData, HeartbeatResponseData]:
        ...

    @overload
    def send(self, request_data: LeaveGroupRequestData) -> ApiCall[LeaveGroupRequestData, LeaveGroupResponseData]:
        ...

    @overload
    def send(self, request_data: SyncGroupRequestData) -> ApiCall[SyncGroupRequestData, SyncGroupResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeGroupsRequestData
    ) -> ApiCall[DescribeGroupsRequestData, DescribeGroupsResponseData]:
        ...

    @overload
    def send(self, request_data: ListGroupsRequestData) -> ApiCall[ListGroupsRequestData, ListGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslHandshakeRequestData
    ) -> ApiCall[SaslHandshakeRequestData, SaslHandshakeResponseData]:
        ...

    @overload
    def send(self, request_data: ApiVersionsRequestData) -> ApiCall[ApiVersionsRequestData, ApiVersionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateTopicsRequestData
    ) -> ApiCall[CreateTopicsRequestData, CreateTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteTopicsRequestData
    ) -> ApiCall[DeleteTopicsRequestData, DeleteTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteRecordsRequestData
    ) -> ApiCall[DeleteRecordsRequestData, DeleteRecordsResponseData]:
        ...

    @overload
    def send(
        self, request_data: InitProducerIdRequestData
    ) -> ApiCall[InitProducerIdRequestData, InitProducerIdResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetForLeaderEpochRequestData
    ) -> ApiCall[OffsetForLeaderEpochRequestData, OffsetForLeaderEpochResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddPartitionsToTxnRequestData
    ) -> ApiCall[AddPartitionsToTxnRequestData, AddPartitionsToTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddOffsetsToTxnRequestData
    ) -> ApiCall[AddOffsetsToTxnRequestData, AddOffsetsToTxnResponseData]:
        ...

    @overload
    def send(self, request_data: EndTxnRequestData) -> ApiCall[EndTxnRequestData, EndTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: WriteTxnMarkersRequestData
    ) -> ApiCall[WriteTxnMarkersRequestData, WriteTxnMarkersResponseData]:
        ...

    @overload
    def send(
        self, request_data: TxnOffsetCommitRequestData
    ) -> ApiCall[TxnOffsetCommitRequestData, TxnOffsetCommitResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeAclsRequestData
    ) -> ApiCall[DescribeAclsRequestData, DescribeAclsResponseData]:
        ...

    @overload
    def send(self, request_data: CreateAclsRequestData) -> ApiCall[CreateAclsRequestData, CreateAclsResponseData]:
        ...

    @overload
    def send(self, request_data: DeleteAclsRequestData) -> ApiCall[DeleteAclsRequestData, DeleteAclsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeConfigsRequestData
    ) -> ApiCall[DescribeConfigsRequestData, DescribeConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterConfigsRequestData
    ) -> ApiCall[AlterConfigsRequestData, AlterConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterReplicaLogDirsRequestData
    ) -> ApiCall[AlterReplicaLogDirsRequestData, AlterReplicaLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeLogDirsRequestData
    ) -> ApiCall[DescribeLogDirsRequestData, DescribeLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslAuthenticateRequestData
    ) -> ApiCall[SaslAuthenticateRequestData, SaslAuthenticateResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreatePartitionsRequestData
    ) -> ApiCall[CreatePartitionsRequestData, CreatePartitionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateDelegationTokenRequestData
    ) -> ApiCall[CreateDelegationTokenRequestData, CreateDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: RenewDelegationTokenRequestData
    ) -> ApiCall[RenewDelegationTokenRequestData, RenewDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: ExpireDelegationTokenRequestData
    ) -> ApiCall[ExpireDelegationTokenRequestData, ExpireDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeDelegationTokenRequestData
    ) -> ApiCall[DescribeDelegationTokenRequestData, DescribeDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteGroupsRequestData
    ) -> ApiCall[DeleteGroupsRequestData, DeleteGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: ElectPreferredLeadersRequestData
    ) -> ApiCall[ElectPreferredLeadersRequestData, ElectPreferredLeadersResponseData]:
        ...

    @overload
    def send(
        self, request_data: IncrementalAlterConfigsRequestData
    ) -> ApiCall[IncrementalAlterConfigsRequestData, IncrementalAlterConfigsResponseData]:
        ...

    def send(self, request_data: RequestData) -> ApiCall:
        return self._send(request_data)

    def _send(self, request_data: RequestData) -> ApiCall:
        raise NotImplementedError()
