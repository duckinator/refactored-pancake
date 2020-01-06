from subprocess import check_call as run


def firefox():
    run(['firefox'])


def firefox_private_window():
    run(['firefox', '--private-window'])


def youtube():
    run(['firefox', '--kiosk', 'https://youtube.com'])


def plex():
    run(['firefox', '--kiosk', 'https://plex.tv'])
