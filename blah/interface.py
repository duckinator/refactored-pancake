from kivy.core.window import Window

Window.borderless = True
Window.left = 0
Window.top = 0
Window.size = (1920, 1080)

import kivy
kivy.require('1.0.7')

from kivy.app import App

import re
import subprocess

from . import apps


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
    kv_directory = 'blah'

    # Manages a single process for the various apps.
    app = ProcessHandler()

    def on_start(self):
        for child in self.root.children[0].children:
            child.bind(on_press=self.start)

    def start(self, button):
        # Lowercase everything, replace spaces with underscore.
        name = button.text.lower().replace(' ', '_')
        # Replace anything that's not alphanumeric with underscores.'
        name = re.sub(r'[^a-z0-9]', '_', name)
        # Replace repeated underscores with one underscore.
        name = re.sub(r'_+', '_', name)
        # Remove leading and trailing underscores.
        name = re.sub(r'^_|_$', '', name)
        error_callback = lambda: self.error(name)
        app_fn = getattr(apps, name, None)
        if app_fn is None:
            print('NO SUCH FUNCTION: {}'.format(name))
            return

        command = app_fn()
        self.app.start(command)


def main(_args=None):
    InterfaceApp().run()


if __name__ == '__main__':
    main()
