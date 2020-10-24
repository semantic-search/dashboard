cap_containers = list()
ocr_container = list()
object_detect = list()
scene_recog = list()
image_recog = list()
image_search = list()
face_recog = list()

cap_containers_list = list()
ocr_container_list = list()
object_detect_list = list()
scene_recog_list = list()
image_recog_list = list()
image_search_list = list()
face_recog_list = list()

sound_classification = list()
audio_fingerprinting = list()
speech_to_text = list()

sound_classification_list = list()
audio_fingerprinting_list = list()
speech_to_text_list = list()

final_dict = dict()

container_dict = {

    "DENSE_CAP": list(),
    "IMAGE_CAPTIONING": list(),
    "SELF_CRITICAL_PYTORCH": list(),
    "NEURAL_TALK_2": list(),
    "IM2TXT": list(),

    "KERAS_TESSER_OCR": list(),
    "EASY_OCR": list(),

    "PP_YOLO": list(),
    "YOLO_V4": list(),
    "YOLO_V4_VOC": list(),
    "MASK_RCNN_SENET": list(),
    "OPEN_IMAGES_MODEL": list(),
    "COCO_MODEL": list(),
    "RETINA_NET_MODEL": list(),

    "PLACES_365_TORCH": list(),
    "PLACES_365_KERAS_HYBRID": list(),
    "PLACES_365_KERAS_BASE": list(),
    "IBM_MAX_SCENE_CLASSIFIER": list(),

    "IMAGE_NET_KERAS_MODELS": list(),
    "TENCENT_ML_IMAGES_MODEL": list(),

    "VGG16_MODEL": list(),

    "DLIB": list(),

    "MAX_AUDIO_CLASSIFIER": list(),

    "DEJAVU": list(),
    "JASPER": list(),
    "QUARTZNET": list(),
    "DEEP_SPEECH": list(),

}

image_containers = ["DENSE_CAP",
                    "IMAGE_CAPTIONING",
                    "SELF_CRITICAL_PYTORCH",
                    "NEURAL_TALK_2",
                    "IM2TXT",
                    "KERAS_TESSER_OCR",
                    "EASY_OCR",
                    "PP_YOLO",
                    "YOLO_V4",
                    "YOLO_V4_VOC",
                    "MASK_RCNN_SENET",
                    "OPEN_IMAGES_MODEL",
                    "COCO_MODEL",
                    "RETINA_NET_MODEL",
                    "PLACES_365_TORCH",
                    "PLACES_365_KERAS_HYBRID",
                    "PLACES_365_KERAS_BASE",
                    "IBM_MAX_SCENE_CLASSIFIER",
                    "IMAGE_NET_KERAS_MODELS",
                    "TENCENT_ML_IMAGES_MODEL",
                    "VGG16_MODEL",
                    "DLIB"
                    ]

audio_container = ["MAX_AUDIO_CLASSIFIER",
                   "DEJAVU",
                   "JASPER",
                   "QUARTZNET",
                   "DEEP_SPEECH"
                   ]

image_groups_all = ["Image_Captioning",
                    "Ocr",
                    "Object_Detection",
                    "Scene_Recognition",
                    "Image_Recognition",
                    "Image_Search",
                    "Face_Recognition",
                    ]

audio_groups_all = ["Audio_Fingerprinting", "Sound_Classification", "Speech_To_Text"]
