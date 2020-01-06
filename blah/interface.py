import re

import kivy
kivy.require('1.0.7')

from kivy.app import App

from . import apps

class InterfaceApp(App):
    # This is required when the app is installed via pip.
    # The value should be the directory this file is in.
    kv_directory = 'blah'

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
        fn = getattr(apps, name, error_callback)
        fn()

    @staticmethod
    def error(name):
        print('NO SUCH FUNCTION: {}'.format(name))


def main(_args=None):
    InterfaceApp().run()


if __name__ == '__main__':
    main()
