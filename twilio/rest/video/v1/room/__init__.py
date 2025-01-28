r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.video.v1.room.participant import ParticipantList
from twilio.rest.video.v1.room.recording_rules import RecordingRulesList
from twilio.rest.video.v1.room.room_recording import RoomRecordingList


class RoomInstance(InstanceResource):

    class RoomStatus(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    class RoomType(object):
        GO = "go"
        PEER_TO_PEER = "peer-to-peer"
        GROUP = "group"
        GROUP_SMALL = "group-small"

    class VideoCodec(object):
        VP8 = "VP8"
        H264 = "H264"

    """
    :ivar sid: The unique string that Twilio created to identify the Room resource.
    :ivar status: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Room resource.
    :ivar enable_turn: Deprecated, now always considered to be true.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
    :ivar status_callback: The URL Twilio calls using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
    :ivar status_callback_method: The HTTP method Twilio uses to call `status_callback`. Can be `POST` or `GET` and defaults to `POST`.
    :ivar end_time: The UTC end time of the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :ivar duration: The duration of the room in seconds.
    :ivar type: 
    :ivar max_participants: The maximum number of concurrent Participants allowed in the room. 
    :ivar max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
    :ivar max_concurrent_published_tracks: The maximum number of published audio, video, and data tracks all participants combined are allowed to publish in the room at the same time. Check [Programmable Video Limits](https://www.twilio.com/docs/video/programmable-video-limits) for more details. If it is set to 0 it means unconstrained.
    :ivar record_participants_on_connect: Whether to start recording when Participants connect.
    :ivar video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.
    :ivar media_region: The region for the Room's media server.  Can be one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#media-servers).
    :ivar audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed.
    :ivar empty_room_timeout: Specifies how long (in minutes) a room will remain active after last participant leaves. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
    :ivar unused_room_timeout: Specifies how long (in minutes) a room will remain active if no one joins. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
    :ivar large_room: Indicates if this is a large room.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["RoomInstance.RoomStatus"] = payload.get("status")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.enable_turn: Optional[bool] = payload.get("enable_turn")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.type: Optional["RoomInstance.RoomType"] = payload.get("type")
        self.max_participants: Optional[int] = deserialize.integer(
            payload.get("max_participants")
        )
        self.max_participant_duration: Optional[int] = deserialize.integer(
            payload.get("max_participant_duration")
        )
        self.max_concurrent_published_tracks: Optional[int] = deserialize.integer(
            payload.get("max_concurrent_published_tracks")
        )
        self.record_participants_on_connect: Optional[bool] = payload.get(
            "record_participants_on_connect"
        )
        self.video_codecs: Optional[List["RoomInstance.VideoCodec"]] = payload.get(
            "video_codecs"
        )
        self.media_region: Optional[str] = payload.get("media_region")
        self.audio_only: Optional[bool] = payload.get("audio_only")
        self.empty_room_timeout: Optional[int] = deserialize.integer(
            payload.get("empty_room_timeout")
        )
        self.unused_room_timeout: Optional[int] = deserialize.integer(
            payload.get("unused_room_timeout")
        )
        self.large_room: Optional[bool] = payload.get("large_room")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[RoomContext] = None

    @property
    def _proxy(self) -> "RoomContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomContext for this RoomInstance
        """
        if self._context is None:
            self._context = RoomContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "RoomInstance":
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RoomInstance":
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return await self._proxy.fetch_async()

    def update(self, status: "RoomInstance.RoomStatus") -> "RoomInstance":
        """
        Update the RoomInstance

        :param status:

        :returns: The updated RoomInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(self, status: "RoomInstance.RoomStatus") -> "RoomInstance":
        """
        Asynchronous coroutine to update the RoomInstance

        :param status:

        :returns: The updated RoomInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    @property
    def recording_rules(self) -> RecordingRulesList:
        """
        Access the recording_rules
        """
        return self._proxy.recording_rules

    @property
    def recordings(self) -> RoomRecordingList:
        """
        Access the recordings
        """
        return self._proxy.recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomInstance {}>".format(context)


class RoomContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RoomContext

        :param version: Version that contains the resource
        :param sid: The SID of the Room resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Rooms/{sid}".format(**self._solution)

        self._participants: Optional[ParticipantList] = None
        self._recording_rules: Optional[RecordingRulesList] = None
        self._recordings: Optional[RoomRecordingList] = None

    def fetch(self) -> RoomInstance:
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RoomInstance:
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, status: "RoomInstance.RoomStatus") -> RoomInstance:
        """
        Update the RoomInstance

        :param status:

        :returns: The updated RoomInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return RoomInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(self, status: "RoomInstance.RoomStatus") -> RoomInstance:
        """
        Asynchronous coroutine to update the RoomInstance

        :param status:

        :returns: The updated RoomInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return RoomInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                self._solution["sid"],
            )
        return self._participants

    @property
    def recording_rules(self) -> RecordingRulesList:
        """
        Access the recording_rules
        """
        if self._recording_rules is None:
            self._recording_rules = RecordingRulesList(
                self._version,
                self._solution["sid"],
            )
        return self._recording_rules

    @property
    def recordings(self) -> RoomRecordingList:
        """
        Access the recordings
        """
        if self._recordings is None:
            self._recordings = RoomRecordingList(
                self._version,
                self._solution["sid"],
            )
        return self._recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomContext {}>".format(context)


class RoomPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> RoomInstance:
        """
        Build an instance of RoomInstance

        :param payload: Payload response from the API
        """
        return RoomInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RoomPage>"


class RoomList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Rooms"

    def create(
        self,
        enable_turn: Union[bool, object] = values.unset,
        type: Union["RoomInstance.RoomType", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_participants: Union[int, object] = values.unset,
        record_participants_on_connect: Union[bool, object] = values.unset,
        video_codecs: Union[List["RoomInstance.VideoCodec"], object] = values.unset,
        media_region: Union[str, object] = values.unset,
        recording_rules: Union[object, object] = values.unset,
        audio_only: Union[bool, object] = values.unset,
        max_participant_duration: Union[int, object] = values.unset,
        empty_room_timeout: Union[int, object] = values.unset,
        unused_room_timeout: Union[int, object] = values.unset,
        large_room: Union[bool, object] = values.unset,
    ) -> RoomInstance:
        """
        Create the RoomInstance

        :param enable_turn: Deprecated, now always considered to be true.
        :param type:
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :param status_callback: The URL Twilio should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :param status_callback_method: The HTTP method Twilio should use to call `status_callback`. Can be `POST` or `GET`.
        :param max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed value is 50.
        :param record_participants_on_connect: Whether to start recording when Participants connect.
        :param video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.
        :param media_region: The region for the Room's media server.  Can be one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers).
        :param recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :param audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed.
        :param max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :param empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
        :param unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
        :param large_room: When set to true, indicated that this is the large room.

        :returns: The created RoomInstance
        """

        data = values.of(
            {
                "EnableTurn": serialize.boolean_to_string(enable_turn),
                "Type": type,
                "UniqueName": unique_name,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxParticipants": max_participants,
                "RecordParticipantsOnConnect": serialize.boolean_to_string(
                    record_participants_on_connect
                ),
                "VideoCodecs": serialize.map(video_codecs, lambda e: e),
                "MediaRegion": media_region,
                "RecordingRules": serialize.object(recording_rules),
                "AudioOnly": serialize.boolean_to_string(audio_only),
                "MaxParticipantDuration": max_participant_duration,
                "EmptyRoomTimeout": empty_room_timeout,
                "UnusedRoomTimeout": unused_room_timeout,
                "LargeRoom": serialize.boolean_to_string(large_room),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return RoomInstance(self._version, payload)

    async def create_async(
        self,
        enable_turn: Union[bool, object] = values.unset,
        type: Union["RoomInstance.RoomType", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_participants: Union[int, object] = values.unset,
        record_participants_on_connect: Union[bool, object] = values.unset,
        video_codecs: Union[List["RoomInstance.VideoCodec"], object] = values.unset,
        media_region: Union[str, object] = values.unset,
        recording_rules: Union[object, object] = values.unset,
        audio_only: Union[bool, object] = values.unset,
        max_participant_duration: Union[int, object] = values.unset,
        empty_room_timeout: Union[int, object] = values.unset,
        unused_room_timeout: Union[int, object] = values.unset,
        large_room: Union[bool, object] = values.unset,
    ) -> RoomInstance:
        """
        Asynchronously create the RoomInstance

        :param enable_turn: Deprecated, now always considered to be true.
        :param type:
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :param status_callback: The URL Twilio should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :param status_callback_method: The HTTP method Twilio should use to call `status_callback`. Can be `POST` or `GET`.
        :param max_participants: The maximum number of concurrent Participants allowed in the room. The maximum allowed value is 50.
        :param record_participants_on_connect: Whether to start recording when Participants connect.
        :param video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.
        :param media_region: The region for the Room's media server.  Can be one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers).
        :param recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :param audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed.
        :param max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :param empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
        :param unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
        :param large_room: When set to true, indicated that this is the large room.

        :returns: The created RoomInstance
        """

        data = values.of(
            {
                "EnableTurn": serialize.boolean_to_string(enable_turn),
                "Type": type,
                "UniqueName": unique_name,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxParticipants": max_participants,
                "RecordParticipantsOnConnect": serialize.boolean_to_string(
                    record_participants_on_connect
                ),
                "VideoCodecs": serialize.map(video_codecs, lambda e: e),
                "MediaRegion": media_region,
                "RecordingRules": serialize.object(recording_rules),
                "AudioOnly": serialize.boolean_to_string(audio_only),
                "MaxParticipantDuration": max_participant_duration,
                "EmptyRoomTimeout": empty_room_timeout,
                "UnusedRoomTimeout": unused_room_timeout,
                "LargeRoom": serialize.boolean_to_string(large_room),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return RoomInstance(self._version, payload)

    def stream(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[RoomInstance]:
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[RoomInstance]:
        """
        Asynchronously streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoomInstance]:
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                status=status,
                unique_name=unique_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoomInstance]:
        """
        Asynchronously lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                status=status,
                unique_name=unique_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoomPage:
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param unique_name: Read only rooms with the this `unique_name`.
        :param date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "Status": status,
                "UniqueName": unique_name,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return RoomPage(self._version, response)

    async def page_async(
        self,
        status: Union["RoomInstance.RoomStatus", object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoomPage:
        """
        Asynchronously retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param unique_name: Read only rooms with the this `unique_name`.
        :param date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "Status": status,
                "UniqueName": unique_name,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return RoomPage(self._version, response)

    def get_page(self, target_url: str) -> RoomPage:
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RoomPage(self._version, response)

    async def get_page_async(self, target_url: str) -> RoomPage:
        """
        Asynchronously retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RoomPage(self._version, response)

    def get(self, sid: str) -> RoomContext:
        """
        Constructs a RoomContext

        :param sid: The SID of the Room resource to update.
        """
        return RoomContext(self._version, sid=sid)

    def __call__(self, sid: str) -> RoomContext:
        """
        Constructs a RoomContext

        :param sid: The SID of the Room resource to update.
        """
        return RoomContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RoomList>"
