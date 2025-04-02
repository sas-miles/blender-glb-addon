from framework import get_init_file_path, test_addon
from main import ACTIVE_ADDON

# Please modify ACTIVE_ADDON parameter before testing

# The name of the addon to be tested, this name is defined in the config.py of the addon as __addon_name__

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('addon', default=ACTIVE_ADDON, nargs='?', help='addon name')
    parser.add_argument('--disable_watch', default=False, action='store_true', help='If true, disable the file watch '
                                                                                    'feature. The addon will not be '
                                                                                    'reloaded automatically when you '
                                                                                    'modify the source code.')
    args = parser.parse_args()
    test_addon(addon_name=args.addon, enable_watch=not args.disable_watch)
