def user_media_path(obj, filename):
    """ set media path dynamically based
        on the user id.
    """
    return f"users/{obj.id}/avatar/{filename}"

def artwork_media_path(obj, filename):
    """set artwork media path"""
    return f"artwork/{obj.artwork_id}/image/{filename}"
