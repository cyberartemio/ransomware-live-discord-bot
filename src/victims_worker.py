from loguru import logger
from ransomware_live_api import RansomwareLiveApi
from dbfs import DbFS
from messages import Messages
from discord import Discord
import os
from dotenv import load_dotenv
import sys

def check_env_vars():
    logger.debug("Checking env variables")
    load_dotenv()
    if os.getenv("DISCORD_WEBHOOK") is None:
        logger.critical("Missing env variable::DISCORD_WEBHOOK")
        sys.exit(1)

def main():
    check_env_vars()
    api = RansomwareLiveApi()
    discord = Discord(os.getenv("DISCORD_WEBHOOK"))
    db = DbFS()
    messages = Messages()
    notified_victims_digests = db.already_notified_victims()

    recent_victims = api.recent_victims()
    for victim in recent_victims:
        victim_digest = victim.digest()
        if victim_digest not in notified_victims_digests:
            logger.info(f"Notifying new victim - victim::{victim.name}")
            if discord.send_message(messages.victim_discord_message(victim)):
                logger.info(f"Adding digest to dbfs file - digest::{victim_digest}")
                if not db.add_notified_victim(victim_digest):
                    logger.error(f"Failed saving victim digest - digest::{victim_digest}")
            else:
                logger.error(f"Failed notifying victim to Discord - victim::{victim.name}")

if __name__ == "__main__":
    main()