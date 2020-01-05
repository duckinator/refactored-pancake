import kivy
kivy.require('1.0.7')

from kivy.app import App


class InterfaceApp(App):
    # This is required when the app is installed via pip.
    # The value should be the directory this file is in.
    kv_directory = 'blah'

    def on_start(self):
        print('owo')
        for child in self.root_window.children[0].children:
            print(child, child.height, child.width)
        #row_default_height = 

def main(_args=None):
    InterfaceApp().run()

if __name__ == '__main__':
    main()
