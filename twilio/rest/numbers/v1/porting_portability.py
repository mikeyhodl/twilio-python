r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PortingPortabilityInstance(InstanceResource):

    class NumberType(object):
        LOCAL = "LOCAL"
        UNKNOWN = "UNKNOWN"
        MOBILE = "MOBILE"
        TOLL_FREE = "TOLL-FREE"

    """
    :ivar phone_number: The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212).
    :ivar account_sid: Account Sid that the phone number belongs to in Twilio. This is only returned for phone numbers that already exist in Twilio’s inventory and belong to your account or sub account.
    :ivar portable: Boolean flag indicates if the phone number can be ported into Twilio through the Porting API or not.
    :ivar pin_and_account_number_required: Indicates if the port in process will require a personal identification number (PIN) and an account number for this phone number. If this is true you will be required to submit both a PIN and account number from the losing carrier for this number when opening a port in request. These fields will be required in order to complete the port in process to Twilio.
    :ivar not_portable_reason: Reason why the phone number cannot be ported into Twilio, `null` otherwise.
    :ivar not_portable_reason_code: The Portability Reason Code for the phone number if it cannot be ported into Twilio, `null` otherwise.
    :ivar number_type: 
    :ivar country: Country the phone number belongs to.
    :ivar url: This is the url of the request that you're trying to reach out to locate the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        phone_number: Optional[str] = None,
    ):
        super().__init__(version)

        self.phone_number: Optional[str] = payload.get("phone_number")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.portable: Optional[bool] = payload.get("portable")
        self.pin_and_account_number_required: Optional[bool] = payload.get(
            "pin_and_account_number_required"
        )
        self.not_portable_reason: Optional[str] = payload.get("not_portable_reason")
        self.not_portable_reason_code: Optional[int] = deserialize.integer(
            payload.get("not_portable_reason_code")
        )
        self.number_type: Optional["PortingPortabilityInstance.NumberType"] = (
            payload.get("number_type")
        )
        self.country: Optional[str] = payload.get("country")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "phone_number": phone_number or self.phone_number,
        }
        self._context: Optional[PortingPortabilityContext] = None

    @property
    def _proxy(self) -> "PortingPortabilityContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PortingPortabilityContext for this PortingPortabilityInstance
        """
        if self._context is None:
            self._context = PortingPortabilityContext(
                self._version,
                phone_number=self._solution["phone_number"],
            )
        return self._context

    def fetch(
        self,
        target_account_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
    ) -> "PortingPortabilityInstance":
        """
        Fetch the PortingPortabilityInstance

        :param target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub account already has the number in its inventory or a different sub account. If this is not provided, the authenticated account will be assumed to be the target account.
        :param address_sid: Address Sid of customer to which the number will be ported.

        :returns: The fetched PortingPortabilityInstance
        """
        return self._proxy.fetch(
            target_account_sid=target_account_sid,
            address_sid=address_sid,
        )

    async def fetch_async(
        self,
        target_account_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
    ) -> "PortingPortabilityInstance":
        """
        Asynchronous coroutine to fetch the PortingPortabilityInstance

        :param target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub account already has the number in its inventory or a different sub account. If this is not provided, the authenticated account will be assumed to be the target account.
        :param address_sid: Address Sid of customer to which the number will be ported.

        :returns: The fetched PortingPortabilityInstance
        """
        return await self._proxy.fetch_async(
            target_account_sid=target_account_sid,
            address_sid=address_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingPortabilityInstance {}>".format(context)


class PortingPortabilityContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PortingPortabilityContext

        :param version: Version that contains the resource
        :param phone_number: Phone number to check portability in e164 format.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "phone_number": phone_number,
        }
        self._uri = "/Porting/Portability/PhoneNumber/{phone_number}".format(
            **self._solution
        )

    def fetch(
        self,
        target_account_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
    ) -> PortingPortabilityInstance:
        """
        Fetch the PortingPortabilityInstance

        :param target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub account already has the number in its inventory or a different sub account. If this is not provided, the authenticated account will be assumed to be the target account.
        :param address_sid: Address Sid of customer to which the number will be ported.

        :returns: The fetched PortingPortabilityInstance
        """

        data = values.of(
            {
                "TargetAccountSid": target_account_sid,
                "AddressSid": address_sid,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return PortingPortabilityInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    async def fetch_async(
        self,
        target_account_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
    ) -> PortingPortabilityInstance:
        """
        Asynchronous coroutine to fetch the PortingPortabilityInstance

        :param target_account_sid: Account Sid to which the number will be ported. This can be used to determine if a sub account already has the number in its inventory or a different sub account. If this is not provided, the authenticated account will be assumed to be the target account.
        :param address_sid: Address Sid of customer to which the number will be ported.

        :returns: The fetched PortingPortabilityInstance
        """

        data = values.of(
            {
                "TargetAccountSid": target_account_sid,
                "AddressSid": address_sid,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return PortingPortabilityInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingPortabilityContext {}>".format(context)


class PortingPortabilityList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PortingPortabilityList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, phone_number: str) -> PortingPortabilityContext:
        """
        Constructs a PortingPortabilityContext

        :param phone_number: Phone number to check portability in e164 format.
        """
        return PortingPortabilityContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number: str) -> PortingPortabilityContext:
        """
        Constructs a PortingPortabilityContext

        :param phone_number: Phone number to check portability in e164 format.
        """
        return PortingPortabilityContext(self._version, phone_number=phone_number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.PortingPortabilityList>"
