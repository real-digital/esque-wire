from typing import overload

from .protocol.request import Response
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
    def send(self, request_data: ProduceRequestData) -> Response[ProduceRequestData, ProduceResponseData]:
        ...

    @overload
    def send(self, request_data: FetchRequestData) -> Response[FetchRequestData, FetchResponseData]:
        ...

    @overload
    def send(self, request_data: ListOffsetsRequestData) -> Response[ListOffsetsRequestData, ListOffsetsResponseData]:
        ...

    @overload
    def send(self, request_data: MetadataRequestData) -> Response[MetadataRequestData, MetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: LeaderAndIsrRequestData
    ) -> Response[LeaderAndIsrRequestData, LeaderAndIsrResponseData]:
        ...

    @overload
    def send(self, request_data: StopReplicaRequestData) -> Response[StopReplicaRequestData, StopReplicaResponseData]:
        ...

    @overload
    def send(
        self, request_data: UpdateMetadataRequestData
    ) -> Response[UpdateMetadataRequestData, UpdateMetadataResponseData]:
        ...

    @overload
    def send(
        self, request_data: ControlledShutdownRequestData
    ) -> Response[ControlledShutdownRequestData, ControlledShutdownResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetCommitRequestData
    ) -> Response[OffsetCommitRequestData, OffsetCommitResponseData]:
        ...

    @overload
    def send(self, request_data: OffsetFetchRequestData) -> Response[OffsetFetchRequestData, OffsetFetchResponseData]:
        ...

    @overload
    def send(
        self, request_data: FindCoordinatorRequestData
    ) -> Response[FindCoordinatorRequestData, FindCoordinatorResponseData]:
        ...

    @overload
    def send(self, request_data: JoinGroupRequestData) -> Response[JoinGroupRequestData, JoinGroupResponseData]:
        ...

    @overload
    def send(self, request_data: HeartbeatRequestData) -> Response[HeartbeatRequestData, HeartbeatResponseData]:
        ...

    @overload
    def send(self, request_data: LeaveGroupRequestData) -> Response[LeaveGroupRequestData, LeaveGroupResponseData]:
        ...

    @overload
    def send(self, request_data: SyncGroupRequestData) -> Response[SyncGroupRequestData, SyncGroupResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeGroupsRequestData
    ) -> Response[DescribeGroupsRequestData, DescribeGroupsResponseData]:
        ...

    @overload
    def send(self, request_data: ListGroupsRequestData) -> Response[ListGroupsRequestData, ListGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslHandshakeRequestData
    ) -> Response[SaslHandshakeRequestData, SaslHandshakeResponseData]:
        ...

    @overload
    def send(self, request_data: ApiVersionsRequestData) -> Response[ApiVersionsRequestData, ApiVersionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateTopicsRequestData
    ) -> Response[CreateTopicsRequestData, CreateTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteTopicsRequestData
    ) -> Response[DeleteTopicsRequestData, DeleteTopicsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteRecordsRequestData
    ) -> Response[DeleteRecordsRequestData, DeleteRecordsResponseData]:
        ...

    @overload
    def send(
        self, request_data: InitProducerIdRequestData
    ) -> Response[InitProducerIdRequestData, InitProducerIdResponseData]:
        ...

    @overload
    def send(
        self, request_data: OffsetForLeaderEpochRequestData
    ) -> Response[OffsetForLeaderEpochRequestData, OffsetForLeaderEpochResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddPartitionsToTxnRequestData
    ) -> Response[AddPartitionsToTxnRequestData, AddPartitionsToTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: AddOffsetsToTxnRequestData
    ) -> Response[AddOffsetsToTxnRequestData, AddOffsetsToTxnResponseData]:
        ...

    @overload
    def send(self, request_data: EndTxnRequestData) -> Response[EndTxnRequestData, EndTxnResponseData]:
        ...

    @overload
    def send(
        self, request_data: WriteTxnMarkersRequestData
    ) -> Response[WriteTxnMarkersRequestData, WriteTxnMarkersResponseData]:
        ...

    @overload
    def send(
        self, request_data: TxnOffsetCommitRequestData
    ) -> Response[TxnOffsetCommitRequestData, TxnOffsetCommitResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeAclsRequestData
    ) -> Response[DescribeAclsRequestData, DescribeAclsResponseData]:
        ...

    @overload
    def send(self, request_data: CreateAclsRequestData) -> Response[CreateAclsRequestData, CreateAclsResponseData]:
        ...

    @overload
    def send(self, request_data: DeleteAclsRequestData) -> Response[DeleteAclsRequestData, DeleteAclsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeConfigsRequestData
    ) -> Response[DescribeConfigsRequestData, DescribeConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterConfigsRequestData
    ) -> Response[AlterConfigsRequestData, AlterConfigsResponseData]:
        ...

    @overload
    def send(
        self, request_data: AlterReplicaLogDirsRequestData
    ) -> Response[AlterReplicaLogDirsRequestData, AlterReplicaLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeLogDirsRequestData
    ) -> Response[DescribeLogDirsRequestData, DescribeLogDirsResponseData]:
        ...

    @overload
    def send(
        self, request_data: SaslAuthenticateRequestData
    ) -> Response[SaslAuthenticateRequestData, SaslAuthenticateResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreatePartitionsRequestData
    ) -> Response[CreatePartitionsRequestData, CreatePartitionsResponseData]:
        ...

    @overload
    def send(
        self, request_data: CreateDelegationTokenRequestData
    ) -> Response[CreateDelegationTokenRequestData, CreateDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: RenewDelegationTokenRequestData
    ) -> Response[RenewDelegationTokenRequestData, RenewDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: ExpireDelegationTokenRequestData
    ) -> Response[ExpireDelegationTokenRequestData, ExpireDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DescribeDelegationTokenRequestData
    ) -> Response[DescribeDelegationTokenRequestData, DescribeDelegationTokenResponseData]:
        ...

    @overload
    def send(
        self, request_data: DeleteGroupsRequestData
    ) -> Response[DeleteGroupsRequestData, DeleteGroupsResponseData]:
        ...

    @overload
    def send(
        self, request_data: ElectPreferredLeadersRequestData
    ) -> Response[ElectPreferredLeadersRequestData, ElectPreferredLeadersResponseData]:
        ...

    @overload
    def send(
        self, request_data: IncrementalAlterConfigsRequestData
    ) -> Response[IncrementalAlterConfigsRequestData, IncrementalAlterConfigsResponseData]:
        ...

    def send(self, request_data: RequestData) -> Response:
        return self._send(request_data)

    def _send(self, request_data: RequestData) -> Response:
        raise NotImplementedError()
