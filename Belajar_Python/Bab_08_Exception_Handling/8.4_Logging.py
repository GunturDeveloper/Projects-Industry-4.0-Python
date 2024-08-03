# Menggunakan logging
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Ini adalah pesan debug")
logging.info("Ini adalah pesan info")
logging.warning("Ini adalah pesan warning")
logging.error("Ini adalah pesan error")
logging.critical("Ini adalah pesan critical")
