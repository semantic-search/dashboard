import os
from dotenv import load_dotenv

load_dotenv()


KAFKA_HOSTNAME = os.getenv("KAFKA_HOSTNAME")
KAFKA_PORT = os.getenv("KAFKA_PORT")
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME")
KAFKA_PASSWORD = os.getenv("KAFKA_PASSWORD")
KAFKA_CLIENT_ID = os.getenv("KAFKA_CLIENT_ID")
REDIS_HOSTNAME = os.getenv("REDIS_HOSTNAME")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = '0'
CLIENT_ID = os.getenv("CLIENT_ID")


image_captioning_containers = None
ocr_containers = None
object_detection_containers = None
scene_recognition_containers = None
image_recognition_containers = None
image_search_containers = None
face_recognition_containers = None
sound_classification_containers = None
audio_fingerprinting_containers = None
speech_to_text_containers = None
entity_recognition_containers = None
search_containers = None
