def user_media_path(obj, filename):
    """ set media path dynamically based
        on the user id.
    """
    return f"users/{obj.id}/avatar/{filename}"

def artwork_media_path(obj, filename):
    """set artwork media path"""
    return f"artwork/{obj.artwork_id}/image/{filename}"


def generate_handle(handle, count = 0):
    return f"{handle}{(lambda x: x+1 if x else '')(count)}"

def modify_image_input(images, is_featured):
    return list([dict([ ('image', img), ('is_featured',is_featured ) ]) for img in images or [] ])