import pycountry
import hashlib

class Victim:
    def __init__(self, activity, country_code, description, discovered, group_name, name, group_post_url, published_date, screenshot_url, website):
        self.activity = activity
        self.country_code = country_code
        self.description = description
        self.discovered = discovered
        self.group_name = group_name
        self.name = name
        self.group_post_url = group_post_url
        self.published_date = published_date
        self.screenshot_url = screenshot_url
        self.website = website

        if self.country_code != "N/A":
            country_data = pycountry.countries.get(alpha_2=self.country_code)
            self.country = country_data.name if hasattr(country_data, "name") else "N/A"
            self.country_flag = country_data.flag if hasattr(country_data, "flag") else "🏴󠁥󠁳󠁰󠁶󠁿"
        else:
            self.country = "N/A"
            self.country_flag = "🏴󠁥󠁳󠁰󠁶󠁿"
    
    def digest(self):
        plain_text_id = f"{self.name}::{self.group_name}::{self.published_date}"
        hashed_id = hashlib.sha256(plain_text_id.encode())
        return hashed_id.hexdigest()