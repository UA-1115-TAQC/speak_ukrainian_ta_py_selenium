from os import path


class ConfigProperties:

    @staticmethod
    def get_image_path(image_name):
        img_folder_path = "tests/images/"
        try:
            current_absolute = path.abspath(__file__)
            index = current_absolute.rfind('speak_ukrainian_ta_py_selenium')
            trimmed_path = current_absolute[:index + len('speak_ukrainian_ta_py_selenium')]
            img_path = path.normpath(path.join(trimmed_path, img_folder_path, image_name))
            return img_path
        except Exception as err:
            print(err)
