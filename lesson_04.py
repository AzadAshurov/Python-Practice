import logging
import time
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logging.info("This is an info message")
logging.warning("This is a warning message")    
logging.error("This is an error message")
logging.critical("This is a critical message")




def start_service():
    logger.info("Service has started successfully")


def load_model():
    logger.info("Model has loaded successfully ")
    logger.warning("Model response is slow")
    logger.error("Model failed")


def predict():
    logger.info("Prediction completed successfully")


start_service()
load_model()
predict()


