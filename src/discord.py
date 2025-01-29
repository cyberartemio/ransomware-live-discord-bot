import requests
from loguru import logger

class Discord:    
    def __init__(self, webhook):
        self.__webhook = webhook

    def send_message(self, message):
        response = requests.post(self.__webhook, json=message)
        if response.status_code == 204:
            logger.debug("Discord message sent")
            return True
        else:
            logger.error(f"Failed sending message to Discord")
            return False