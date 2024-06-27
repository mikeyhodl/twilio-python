r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.content.v1.content.approval_create import ApprovalCreateList
from twilio.rest.content.v1.content.approval_fetch import ApprovalFetchList


class ContentInstance(InstanceResource):

    class AuthenticationActionType(object):
        COPY_CODE = "COPY_CODE"

    class CallToActionActionType(object):
        URL = "URL"
        PHONE_NUMBER = "PHONE_NUMBER"

    class CardActionType(object):
        URL = "URL"
        PHONE_NUMBER = "PHONE_NUMBER"
        QUICK_REPLY = "QUICK_REPLY"

    class QuickReplyActionType(object):
        QUICK_REPLY = "QUICK_REPLY"

    """
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar sid: The unique string that that we created to identify the Content resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
    :ivar friendly_name: A string name used to describe the Content resource. Not visible to the end recipient.
    :ivar language: Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.
    :ivar variables: Defines the default placeholder values for variables included in the Content resource. e.g. {\"1\": \"Customer_Name\"}.
    :ivar types: The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.
    :ivar url: The URL of the resource, relative to `https://content.twilio.com`.
    :ivar links: A list of links related to the Content resource, such as approval_fetch and approval_create
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.language: Optional[str] = payload.get("language")
        self.variables: Optional[Dict[str, object]] = payload.get("variables")
        self.types: Optional[Dict[str, object]] = payload.get("types")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ContentContext] = None

    @property
    def _proxy(self) -> "ContentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ContentContext for this ContentInstance
        """
        if self._context is None:
            self._context = ContentContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ContentInstance":
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ContentInstance":
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        """
        return await self._proxy.fetch_async()

    @property
    def approval_create(self) -> ApprovalCreateList:
        """
        Access the approval_create
        """
        return self._proxy.approval_create

    @property
    def approval_fetch(self) -> ApprovalFetchList:
        """
        Access the approval_fetch
        """
        return self._proxy.approval_fetch

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentInstance {}>".format(context)


class ContentContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ContentContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Content/{sid}".format(**self._solution)

        self._approval_create: Optional[ApprovalCreateList] = None
        self._approval_fetch: Optional[ApprovalFetchList] = None

    def delete(self) -> bool:
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ContentInstance:
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ContentInstance:
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def approval_create(self) -> ApprovalCreateList:
        """
        Access the approval_create
        """
        if self._approval_create is None:
            self._approval_create = ApprovalCreateList(
                self._version,
                self._solution["sid"],
            )
        return self._approval_create

    @property
    def approval_fetch(self) -> ApprovalFetchList:
        """
        Access the approval_fetch
        """
        if self._approval_fetch is None:
            self._approval_fetch = ApprovalFetchList(
                self._version,
                self._solution["sid"],
            )
        return self._approval_fetch

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentContext {}>".format(context)


class ContentPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ContentInstance:
        """
        Build an instance of ContentInstance

        :param payload: Payload response from the API
        """
        return ContentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentPage>"


class ContentList(ListResource):

    class AuthenticationAction(object):
        """
        :ivar type:
        :ivar copy_code_text:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.type: Optional["ContentInstance.AuthenticationActionType"] = (
                payload.get("type")
            )
            self.copy_code_text: Optional[str] = payload.get("copy_code_text")

        def to_dict(self):
            return {
                "type": self.type,
                "copy_code_text": self.copy_code_text,
            }

    class CallToActionAction(object):
        """
        :ivar type:
        :ivar title:
        :ivar url:
        :ivar phone:
        :ivar id:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.type: Optional["ContentInstance.CallToActionActionType"] = payload.get(
                "type"
            )
            self.title: Optional[str] = payload.get("title")
            self.url: Optional[str] = payload.get("url")
            self.phone: Optional[str] = payload.get("phone")
            self.id: Optional[str] = payload.get("id")

        def to_dict(self):
            return {
                "type": self.type,
                "title": self.title,
                "url": self.url,
                "phone": self.phone,
                "id": self.id,
            }

    class CardAction(object):
        """
        :ivar type:
        :ivar title:
        :ivar url:
        :ivar phone:
        :ivar id:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.type: Optional["ContentInstance.CardActionType"] = payload.get("type")
            self.title: Optional[str] = payload.get("title")
            self.url: Optional[str] = payload.get("url")
            self.phone: Optional[str] = payload.get("phone")
            self.id: Optional[str] = payload.get("id")

        def to_dict(self):
            return {
                "type": self.type,
                "title": self.title,
                "url": self.url,
                "phone": self.phone,
                "id": self.id,
            }

    class CatalogItem(object):
        """
        :ivar id:
        :ivar section_title:
        :ivar name:
        :ivar media_url:
        :ivar price:
        :ivar description:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.id: Optional[str] = payload.get("id")
            self.section_title: Optional[str] = payload.get("section_title")
            self.name: Optional[str] = payload.get("name")
            self.media_url: Optional[str] = payload.get("media_url")
            self.price: Optional[float] = payload.get("price")
            self.description: Optional[str] = payload.get("description")

        def to_dict(self):
            return {
                "id": self.id,
                "section_title": self.section_title,
                "name": self.name,
                "media_url": self.media_url,
                "price": self.price,
                "description": self.description,
            }

    class ContentCreateRequest(object):
        """
        :ivar friendly_name: User defined name of the content
        :ivar variables: Key value pairs of variable name to value
        :ivar language: Language code for the content
        :ivar types:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.friendly_name: Optional[str] = payload.get("friendly_name")
            self.variables: Optional[dict[str, str]] = payload.get("variables")
            self.language: Optional[str] = payload.get("language")
            self.types: Optional[ContentList.Types] = payload.get("types")

        def to_dict(self):
            return {
                "friendly_name": self.friendly_name,
                "variables": self.variables,
                "language": self.language,
                "types": self.types.to_dict(),
            }

    class ListItem(object):
        """
        :ivar id:
        :ivar item:
        :ivar description:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.id: Optional[str] = payload.get("id")
            self.item: Optional[str] = payload.get("item")
            self.description: Optional[str] = payload.get("description")

        def to_dict(self):
            return {
                "id": self.id,
                "item": self.item,
                "description": self.description,
            }

    class QuickReplyAction(object):
        """
        :ivar type:
        :ivar title:
        :ivar id:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.type: Optional["ContentInstance.QuickReplyActionType"] = payload.get(
                "type"
            )
            self.title: Optional[str] = payload.get("title")
            self.id: Optional[str] = payload.get("id")

        def to_dict(self):
            return {
                "type": self.type,
                "title": self.title,
                "id": self.id,
            }

    class TwilioCallToAction(object):
        """
        :ivar body:
        :ivar actions:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")
            self.actions: Optional[List[ContentList.CallToActionAction]] = payload.get(
                "actions"
            )

        def to_dict(self):
            return {
                "body": self.body,
                "actions": [actions.to_dict() for actions in self.actions],
            }

    class TwilioCard(object):
        """
        :ivar title:
        :ivar subtitle:
        :ivar media:
        :ivar actions:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.title: Optional[str] = payload.get("title")
            self.subtitle: Optional[str] = payload.get("subtitle")
            self.media: Optional[List[str]] = payload.get("media")
            self.actions: Optional[List[ContentList.CardAction]] = payload.get(
                "actions"
            )

        def to_dict(self):
            return {
                "title": self.title,
                "subtitle": self.subtitle,
                "media": self.media,
                "actions": [actions.to_dict() for actions in self.actions],
            }

    class TwilioCatalog(object):
        """
        :ivar title:
        :ivar body:
        :ivar subtitle:
        :ivar id:
        :ivar items:
        :ivar dynamic_items:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.title: Optional[str] = payload.get("title")
            self.body: Optional[str] = payload.get("body")
            self.subtitle: Optional[str] = payload.get("subtitle")
            self.id: Optional[str] = payload.get("id")
            self.items: Optional[List[ContentList.CatalogItem]] = payload.get("items")
            self.dynamic_items: Optional[str] = payload.get("dynamic_items")

        def to_dict(self):
            return {
                "title": self.title,
                "body": self.body,
                "subtitle": self.subtitle,
                "id": self.id,
                "items": [items.to_dict() for items in self.items],
                "dynamic_items": self.dynamic_items,
            }

    class TwilioListPicker(object):
        """
        :ivar body:
        :ivar button:
        :ivar items:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")
            self.button: Optional[str] = payload.get("button")
            self.items: Optional[List[ContentList.ListItem]] = payload.get("items")

        def to_dict(self):
            return {
                "body": self.body,
                "button": self.button,
                "items": [items.to_dict() for items in self.items],
            }

    class TwilioLocation(object):
        """
        :ivar latitude:
        :ivar longitude:
        :ivar label:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.latitude: Optional[float] = payload.get("latitude")
            self.longitude: Optional[float] = payload.get("longitude")
            self.label: Optional[str] = payload.get("label")

        def to_dict(self):
            return {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "label": self.label,
            }

    class TwilioMedia(object):
        """
        :ivar body:
        :ivar media:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")
            self.media: Optional[List[str]] = payload.get("media")

        def to_dict(self):
            return {
                "body": self.body,
                "media": self.media,
            }

    class TwilioQuickReply(object):
        """
        :ivar body:
        :ivar actions:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")
            self.actions: Optional[List[ContentList.QuickReplyAction]] = payload.get(
                "actions"
            )

        def to_dict(self):
            return {
                "body": self.body,
                "actions": [actions.to_dict() for actions in self.actions],
            }

    class TwilioText(object):
        """
        :ivar body:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")

        def to_dict(self):
            return {
                "body": self.body,
            }

    class Types(object):
        """
        :ivar twilio_text:
        :ivar twilio_media:
        :ivar twilio_location:
        :ivar twilio_list_picker:
        :ivar twilio_call_to_action:
        :ivar twilio_quick_reply:
        :ivar twilio_card:
        :ivar twilio_catalog:
        :ivar whatsapp_card:
        :ivar whatsapp_authentication:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.twilio_text: Optional[ContentList.TwilioText] = payload.get(
                "twilio_text"
            )
            self.twilio_media: Optional[ContentList.TwilioMedia] = payload.get(
                "twilio_media"
            )
            self.twilio_location: Optional[ContentList.TwilioLocation] = payload.get(
                "twilio_location"
            )
            self.twilio_list_picker: Optional[ContentList.TwilioListPicker] = (
                payload.get("twilio_list_picker")
            )
            self.twilio_call_to_action: Optional[ContentList.TwilioCallToAction] = (
                payload.get("twilio_call_to_action")
            )
            self.twilio_quick_reply: Optional[ContentList.TwilioQuickReply] = (
                payload.get("twilio_quick_reply")
            )
            self.twilio_card: Optional[ContentList.TwilioCard] = payload.get(
                "twilio_card"
            )
            self.twilio_catalog: Optional[ContentList.TwilioCatalog] = payload.get(
                "twilio_catalog"
            )
            self.whatsapp_card: Optional[ContentList.WhatsappCard] = payload.get(
                "whatsapp_card"
            )
            self.whatsapp_authentication: Optional[
                ContentList.WhatsappAuthentication
            ] = payload.get("whatsapp_authentication")

        def to_dict(self):
            return {
                "twilio_text": self.twilio_text.to_dict(),
                "twilio_media": self.twilio_media.to_dict(),
                "twilio_location": self.twilio_location.to_dict(),
                "twilio_list_picker": self.twilio_list_picker.to_dict(),
                "twilio_call_to_action": self.twilio_call_to_action.to_dict(),
                "twilio_quick_reply": self.twilio_quick_reply.to_dict(),
                "twilio_card": self.twilio_card.to_dict(),
                "twilio_catalog": self.twilio_catalog.to_dict(),
                "whatsapp_card": self.whatsapp_card.to_dict(),
                "whatsapp_authentication": self.whatsapp_authentication.to_dict(),
            }

    class WhatsappAuthentication(object):
        """
        :ivar add_security_recommendation:
        :ivar code_expiration_minutes:
        :ivar actions:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.add_security_recommendation: Optional[bool] = payload.get(
                "add_security_recommendation"
            )
            self.code_expiration_minutes: Optional[float] = payload.get(
                "code_expiration_minutes"
            )
            self.actions: Optional[List[ContentList.AuthenticationAction]] = (
                payload.get("actions")
            )

        def to_dict(self):
            return {
                "add_security_recommendation": self.add_security_recommendation,
                "code_expiration_minutes": self.code_expiration_minutes,
                "actions": [actions.to_dict() for actions in self.actions],
            }

    class WhatsappCard(object):
        """
        :ivar body:
        :ivar footer:
        :ivar media:
        :ivar header_text:
        :ivar actions:
        """

        def __init__(self, payload: Dict[str, Any], sid: Optional[str] = None):

            self.body: Optional[str] = payload.get("body")
            self.footer: Optional[str] = payload.get("footer")
            self.media: Optional[List[str]] = payload.get("media")
            self.header_text: Optional[str] = payload.get("header_text")
            self.actions: Optional[List[ContentList.CardAction]] = payload.get(
                "actions"
            )

        def to_dict(self):
            return {
                "body": self.body,
                "footer": self.footer,
                "media": self.media,
                "header_text": self.header_text,
                "actions": [actions.to_dict() for actions in self.actions],
            }

    def __init__(self, version: Version):
        """
        Initialize the ContentList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Content"

    def create(self, content_create_request: ContentCreateRequest) -> ContentInstance:
        """
        Create the ContentInstance

        :param content_create_request:

        :returns: The created ContentInstance
        """
        data = content_create_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ContentInstance(self._version, payload)

    async def create_async(
        self, content_create_request: ContentCreateRequest
    ) -> ContentInstance:
        """
        Asynchronously create the ContentInstance

        :param content_create_request:

        :returns: The created ContentInstance
        """
        data = content_create_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ContentInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ContentInstance]:
        """
        Streams ContentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ContentInstance]:
        """
        Asynchronously streams ContentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ContentInstance]:
        """
        Lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ContentInstance]:
        """
        Asynchronously lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ContentPage:
        """
        Retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ContentPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ContentPage:
        """
        Asynchronously retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ContentPage(self._version, response)

    def get_page(self, target_url: str) -> ContentPage:
        """
        Retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ContentPage(self._version, response)

    async def get_page_async(self, target_url: str) -> ContentPage:
        """
        Asynchronously retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ContentPage(self._version, response)

    def get(self, sid: str) -> ContentContext:
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        return ContentContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ContentContext:
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
        """
        return ContentContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentList>"
