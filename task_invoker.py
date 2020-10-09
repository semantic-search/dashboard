from task import consume
import globals


def invoke():
    for topic in globals.image_captioning_containers:
        consume.delay(topic)
    for topic in globals.ocr_containers:
        consume.delay(topic)
    for topic in globals.object_detection_containers:
        consume.delay(topic)
    for topic in globals.scene_recognition_containers:
        consume.delay(topic)
    for topic in globals.image_recognition_containers:
        consume.delay(topic)
    for topic in globals.image_search_containers:
        consume.delay(topic)
    for topic in globals.face_recognition_containers:
        consume.delay(topic)
    for topic in globals.sound_classification_containers:
        consume.delay(topic)
    for topic in globals.audio_fingerprinting_containers:
        consume.delay(topic)
    for topic in globals.speech_to_text_containers:
        consume.delay(topic)
    for topic in globals.entity_recognition_containers:
        consume.delay(topic)
