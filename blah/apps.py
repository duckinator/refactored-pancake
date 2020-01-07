from subprocess import check_call as run

PROFILE_ARGS = ['-P', 'secondary']


def firefox():
    run(['firefox', *PROFILE_ARGS])


def firefox_private_window():
    run(['firefox', *PROFILE_ARGS, '--private-window'])


def youtube():
    run(['firefox', *PROFILE_ARGS, '--kiosk', 'https://youtube.com'])


def plex():
    run(['firefox', *PROFILE_ARGS, '--kiosk', 'https://plex.tv'])
