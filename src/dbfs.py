from loguru import logger
import os

class DbFS:
    DB_FOLDER = "data" # Name of the folder where all the data is stored
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        logger.info(current_file_path)
        src_directory = os.path.dirname(current_file_path)
        logger.info(src_directory)
        root_directory = os.path.dirname(src_directory)
        logger.info(root_directory)
        self.folder = os.path.join(root_directory, self.DB_FOLDER)
        logger.info(self.folder)

    def already_notified_victims(self):
        logger.debug("Loading list of already notified victims from filesystem")
        try:
            with open(os.path.join(self.folder, "notified_victims.txt"), "r") as nvf:
                notified_victims_digests = nvf.readlines()
                logger.info(f"Loaded digests of already notified victims from FS::{len(notified_victims_digests)} digests")
                return [ digest.strip() for digest in notified_victims_digests ] 
        except Exception as e:
            logger.error(f"Failed loading notified victims::{e}")
            return None
    
    def add_notified_victim(self, victim_digest):
        try:
            with open(os.path.join(self.folder, "notified_victims.txt"), "a") as nvf:
                nvf.write(f"{victim_digest}\n")
                return True
        except Exception as e:
            logger.error(f"Failed saving notified victim::{e} - digest::{victim_digest}")
            return False