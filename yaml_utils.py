import yaml

image_data = None
audio_data = None

cap_containers = list()
ocr_container = list()
object_detect = list()
scene_recog = list()
image_recog = list()
image_search = list()
face_recog= list()

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

with open("config.yaml") as f:
    config_dict = yaml.safe_load(f)

if "Image" in config_dict:
    image_data = config_dict["Image"]
if "Audio" in config_dict:
    audio_data = config_dict["Audio"]

if 'Image_Captioning' in image_data:
    cap_containers = image_data['Image_Captioning']
if 'Ocr' in image_data:
    ocr_container = image_data['Ocr']
if 'Object_Detection' in image_data:
    object_detect = image_data['Object_Detection']
if 'Scene_Recognition' in image_data:
    scene_recog = image_data['Scene_Recognition']
if 'Image_Recognition' in image_data:
    image_recog = image_data['Image_Recognition']
if 'Image_Search' in image_data:
    image_search = image_data['Image_Search']
if 'Face_Recognition' in image_data:
    face_recog = image_data['Face_Recognition']

if 'Sound_Classification' in audio_data:
    sound_classification = audio_data['Sound_Classification']
if 'Audio_Fingerprinting' in audio_data:
    audio_fingerprinting = audio_data['Audio_Fingerprinting']
if 'Speech_To_Text' in audio_data:
    speech_to_text = audio_data['Speech_To_Text']


def interm_gen(contname):
    interm_dict = {
        "Container": contname,
        "Processing_File": "No File",
        "Status": "Not Started"
    }
    return interm_dict


for container in cap_containers:
    interm_dict = interm_gen(container)
    cap_containers_list.append(interm_dict)
for container in ocr_container:
    interm_dict = interm_gen(container)
    ocr_container_list.append(interm_dict)
for container in object_detect:
    interm_dict = interm_gen(container)
    object_detect_list.append(interm_dict)
for container in object_detect:
    interm_dict = interm_gen(container)
    object_detect_list.append(interm_dict)
for container in scene_recog:
    interm_dict = interm_gen(container)
    scene_recog_list.append(interm_dict)
for container in image_recog:
    interm_dict = interm_gen(container)
    image_recog_list.append(interm_dict)
for container in image_search:
    interm_dict = interm_gen(container)
    image_search_list.append(interm_dict)
for container in face_recog:
    interm_dict = interm_gen(container)
    face_recog_list.append(interm_dict)

for container in sound_classification:
    interm_dict = interm_gen(container)
    sound_classification_list.append(interm_dict)
for container in audio_fingerprinting:
    interm_dict = interm_gen(container)
    audio_fingerprinting_list.append(interm_dict)

for container in speech_to_text:
    interm_dict = interm_gen(container)
    speech_to_text_list.append(interm_dict)


def helper(file, last_file, container_list, container):
    print(container)
    for is_a_dict in container_list:
        print(is_a_dict)
        if container == is_a_dict["Container"]:
            print(is_a_dict)
            if file == last_file:
                is_a_dict["Processing_File"] = file
                is_a_dict["Status"] = "Complete"
            else:
                is_a_dict["Processing_File"] = file


def update_state(parent, group, container, file, last_image_file, last_audio_file):
    if parent == "Image":
        if group == "Image_Captioning":
            print("here")
            helper(
                file=file,
                last_file=last_image_file,
                container_list=cap_containers_list,
                container=container
            )
        elif group == "Ocr":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=ocr_container_list,
                container=container
            )
        elif group == "Object_Detection":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=object_detect_list,
                container=container
            )
        elif group == "Scene_Recognition":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=scene_recog_list,
                container=container
            )
        elif group == "Image_Recognition":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=image_recog_list,
                container=container
            )
        elif group == "Image_Search":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=image_search_list,
                container=container
            )
        elif group == "Face_Recognition":
            helper(
                file=file,
                last_file=last_image_file,
                container_list=face_recog_list,
                container=container
            )
    elif parent == "Audio":
        if group == "Audio_Fingerprinting":
            helper(
                file=file,
                last_file=last_audio_file,
                container_list=audio_fingerprinting_list,
                container=container
            )
        elif group == "Sound_Classification":
            helper(
                file=file,
                last_file=last_audio_file,
                container_list=sound_classification_list,
                container=container
            )
        elif group == "Speech_To_Text":
            helper(
                file=file,
                last_file=last_audio_file,
                container_list=speech_to_text_list,
                container=container
            )
    image_dict = {
        'Image_Captioning': cap_containers_list,
        'Ocr': ocr_container_list,
        'Object_Detection': object_detect_list,
        'Scene_Recognition': scene_recog_list,
        'Image_Recognition': image_recog_list,
        'Image_Search': image_search_list,
        'Face_Recognition': face_recog_list
    }
    audio_dict = {
        'Sound_Classification': sound_classification_list,
        'Audio_Fingerprinting': audio_fingerprinting_list,
        'Speech_To_Text': speech_to_text_list
    }
    global final_dict

    final_dict = {
        'Image': image_dict,
        'audio': audio_dict
    }
    return final_dict


def get_dict():
    image_dict = {
        'Image_Captioning': cap_containers_list,
        'Ocr': ocr_container_list,
        'Object_Detection': object_detect_list,
        'Scene_Recognition': scene_recog_list,
        'Image_Recognition': image_recog_list,
        'Image_Search': image_search_list,
        'Face_Recognition': face_recog_list
    }
    audio_dict = {
        'Sound_Classification': sound_classification_list,
        'Audio_Fingerprinting': audio_fingerprinting_list,
        'Speech_To_Text': speech_to_text_list
    }
    global final_dict

    final_dict = {
        'Image': image_dict,
        'audio': audio_dict
    }
    return final_dict
