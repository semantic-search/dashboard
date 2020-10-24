import yaml
import globals

image_data = None
audio_data = None

with open("config.yaml") as f:
    config_dict = yaml.safe_load(f)

if "Image" in config_dict:
    image_data = config_dict["Image"]
if "Audio" in config_dict:
    audio_data = config_dict["Audio"]

if 'Image_Captioning' in image_data:
    globals.cap_containers = image_data['Image_Captioning']
if 'Ocr' in image_data:
    globals.ocr_container = image_data['Ocr']
if 'Object_Detection' in image_data:
    globals.object_detect = image_data['Object_Detection']
if 'Scene_Recognition' in image_data:
    globals.scene_recog = image_data['Scene_Recognition']
if 'Image_Recognition' in image_data:
    globals.image_recog = image_data['Image_Recognition']
if 'Image_Search' in image_data:
    globals.image_search = image_data['Image_Search']
if 'Face_Recognition' in image_data:
    globals.face_recog = image_data['Face_Recognition']

if 'Sound_Classification' in audio_data:
    globals.sound_classification = audio_data['Sound_Classification']
if 'Audio_Fingerprinting' in audio_data:
    globals.audio_fingerprinting = audio_data['Audio_Fingerprinting']
if 'Speech_To_Text' in audio_data:
    globals.speech_to_text = audio_data['Speech_To_Text']


def interm_gen(contname):
    interm_dict = {
        "Container": contname,
        "Processing_File": "No File",
        "Status": "Not Started",
        "Remaining Files": None,
        "Remaining Files List": None
    }
    return interm_dict


for container in globals.cap_containers:
    interm_dict = interm_gen(container)
    globals.cap_containers_list.append(interm_dict)
for container in globals.ocr_container:
    interm_dict = interm_gen(container)
    globals.ocr_container_list.append(interm_dict)
for container in globals.object_detect:
    interm_dict = interm_gen(container)
    globals.object_detect_list.append(interm_dict)
for container in globals.object_detect:
    interm_dict = interm_gen(container)
    globals.object_detect_list.append(interm_dict)
for container in globals.scene_recog:
    interm_dict = interm_gen(container)
    globals.scene_recog_list.append(interm_dict)
for container in globals.image_recog:
    interm_dict = interm_gen(container)
    globals.image_recog_list.append(interm_dict)
for container in globals.image_search:
    interm_dict = interm_gen(container)
    globals.image_search_list.append(interm_dict)
for container in globals.face_recog:
    interm_dict = interm_gen(container)
    globals.face_recog_list.append(interm_dict)

for container in globals.sound_classification:
    interm_dict = interm_gen(container)
    globals.sound_classification_list.append(interm_dict)
for container in globals.audio_fingerprinting:
    interm_dict = interm_gen(container)
    globals.audio_fingerprinting_list.append(interm_dict)

for container in globals.speech_to_text:
    interm_dict = interm_gen(container)
    globals.speech_to_text_list.append(interm_dict)

image_dict = {
            'Image_Captioning': globals.cap_containers_list,
            'Ocr': globals.ocr_container_list,
            'Object_Detection': globals.object_detect_list,
            'Scene_Recognition': globals.scene_recog_list,
            'Image_Recognition': globals.image_recog_list,
            'Image_Search': globals.image_search_list,
            'Face_Recognition': globals.face_recog_list
        }
audio_dict = {
    'Sound_Classification': globals.sound_classification_list,
    'Audio_Fingerprinting': globals.audio_fingerprinting_list,
    'Speech_To_Text': globals.speech_to_text_list
}

globals.final_dict = {
    'Image': image_dict,
    'audio': audio_dict
}


def helper(file, container_list, container, remove):
    for is_a_dict in container_list:
        if container == is_a_dict["Container"]:
            print(container)
            print("is a dict")
            print(is_a_dict["Container"])
            if file in globals.container_dict[container]:
                print("in match")
                globals.container_dict[container].remove(file)
                print(globals.container_dict[container])
                if len(globals.container_dict[container]) == 0:
                    print("in remove")
                    print(len(globals.container_dict[container]))
                    is_a_dict["Status"] = "Complete"
                    is_a_dict["Remaining Files"] = int(len(globals.container_dict[container]))
                    is_a_dict["Remaining Files List"] = None
                    if not remove:
                        is_a_dict["Processing_File"] = file

                else:
                    if remove and is_a_dict["Status"] == "Not Started":
                        continue
                    else:
                        print("not remove")
                        print(len(globals.container_dict[container]))
                        is_a_dict["Processing_File"] = file
                        is_a_dict["Status"] = "Ongoing"
                        is_a_dict["Remaining Files"] = int(len(globals.container_dict[container]))
                        is_a_dict["Remaining Files List"] = globals.container_dict[container]


def update_state(parent, group, container, file, remove=False):
    if parent == "Image":
        if group == "Image_Captioning":
            helper(
                remove=remove,
                file=file,
                container_list=globals.cap_containers_list,
                container=container,
            )
        elif group == "Ocr":
            helper(
                remove=remove,
                file=file,
                container_list=globals.ocr_container_list,
                container=container,
            )
        elif group == "Object_Detection":
            helper(
                remove=remove,
                file=file,
                container_list=globals.object_detect_list,
                container=container,
            )
        elif group == "Scene_Recognition":
            helper(
                remove=remove,
                file=file,
                container_list=globals.scene_recog_list,
                container=container,
            )
        elif group == "Image_Recognition":
            helper(
                remove=remove,
                file=file,
                container_list=globals.image_recog_list,
                container=container,
            )
        elif group == "Image_Search":
            helper(
                remove=remove,
                file=file,
                container_list=globals.image_search_list,
                container=container,
            )
        elif group == "Face_Recognition":
            helper(
                remove=remove,
                file=file,
                container_list=globals.face_recog_list,
                container=container,
            )
    elif parent == "Audio":
        if group == "Audio_Fingerprinting":
            helper(
                remove=remove,
                file=file,
                container_list=globals.audio_fingerprinting_list,
                container=container,
            )
        elif group == "Sound_Classification":
            helper(
                remove=remove,
                file=file,
                container_list=globals.sound_classification_list,
                container=container,
            )
        elif group == "Speech_To_Text":
            helper(
                remove=remove,
                file=file,
                container_list=globals.speech_to_text_list,
                container=container,
            )
    image_dict = {
        'Image_Captioning': globals.cap_containers_list,
        'Ocr': globals.ocr_container_list,
        'Object_Detection': globals.object_detect_list,
        'Scene_Recognition': globals.scene_recog_list,
        'Image_Recognition': globals.image_recog_list,
        'Image_Search': globals.image_search_list,
        'Face_Recognition': globals.face_recog_list
    }

    audio_dict = {
        'Sound_Classification': globals.sound_classification_list,
        'Audio_Fingerprinting': globals.audio_fingerprinting_list,
        'Speech_To_Text': globals.speech_to_text_list
    }

    globals.final_dict = {
        'Image': image_dict,
        'audio': audio_dict
    }
    return globals.final_dict
