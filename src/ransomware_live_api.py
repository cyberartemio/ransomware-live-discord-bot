import requests
from models.victim import Victim
from loguru import logger

class RansomwareLiveApi:
    API_URL = "https://api.ransomware.live"
    def __get__(self, url):
        try:
            response = requests.get(f"{self.API_URL}{url}", headers={ "accept": "application/json" })
            response.raise_for_status()
            data = response.json()
            return data
        except Exception as e:
            logger.error(f'Error while fetching APIs data from {url}::{e}')
            return None

    def recent_victims(self):
        logger.info("Requesting latest 100 victims from ransomware.live")
        recent_victims = []
        data = self.__get__("/recentvictims")
        if data:
            for victim in data:
                activity = victim["activity"] if "activity" in victim and victim["activity"] != "Not Found" and victim["activity"] != "" else "N/A"
                country = victim["country"] if "country" in victim and victim["country"] != "" else "N/A"
                description = victim["description"] if "description" in victim else "N/A"
                discovered = victim["discovered"] if "discovered" in victim else None # TODO: parse string as datetime obj
                group = victim["group_name"] if "group_name" in victim else "N/A"
                post_title = victim["post_title"] if "post_title" in victim else "N/A"
                post_url = victim["post_url"] if "post_url" in victim else "N/A"
                published = victim["published"] if "published" in victim else None # TODO: parse string as datetime obj
                screenshot = victim["screenshot"] if "screenshot" in victim else None
                website = victim["website"] if "website" in victim and victim["website"] != "" else "N/A"
                recent_victims.append(Victim(activity=activity, country_code=country, description=description, discovered=discovered, group_name=group, name=post_title, group_post_url=post_url, published_date=published, screenshot_url=screenshot, website=website))
        return recent_victims