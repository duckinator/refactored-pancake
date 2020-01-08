PROFILE_ARGS = ['-P', 'secondary']


def firefox():
    return ['firefox', *PROFILE_ARGS]


def firefox_private_window():
    return ['firefox', *PROFILE_ARGS, '--private-window']


def youtube():
    return ['firefox', *PROFILE_ARGS, '--kiosk', 'https://youtube.com']


def plex():
    return ['firefox', *PROFILE_ARGS, '--kiosk', 'https://plex.tv']
