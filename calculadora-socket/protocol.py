from message import Message
import json
class Protocol:
    def marshalMessage(message: Message) -> bytes:
        return json.dumps(message.dict()).encode()
    def unmarshalMessage(message: bytes) -> Message:
        obj = json.loads(message.decode())
        return Message(obj['type'], obj['datatype'], obj['data'], obj['datasize'])
    
if __name__ == '__main__':
    data: str = 'BOM DIA'
    request: Message = Message('request', 'str', data, len(data))

    marshal = Protocol.marshalMessage(request)
    print(Protocol.unmarshalMessage(marshal))