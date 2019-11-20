from typing import overload

from .protocol.request import Request
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
    def send(self, request_data: ProduceRequestData) -> Request[ProduceRequestData, ProduceResponseData]:
        ...

    @overload
    def send(self, request_data: FetchRequestData) -> Request[FetchRequestData, FetchResponseData]:
        ...

    @overload
    def send(self, request_data: ListOffsetsRequestData) -> Request[ListOffsetsRequestData, ListOffsetsResponseData]:
        ...

    @overload
    def send(self, request_data: MetadataRequestData) -> Request[MetadataRequestData, MetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: LeaderAndIsrRequestData
    ) -> Request[LeaderAndIsrRequestData, LeaderAndIsrResponseData]:
        ...

    @overload
    def send(self, request_data: StopReplicaRequestData) -> Request[StopReplicaRequestData, StopReplicaResponseData]:
        ...

    @overload
    def send(
        self, request_data: UpdateMetadataRequestData
    ) -> Request[UpdateMetadataRequestData, UpdateMetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: ControlledShutdownRequestData
    ) -> Request[ControlledShutdownRequestData, ControlledShutdownResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetCommitRequestData
    ) -> Request[OffsetCommitRequestData, OffsetCommitResponseData]:
        ...

    @overload
    def send(self, request_data: OffsetFetchRequestData) -> Request[OffsetFetchRequestData, OffsetFetchResponseData]:
        ...

    @overload
    def send(
        self, request_data: FindCoordinatorRequestData
    ) -> Request[FindCoordinatorRequestData, FindCoordinatorResponseData]:
        ...

    @overload
    def send(self, request_data: JoinGroupRequestData) -> Request[JoinGroupRequestData, JoinGroupResponseData]:
        ...

    @overload
    def send(self, request_data: HeartbeatRequestData) -> Request[HeartbeatRequestData, HeartbeatResponseData]:
        ...

    @overload
    def send(self, request_data: LeaveGroupRequestData) -> Request[LeaveGroupRequestData, LeaveGroupResponseData]:
        ...

    @overload
    def send(self, request_data: SyncGroupRequestData) -> Request[SyncGroupRequestData, SyncGroupResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeGroupsRequestData
    ) -> Request[DescribeGroupsRequestData, DescribeGroupsResponseData]:
        ...

    @overload
    def send(self, request_data: ListGroupsRequestData) -> Request[ListGroupsRequestData, ListGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslHandshakeRequestData
    ) -> Request[SaslHandshakeRequestData, SaslHandshakeResponseData]:
        ...

    @overload
    def send(self, request_data: ApiVersionsRequestData) -> Request[ApiVersionsRequestData, ApiVersionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateTopicsRequestData
    ) -> Request[CreateTopicsRequestData, CreateTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteTopicsRequestData
    ) -> Request[DeleteTopicsRequestData, DeleteTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteRecordsRequestData
    ) -> Request[DeleteRecordsRequestData, DeleteRecordsResponseData]:
        ...

    @overload
    def send(
        self, request_data: InitProducerIdRequestData
    ) -> Request[InitProducerIdRequestData, InitProducerIdResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetForLeaderEpochRequestData
    ) -> Request[OffsetForLeaderEpochRequestData, OffsetForLeaderEpochResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddPartitionsToTxnRequestData
    ) -> Request[AddPartitionsToTxnRequestData, AddPartitionsToTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddOffsetsToTxnRequestData
    ) -> Request[AddOffsetsToTxnRequestData, AddOffsetsToTxnResponseData]:
        ...

    @overload
    def send(self, request_data: EndTxnRequestData) -> Request[EndTxnRequestData, EndTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: WriteTxnMarkersRequestData
    ) -> Request[WriteTxnMarkersRequestData, WriteTxnMarkersResponseData]:
        ...

    @overload
    def send(
        self, request_data: TxnOffsetCommitRequestData
    ) -> Request[TxnOffsetCommitRequestData, TxnOffsetCommitResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeAclsRequestData
    ) -> Request[DescribeAclsRequestData, DescribeAclsResponseData]:
        ...

    @overload
    def send(self, request_data: CreateAclsRequestData) -> Request[CreateAclsRequestData, CreateAclsResponseData]:
        ...

    @overload
    def send(self, request_data: DeleteAclsRequestData) -> Request[DeleteAclsRequestData, DeleteAclsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeConfigsRequestData
    ) -> Request[DescribeConfigsRequestData, DescribeConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterConfigsRequestData
    ) -> Request[AlterConfigsRequestData, AlterConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterReplicaLogDirsRequestData
    ) -> Request[AlterReplicaLogDirsRequestData, AlterReplicaLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeLogDirsRequestData
    ) -> Request[DescribeLogDirsRequestData, DescribeLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslAuthenticateRequestData
    ) -> Request[SaslAuthenticateRequestData, SaslAuthenticateResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreatePartitionsRequestData
    ) -> Request[CreatePartitionsRequestData, CreatePartitionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateDelegationTokenRequestData
    ) -> Request[CreateDelegationTokenRequestData, CreateDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: RenewDelegationTokenRequestData
    ) -> Request[RenewDelegationTokenRequestData, RenewDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: ExpireDelegationTokenRequestData
    ) -> Request[ExpireDelegationTokenRequestData, ExpireDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeDelegationTokenRequestData
    ) -> Request[DescribeDelegationTokenRequestData, DescribeDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteGroupsRequestData
    ) -> Request[DeleteGroupsRequestData, DeleteGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: ElectPreferredLeadersRequestData
    ) -> Request[ElectPreferredLeadersRequestData, ElectPreferredLeadersResponseData]:
        ...

    @overload
    def send(
        self, request_data: IncrementalAlterConfigsRequestData
    ) -> Request[IncrementalAlterConfigsRequestData, IncrementalAlterConfigsResponseData]:
        ...

    def send(self, request_data: RequestData) -> Request:
        return self._send(request_data)

    def _send(self, request_data: RequestData) -> Request:
        raise NotImplementedError()
