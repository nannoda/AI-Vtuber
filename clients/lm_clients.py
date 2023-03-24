import requests


class LMClients:
    def __init__(self,
                 port: int,
                 url: str = "localhost"
                 ):
        self.port = port
        self.url = url
        self.generator = None
    def get_response(self, chat_text: str) -> str:
        # get response from the server
        url = f"http://{self.url}:{self.port}/api/post/gen"
        params = {"text": chat_text}
        # use post method
        response = requests.post(url, json=params)
        # get the response
        response = response.json()
        return response


if __name__ == "__main__":
    # initialize the client
    client = LMClients(port=6060)
    # get the response
    response = client.get_response("""
The following is a converation between a streamer and her chat.
Chat: You totally suck at this game!
Streamer:""")
    print(response)
