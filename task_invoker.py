from task import consume
import globals
from redis import StrictRedis
from rq import Queue
import globals


q = Queue(connection=StrictRedis(
    host=globals.REDIS_HOSTNAME,
    port=globals.REDIS_PORT,
    password=globals.REDIS_PASSWORD,
    ssl=False
))


def invoke():
    for topic in globals.image_captioning_containers:
        q.enqueue(consume, topic)
    for topic in globals.ocr_containers:
        q.enqueue(consume, topic)
    for topic in globals.object_detection_containers:
        q.enqueue(consume, topic)
    for topic in globals.scene_recognition_containers:
        q.enqueue(consume, topic)
    for topic in globals.image_recognition_containers:
        q.enqueue(consume, topic)
    for topic in globals.image_search_containers:
        q.enqueue(consume, topic)
    for topic in globals.face_recognition_containers:
        q.enqueue(consume, topic)
    for topic in globals.sound_classification_containers:
        q.enqueue(consume, topic)
    for topic in globals.audio_fingerprinting_containers:
        q.enqueue(consume, topic)
    for topic in globals.speech_to_text_containers:
        q.enqueue(consume, topic)
    for topic in globals.entity_recognition_containers:
        q.enqueue(consume, topic)
