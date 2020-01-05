import kivy
kivy.require('1.0.7')

from kivy.app import App


class InterfaceApp(App):
    # This is required when the app is installed via pip.
    # The value should be the directory this file is in.
    kv_directory = 'blah'


def main(_args=None):
    InterfaceApp().run()

if __name__ == '__main__':
    main()
