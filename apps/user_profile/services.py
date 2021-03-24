import os


def avatar_upload(instance, file):
    return os.path.join(instance.user.email, 'avatar', file)
