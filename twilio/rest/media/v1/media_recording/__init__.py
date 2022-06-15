# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MediaRecordingList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the MediaRecordingList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingList
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingList
        """
        super(MediaRecordingList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/MediaRecordings'.format(**self._solution)

    def stream(self, order=values.unset, status=values.unset,
               processor_sid=values.unset, source_sid=values.unset, limit=None,
               page_size=None):
        """
        Streams MediaRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param MediaRecordingInstance.Order order: The sort order of the list
        :param MediaRecordingInstance.Status status: Status to filter by
        :param unicode processor_sid: MediaProcessor to filter by
        :param unicode source_sid: Source SID to filter by
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, order=values.unset, status=values.unset,
             processor_sid=values.unset, source_sid=values.unset, limit=None,
             page_size=None):
        """
        Lists MediaRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param MediaRecordingInstance.Order order: The sort order of the list
        :param MediaRecordingInstance.Status status: Status to filter by
        :param unicode processor_sid: MediaProcessor to filter by
        :param unicode source_sid: Source SID to filter by
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_recording.MediaRecordingInstance]
        """
        return list(self.stream(
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, status=values.unset,
             processor_sid=values.unset, source_sid=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param MediaRecordingInstance.Order order: The sort order of the list
        :param MediaRecordingInstance.Status status: Status to filter by
        :param unicode processor_sid: MediaProcessor to filter by
        :param unicode source_sid: Source SID to filter by
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        data = values.of({
            'Order': order,
            'Status': status,
            'ProcessorSid': processor_sid,
            'SourceSid': source_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return MediaRecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MediaRecordingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MediaRecordingContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        return MediaRecordingContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a MediaRecordingContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        return MediaRecordingContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaRecordingList>'


class MediaRecordingPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the MediaRecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingPage
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingPage
        """
        super(MediaRecordingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MediaRecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        return MediaRecordingInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaRecordingPage>'


class MediaRecordingContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the MediaRecordingContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingContext
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        super(MediaRecordingContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/MediaRecordings/{sid}'.format(**self._solution)

    def delete(self):
        """
        Deletes the MediaRecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the MediaRecordingInstance

        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MediaRecordingInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaRecordingContext {}>'.format(context)


class MediaRecordingInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    class Status(object):
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the MediaRecordingInstance

        :returns: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        super(MediaRecordingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'bitrate': deserialize.integer(payload.get('bitrate')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'duration': deserialize.integer(payload.get('duration')),
            'format': payload.get('format'),
            'links': payload.get('links'),
            'processor_sid': payload.get('processor_sid'),
            'resolution': payload.get('resolution'),
            'source_sid': payload.get('source_sid'),
            'sid': payload.get('sid'),
            'media_size': deserialize.integer(payload.get('media_size')),
            'status': payload.get('status'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MediaRecordingContext for this MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingContext
        """
        if self._context is None:
            self._context = MediaRecordingContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def bitrate(self):
        """
        :returns: The bitrate of the media
        :rtype: unicode
        """
        return self._properties['bitrate']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def duration(self):
        """
        :returns: The duration of the MediaRecording
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def format(self):
        """
        :returns: The format of the MediaRecording
        :rtype: MediaRecordingInstance.Format
        """
        return self._properties['format']

    @property
    def links(self):
        """
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def processor_sid(self):
        """
        :returns: The SID of the MediaProcessor
        :rtype: unicode
        """
        return self._properties['processor_sid']

    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels
        :rtype: unicode
        """
        return self._properties['resolution']

    @property
    def source_sid(self):
        """
        :returns: The SID of the resource that generated the original media
        :rtype: unicode
        """
        return self._properties['source_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def media_size(self):
        """
        :returns: The size of the recording media
        :rtype: unicode
        """
        return self._properties['media_size']

    @property
    def status(self):
        """
        :returns: The status of the MediaRecording
        :rtype: MediaRecordingInstance.Status
        """
        return self._properties['status']

    @property
    def status_callback(self):
        """
        :returns: The URL to which Twilio will send MediaRecording event updates
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method Twilio should use to call the `status_callback` URL
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def delete(self):
        """
        Deletes the MediaRecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the MediaRecordingInstance

        :returns: The fetched MediaRecordingInstance
        :rtype: twilio.rest.media.v1.media_recording.MediaRecordingInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaRecordingInstance {}>'.format(context)
