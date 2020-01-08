from kivy.core.window import Window

Window.borderless = True
Window.left = 0
Window.top = 0
Window.size = (1920, 1080)

import kivy
kivy.require('1.0.7')

from kivy.app import App

import toml

from pathlib import Path
import re
import subprocess

# Handles exactly one child process.
# If you start one before the other one has exited, it gets replaced.
class ProcessHandler:
    def __init__(self):
        self.child = None

    def start(self, args):
        # If there's an old child process, kill it.
        if self.child and not self.child.poll():
            print("[ProcessHandler] Termininating old process.")
            self.child.kill()

        self.child = subprocess.Popen(args)
        return self.child

    def stop(self):
        if not self.child:
            return
        if self.child.poll() is not None:
            return
        self.child.kill()


class InterfaceApp(App):
    # This is required when the app is installed via pip.
    # The value should be the directory this file is in.
    kv_directory = Path(__file__).resolve().parent
    #'blah'

    def __init__(self):
        # Manages a single process for the various apps.
        self.app = ProcessHandler()

        src_dir = Path(__file__).resolve().parent
        apps_file = src_dir / 'apps.toml'

        #if Path('../apps.custom.toml').exists():
        #    apps_file = Path('../apps.custom.toml')
        self.apps = toml.loads(apps_file.read_text())
        print(self.apps)

    def on_start(self):
        for child in self.root.children[0].children:
            child.bind(on_press=self.start)

    def start(self, button):
        name = button.text

        command = APPS.get(name, None)
        if command is None:
            print('NO SUCH FUNCTION: {}'.format(name))
            return

        self.app.start(command)

def main(_args=None):
    InterfaceApp().run()


if __name__ == '__main__':
    main()
