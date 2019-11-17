##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.fetch_response import (
    AbortedTransaction,
    FetchResponseData,
    PartitionHeader,
    PartitionResponse,
    Response,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    nullableBytesSerializer,
    stringSerializer,
)


abortedTransactionSchemas: Dict[int, Schema] = {
    4: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    5: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    6: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    7: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    8: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    9: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    10: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
    11: [
        ('producer_id', int64Serializer),
        ('first_offset', int64Serializer),
    ],
}


abortedTransactionSerializers: Dict[int, DataClassSerializer[AbortedTransaction]] = {
    version: DataClassSerializer(AbortedTransaction, schema) for version, schema
    in abortedTransactionSchemas.items()
}


partitionHeaderSchemas: Dict[int, Schema] = {
    0: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', DummySerializer(int64Serializer.default)),
        ('log_start_offset', DummySerializer(int64Serializer.default)),
        ('aborted_transactions', DummySerializer(ArraySerializer(abortedTransactionSerializers[0]).default)),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    1: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', DummySerializer(int64Serializer.default)),
        ('log_start_offset', DummySerializer(int64Serializer.default)),
        ('aborted_transactions', DummySerializer(ArraySerializer(abortedTransactionSerializers[0]).default)),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    2: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', DummySerializer(int64Serializer.default)),
        ('log_start_offset', DummySerializer(int64Serializer.default)),
        ('aborted_transactions', DummySerializer(ArraySerializer(abortedTransactionSerializers[0]).default)),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    3: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', DummySerializer(int64Serializer.default)),
        ('log_start_offset', DummySerializer(int64Serializer.default)),
        ('aborted_transactions', DummySerializer(ArraySerializer(abortedTransactionSerializers[0]).default)),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    4: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[4])),
        ('log_start_offset', DummySerializer(int64Serializer.default)),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    5: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[5])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    6: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[6])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    7: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[7])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    8: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[8])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    9: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[9])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    10: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[10])),
        ('preferred_read_replica', DummySerializer(int32Serializer.default)),
    ],
    11: [
        ('partition', int32Serializer),
        ('error_code', int16Serializer),
        ('high_watermark', int64Serializer),
        ('last_stable_offset', int64Serializer),
        ('log_start_offset', int64Serializer),
        ('aborted_transactions', ArraySerializer(abortedTransactionSerializers[11])),
        ('preferred_read_replica', int32Serializer),
    ],
}


partitionHeaderSerializers: Dict[int, DataClassSerializer[PartitionHeader]] = {
    version: DataClassSerializer(PartitionHeader, schema) for version, schema
    in partitionHeaderSchemas.items()
}


partitionResponseSchemas: Dict[int, Schema] = {
    0: [
        ('partition_header', partitionHeaderSerializers[0]),
        ('record_set', nullableBytesSerializer),
    ],
    1: [
        ('partition_header', partitionHeaderSerializers[1]),
        ('record_set', nullableBytesSerializer),
    ],
    2: [
        ('partition_header', partitionHeaderSerializers[2]),
        ('record_set', nullableBytesSerializer),
    ],
    3: [
        ('partition_header', partitionHeaderSerializers[3]),
        ('record_set', nullableBytesSerializer),
    ],
    4: [
        ('partition_header', partitionHeaderSerializers[4]),
        ('record_set', nullableBytesSerializer),
    ],
    5: [
        ('partition_header', partitionHeaderSerializers[5]),
        ('record_set', nullableBytesSerializer),
    ],
    6: [
        ('partition_header', partitionHeaderSerializers[6]),
        ('record_set', nullableBytesSerializer),
    ],
    7: [
        ('partition_header', partitionHeaderSerializers[7]),
        ('record_set', nullableBytesSerializer),
    ],
    8: [
        ('partition_header', partitionHeaderSerializers[8]),
        ('record_set', nullableBytesSerializer),
    ],
    9: [
        ('partition_header', partitionHeaderSerializers[9]),
        ('record_set', nullableBytesSerializer),
    ],
    10: [
        ('partition_header', partitionHeaderSerializers[10]),
        ('record_set', nullableBytesSerializer),
    ],
    11: [
        ('partition_header', partitionHeaderSerializers[11]),
        ('record_set', nullableBytesSerializer),
    ],
}


partitionResponseSerializers: Dict[int, DataClassSerializer[PartitionResponse]] = {
    version: DataClassSerializer(PartitionResponse, schema) for version, schema
    in partitionResponseSchemas.items()
}


responseSchemas: Dict[int, Schema] = {
    0: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[0])),
    ],
    1: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[1])),
    ],
    2: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[2])),
    ],
    3: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[3])),
    ],
    4: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[4])),
    ],
    5: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[5])),
    ],
    6: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[6])),
    ],
    7: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[7])),
    ],
    8: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[8])),
    ],
    9: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[9])),
    ],
    10: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[10])),
    ],
    11: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[11])),
    ],
}


responseSerializers: Dict[int, DataClassSerializer[Response]] = {
    version: DataClassSerializer(Response, schema) for version, schema
    in responseSchemas.items()
}


fetchResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ('responses', ArraySerializer(responseSerializers[0])),
        ('throttle_time_ms', DummySerializer(0)),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    1: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[1])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    2: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[2])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    3: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[3])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    4: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[4])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    5: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[5])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    6: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[6])),
        ('error_code', DummySerializer(int16Serializer.default)),
        ('session_id', DummySerializer(int32Serializer.default)),
    ],
    7: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('session_id', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[7])),
    ],
    8: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('session_id', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[8])),
    ],
    9: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('session_id', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[9])),
    ],
    10: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('session_id', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[10])),
    ],
    11: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('session_id', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[11])),
    ],
}


fetchResponseDataSerializers: Dict[int, DataClassSerializer[FetchResponseData]] = {
    version: DataClassSerializer(FetchResponseData, schema) for version, schema
    in fetchResponseDataSchemas.items()
}

