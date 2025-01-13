from pydantic import BaseModel

from picturas_shared_ms.core.messages.request_message import RequestMessage


class WatermarkParameters(BaseModel):
    inputImageURI: str
    outputImageURI: str


WatermarkRequestMessage = RequestMessage[WatermarkParameters]
