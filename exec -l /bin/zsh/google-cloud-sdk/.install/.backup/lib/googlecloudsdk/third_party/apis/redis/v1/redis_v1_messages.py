"""Generated message classes for redis version v1.

Creates and manages Redis instances on the Google Cloud Platform.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'redis'


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ExportInstanceRequest(_messages.Message):
  r"""Request for Export.

  Fields:
    outputConfig: Required. Specify data to be exported.
  """

  outputConfig = _messages.MessageField('OutputConfig', 1)


class FailoverInstanceRequest(_messages.Message):
  r"""Request for Failover.

  Enums:
    DataProtectionModeValueValuesEnum: Optional. Available data protection
      modes that the user can choose. If it's unspecified, data protection
      mode will be LIMITED_DATA_LOSS by default.

  Fields:
    dataProtectionMode: Optional. Available data protection modes that the
      user can choose. If it's unspecified, data protection mode will be
      LIMITED_DATA_LOSS by default.
  """

  class DataProtectionModeValueValuesEnum(_messages.Enum):
    r"""Optional. Available data protection modes that the user can choose. If
    it's unspecified, data protection mode will be LIMITED_DATA_LOSS by
    default.

    Values:
      DATA_PROTECTION_MODE_UNSPECIFIED: Defaults to LIMITED_DATA_LOSS if a
        data protection mode is not specified.
      LIMITED_DATA_LOSS: Instance failover will be protected with data loss
        control. More specifically, the failover will only be performed if the
        current replication offset diff between main and replica is under a
        certain threshold.
      FORCE_DATA_LOSS: Instance failover will be performed without data loss
        control.
    """
    DATA_PROTECTION_MODE_UNSPECIFIED = 0
    LIMITED_DATA_LOSS = 1
    FORCE_DATA_LOSS = 2

  dataProtectionMode = _messages.EnumField('DataProtectionModeValueValuesEnum', 1)


class GcsDestination(_messages.Message):
  r"""The Cloud Storage location for the output content

  Fields:
    uri: Required. Data destination URI (e.g. 'gs://my_bucket/my_object').
      Existing files will be overwritten.
  """

  uri = _messages.StringField(1)


class GcsSource(_messages.Message):
  r"""The Cloud Storage location for the input content

  Fields:
    uri: Required. Source data URI. (e.g. 'gs://my_bucket/my_object').
  """

  uri = _messages.StringField(1)


class GoogleCloudRedisV1LocationMetadata(_messages.Message):
  r"""This location metadata represents additional configuration options for a
  given location where a Redis instance may be created. All fields are output
  only. It is returned as content of the
  `google.cloud.location.Location.metadata` field.

  Messages:
    AvailableZonesValue: Output only. The set of available zones in the
      location. The map is keyed by the lowercase ID of each zone, as defined
      by GCE. These keys can be specified in `location_id` or
      `alternative_location_id` fields when creating a Redis instance.

  Fields:
    availableZones: Output only. The set of available zones in the location.
      The map is keyed by the lowercase ID of each zone, as defined by GCE.
      These keys can be specified in `location_id` or
      `alternative_location_id` fields when creating a Redis instance.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AvailableZonesValue(_messages.Message):
    r"""Output only. The set of available zones in the location. The map is
    keyed by the lowercase ID of each zone, as defined by GCE. These keys can
    be specified in `location_id` or `alternative_location_id` fields when
    creating a Redis instance.

    Messages:
      AdditionalProperty: An additional property for a AvailableZonesValue
        object.

    Fields:
      additionalProperties: Additional properties of type AvailableZonesValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a AvailableZonesValue object.

      Fields:
        key: Name of the additional property.
        value: A GoogleCloudRedisV1ZoneMetadata attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('GoogleCloudRedisV1ZoneMetadata', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  availableZones = _messages.MessageField('AvailableZonesValue', 1)


class GoogleCloudRedisV1OperationMetadata(_messages.Message):
  r"""Represents the v1 metadata of the long-running operation.

  Fields:
    apiVersion: API version.
    cancelRequested: Specifies if cancellation was requested for the
      operation.
    createTime: Creation timestamp.
    endTime: End timestamp.
    statusDetail: Operation status details.
    target: Operation target.
    verb: Operation verb.
  """

  apiVersion = _messages.StringField(1)
  cancelRequested = _messages.BooleanField(2)
  createTime = _messages.StringField(3)
  endTime = _messages.StringField(4)
  statusDetail = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class GoogleCloudRedisV1ZoneMetadata(_messages.Message):
  r"""Defines specific information for a particular zone. Currently empty and
  reserved for future use only.
  """



class ImportInstanceRequest(_messages.Message):
  r"""Request for Import.

  Fields:
    inputConfig: Required. Specify data to be imported.
  """

  inputConfig = _messages.MessageField('InputConfig', 1)


class InputConfig(_messages.Message):
  r"""The input content

  Fields:
    gcsSource: Google Cloud Storage location where input content is located.
  """

  gcsSource = _messages.MessageField('GcsSource', 1)


class Instance(_messages.Message):
  r"""A Google Cloud Redis instance.

  Enums:
    ConnectModeValueValuesEnum: Optional. The connect mode of Redis instance.
      If not provided, default one will be used. Current default:
      DIRECT_PEERING.
    StateValueValuesEnum: Output only. The current state of this instance.
    TierValueValuesEnum: Required. The service tier of the instance.

  Messages:
    LabelsValue: Resource labels to represent user provided metadata
    RedisConfigsValue: Optional. Redis configuration parameters, according to
      http://redis.io/topics/config. Currently, the only supported parameters
      are:   Redis version 3.2 and newer:   *   maxmemory-policy  *   notify-
      keyspace-events   Redis version 4.0 and newer:   *   activedefrag  *
      lfu-decay-time  *   lfu-log-factor  *   maxmemory-gb   Redis version 5.0
      and newer:   *   stream-node-max-bytes  *   stream-node-max-entries

  Fields:
    alternativeLocationId: Optional. Only applicable to STANDARD_HA tier which
      protects the instance against zonal failures by provisioning it across
      two zones. If provided, it must be a different zone from the one
      provided in location_id.
    authorizedNetwork: Optional. The full name of the Google Compute Engine
      [network](/compute/docs/networks-and-firewalls#networks) to which the
      instance is connected. If left unspecified, the `default` network will
      be used.
    connectMode: Optional. The connect mode of Redis instance. If not
      provided, default one will be used. Current default: DIRECT_PEERING.
    createTime: Output only. The time the instance was created.
    currentLocationId: Output only. The current zone where the Redis endpoint
      is placed. For Basic Tier instances, this will always be the same as the
      location_id provided by the user at creation time. For Standard Tier
      instances, this can be either location_id or alternative_location_id and
      can change after a failover event.
    displayName: An arbitrary and optional user-provided name for the
      instance.
    host: Output only. Hostname or IP address of the exposed Redis endpoint
      used by clients to connect to the service.
    labels: Resource labels to represent user provided metadata
    locationId: Optional. The zone where the instance will be provisioned. If
      not provided, the service will choose a zone for the instance. For
      STANDARD_HA tier, instances will be created across two zones for
      protection against zonal failures. If alternative_location_id is also
      provided, it must be different from location_id.
    memorySizeGb: Required. Redis memory size in GiB.
    name: Required. Unique name of the resource in this scope including
      project and location using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      Note: Redis instances are managed and addressed at regional level so
      location_id here refers to a GCP region; however, users may choose which
      specific zone (or collection of zones for cross-zone instances) an
      instance should be provisioned in. Refer to location_id and
      alternative_location_id fields for more details.
    persistenceIamIdentity: Output only. Cloud IAM identity used by import /
      export operations to transfer data to/from Cloud Storage. Format is
      "serviceAccount:<service_account_email>". The value may change over time
      for a given instance so should be checked before each import/export
      operation.
    port: Output only. The port number of the exposed Redis endpoint.
    redisConfigs: Optional. Redis configuration parameters, according to
      http://redis.io/topics/config. Currently, the only supported parameters
      are:   Redis version 3.2 and newer:   *   maxmemory-policy  *   notify-
      keyspace-events   Redis version 4.0 and newer:   *   activedefrag  *
      lfu-decay-time  *   lfu-log-factor  *   maxmemory-gb   Redis version 5.0
      and newer:   *   stream-node-max-bytes  *   stream-node-max-entries
    redisVersion: Optional. The version of Redis software. If not provided,
      latest supported version will be used. Currently, the supported values
      are:   *   `REDIS_3_2` for Redis 3.2 compatibility  *   `REDIS_4_0` for
      Redis 4.0 compatibility (default)  *   `REDIS_5_0` for Redis 5.0
      compatibility
    reservedIpRange: Optional. The CIDR range of internal addresses that are
      reserved for this instance. If not provided, the service will choose an
      unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges
      must be unique and non-overlapping with existing subnets in an
      authorized network.
    state: Output only. The current state of this instance.
    statusMessage: Output only. Additional information about the current
      status of this instance, if available.
    tier: Required. The service tier of the instance.
  """

  class ConnectModeValueValuesEnum(_messages.Enum):
    r"""Optional. The connect mode of Redis instance. If not provided, default
    one will be used. Current default: DIRECT_PEERING.

    Values:
      CONNECT_MODE_UNSPECIFIED: Not set.
      DIRECT_PEERING: Connect via directly peering with memorystore redis
        hosted service.
      PRIVATE_SERVICE_ACCESS: Connect with google via private service access
        and share connection across google managed services.
    """
    CONNECT_MODE_UNSPECIFIED = 0
    DIRECT_PEERING = 1
    PRIVATE_SERVICE_ACCESS = 2

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The current state of this instance.

    Values:
      STATE_UNSPECIFIED: Not set.
      CREATING: Redis instance is being created.
      READY: Redis instance has been created and is fully usable.
      UPDATING: Redis instance configuration is being updated. Certain kinds
        of updates may cause the instance to become unusable while the update
        is in progress.
      DELETING: Redis instance is being deleted.
      REPAIRING: Redis instance is being repaired and may be unusable.
      MAINTENANCE: Maintenance is being performed on this Redis instance.
      IMPORTING: Redis instance is importing data (availability may be
        affected).
      FAILING_OVER: Redis instance is failing over (availability may be
        affected).
    """
    STATE_UNSPECIFIED = 0
    CREATING = 1
    READY = 2
    UPDATING = 3
    DELETING = 4
    REPAIRING = 5
    MAINTENANCE = 6
    IMPORTING = 7
    FAILING_OVER = 8

  class TierValueValuesEnum(_messages.Enum):
    r"""Required. The service tier of the instance.

    Values:
      TIER_UNSPECIFIED: Not set.
      BASIC: BASIC tier: standalone instance
      STANDARD_HA: STANDARD_HA tier: highly available primary/replica
        instances
    """
    TIER_UNSPECIFIED = 0
    BASIC = 1
    STANDARD_HA = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Resource labels to represent user provided metadata

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class RedisConfigsValue(_messages.Message):
    r"""Optional. Redis configuration parameters, according to
    http://redis.io/topics/config. Currently, the only supported parameters
    are:   Redis version 3.2 and newer:   *   maxmemory-policy  *   notify-
    keyspace-events   Redis version 4.0 and newer:   *   activedefrag  *
    lfu-decay-time  *   lfu-log-factor  *   maxmemory-gb   Redis version 5.0
    and newer:   *   stream-node-max-bytes  *   stream-node-max-entries

    Messages:
      AdditionalProperty: An additional property for a RedisConfigsValue
        object.

    Fields:
      additionalProperties: Additional properties of type RedisConfigsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a RedisConfigsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  alternativeLocationId = _messages.StringField(1)
  authorizedNetwork = _messages.StringField(2)
  connectMode = _messages.EnumField('ConnectModeValueValuesEnum', 3)
  createTime = _messages.StringField(4)
  currentLocationId = _messages.StringField(5)
  displayName = _messages.StringField(6)
  host = _messages.StringField(7)
  labels = _messages.MessageField('LabelsValue', 8)
  locationId = _messages.StringField(9)
  memorySizeGb = _messages.IntegerField(10, variant=_messages.Variant.INT32)
  name = _messages.StringField(11)
  persistenceIamIdentity = _messages.StringField(12)
  port = _messages.IntegerField(13, variant=_messages.Variant.INT32)
  redisConfigs = _messages.MessageField('RedisConfigsValue', 14)
  redisVersion = _messages.StringField(15)
  reservedIpRange = _messages.StringField(16)
  state = _messages.EnumField('StateValueValuesEnum', 17)
  statusMessage = _messages.StringField(18)
  tier = _messages.EnumField('TierValueValuesEnum', 19)


class ListInstancesResponse(_messages.Message):
  r"""Response for ListInstances.

  Fields:
    instances: A list of Redis instances in the project in the specified
      location, or across all locations.  If the `location_id` in the parent
      field of the request is "-", all regions available to the project are
      queried, and the results aggregated. If in such an aggregated query a
      location is unavailable, a dummy Redis entry is included in the response
      with the `name` field set to a value of the form
      `projects/{project_id}/locations/{location_id}/instances/`- and the
      `status` field set to ERROR and `status_message` field set to "location
      not available for ListInstances".
    nextPageToken: Token to retrieve the next page of results, or empty if
      there are no more results in the list.
    unreachable: Locations that could not be reached.
  """

  instances = _messages.MessageField('Instance', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Output only. The set of available zones in the location.
      The map is keyed by the lowercase ID of each zone, as defined by Compute
      Engine. These keys can be specified in `location_id` or
      `alternative_location_id` fields when creating a Redis instance.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: Resource ID for the region. For example: "us-east1".
    metadata: Output only. The set of available zones in the location. The map
      is keyed by the lowercase ID of each zone, as defined by Compute Engine.
      These keys can be specified in `location_id` or
      `alternative_location_id` fields when creating a Redis instance.
    name: Full resource name for the region. For example: "projects/example-
      project/locations/us-east1".
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Output only. The set of available zones in the location. The map is
    keyed by the lowercase ID of each zone, as defined by Compute Engine.
    These keys can be specified in `location_id` or `alternative_location_id`
    fields when creating a Redis instance.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: {  `createTime`: The time the operation was created.
      `endTime`: The time the operation finished running.  `target`: Server-
      defined resource path for the target of the operation.  `verb`: Name of
      the verb executed by the operation.  `statusDetail`: Human-readable
      status of the operation, if any.  `cancelRequested`: Identifies whether
      the user has requested cancellation of the operation. Operations that
      have successfully been cancelled have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
      `apiVersion`: API version used to start the operation.  }
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: {  `createTime`: The time the operation was created.  `endTime`:
      The time the operation finished running.  `target`: Server-defined
      resource path for the target of the operation.  `verb`: Name of the verb
      executed by the operation.  `statusDetail`: Human-readable status of the
      operation, if any.  `cancelRequested`: Identifies whether the user has
      requested cancellation of the operation. Operations that have
      successfully been cancelled have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
      `apiVersion`: API version used to start the operation.  }
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""{  `createTime`: The time the operation was created.  `endTime`: The
    time the operation finished running.  `target`: Server-defined resource
    path for the target of the operation.  `verb`: Name of the verb executed
    by the operation.  `statusDetail`: Human-readable status of the operation,
    if any.  `cancelRequested`: Identifies whether the user has requested
    cancellation of the operation. Operations that have successfully been
    cancelled have Operation.error value with a google.rpc.Status.code of 1,
    corresponding to `Code.CANCELLED`.  `apiVersion`: API version used to
    start the operation.  }

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OutputConfig(_messages.Message):
  r"""The output content

  Fields:
    gcsDestination: Google Cloud Storage destination for output content.
  """

  gcsDestination = _messages.MessageField('GcsDestination', 1)


class RedisProjectsLocationsGetRequest(_messages.Message):
  r"""A RedisProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsInstancesCreateRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesCreateRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    instanceId: Required. The logical name of the Redis instance in the
      customer project with the following restrictions:  * Must contain only
      lowercase letters, numbers, and hyphens. * Must start with a letter. *
      Must be between 1-40 characters. * Must end with a number or a letter. *
      Must be unique within the customer project / location
    parent: Required. The resource name of the instance location using the
      form:     `projects/{project_id}/locations/{location_id}` where
      `location_id` refers to a GCP region.
  """

  instance = _messages.MessageField('Instance', 1)
  instanceId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class RedisProjectsLocationsInstancesDeleteRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesDeleteRequest object.

  Fields:
    name: Required. Redis instance resource name using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      where `location_id` refers to a GCP region.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsInstancesExportRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesExportRequest object.

  Fields:
    exportInstanceRequest: A ExportInstanceRequest resource to be passed as
      the request body.
    name: Required. Redis instance resource name using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      where `location_id` refers to a GCP region.
  """

  exportInstanceRequest = _messages.MessageField('ExportInstanceRequest', 1)
  name = _messages.StringField(2, required=True)


class RedisProjectsLocationsInstancesFailoverRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesFailoverRequest object.

  Fields:
    failoverInstanceRequest: A FailoverInstanceRequest resource to be passed
      as the request body.
    name: Required. Redis instance resource name using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      where `location_id` refers to a GCP region.
  """

  failoverInstanceRequest = _messages.MessageField('FailoverInstanceRequest', 1)
  name = _messages.StringField(2, required=True)


class RedisProjectsLocationsInstancesGetRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesGetRequest object.

  Fields:
    name: Required. Redis instance resource name using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      where `location_id` refers to a GCP region.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsInstancesImportRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesImportRequest object.

  Fields:
    importInstanceRequest: A ImportInstanceRequest resource to be passed as
      the request body.
    name: Required. Redis instance resource name using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      where `location_id` refers to a GCP region.
  """

  importInstanceRequest = _messages.MessageField('ImportInstanceRequest', 1)
  name = _messages.StringField(2, required=True)


class RedisProjectsLocationsInstancesListRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesListRequest object.

  Fields:
    pageSize: The maximum number of items to return.  If not specified, a
      default value of 1000 will be used by the service. Regardless of the
      page_size value, the response may include a partial list and a caller
      should only rely on response's `next_page_token` to determine if there
      are more instances left to be queried.
    pageToken: The `next_page_token` value returned from a previous
      ListInstances request, if any.
    parent: Required. The resource name of the instance location using the
      form:     `projects/{project_id}/locations/{location_id}` where
      `location_id` refers to a GCP region.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class RedisProjectsLocationsInstancesPatchRequest(_messages.Message):
  r"""A RedisProjectsLocationsInstancesPatchRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    name: Required. Unique name of the resource in this scope including
      project and location using the form:
      `projects/{project_id}/locations/{location_id}/instances/{instance_id}`
      Note: Redis instances are managed and addressed at regional level so
      location_id here refers to a GCP region; however, users may choose which
      specific zone (or collection of zones for cross-zone instances) an
      instance should be provisioned in. Refer to location_id and
      alternative_location_id fields for more details.
    updateMask: Required. Mask of fields to update. At least one path must be
      supplied in this field. The elements of the repeated paths field may
      only include these fields from Instance:   *   `displayName`  *
      `labels`  *   `memorySizeGb`  *   `redisConfig`
  """

  instance = _messages.MessageField('Instance', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class RedisProjectsLocationsListRequest(_messages.Message):
  r"""A RedisProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class RedisProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A RedisProjectsLocationsOperationsCancelRequest object.

  Fields:
    name: The name of the operation resource to be cancelled.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A RedisProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A RedisProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class RedisProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A RedisProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
