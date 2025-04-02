# BlenderAddonPackageTool - A framework for developing multiple blender addons in a single workspace
# Copyright (C) 2024 Xinyu Zhu

import os
from configparser import ConfigParser

from common.class_loader.module_installer import default_blender_addon_path, normalize_blender_path_by_system

# The name of current active addon to be created, tested or released
ACTIVE_ADDON = "glb_tools"

# The path of the blender executable. Blender2.93 is the minimum version required
BLENDER_EXE_PATH = "C:/software/general/Blender/blender-3.6.0-windows-x64/blender.exe"

# Linux example
# BLENDER_EXE_PATH = "/usr/local/blender/blender-3.6.0-linux-x64/blender"

# MacOS example - notice "/Contents/MacOS/Blender" will be appended automatically if you didn't write it explicitly
# BLENDER_EXE_PATH = "/Applications/Blender/blender-3.6.0-macOS/Blender.app"

# Are you developing an extension(for Blender4.2) instead of legacy addon?
# https://docs.blender.org/manual/en/latest/advanced/extensions/addons.html
# The framework will convert absolute import to relative import when packaging the extension.
# Make sure to update __addon_name__ in config.py if you are migrating from legacy addon to extension.
IS_EXTENSION = False

# You can override the default path by setting the path manually
# BLENDER_ADDON_PATH = "C:/software/general/Blender/Blender3.5/3.5/scripts/addons/"
BLENDER_ADDON_PATH = None
if os.path.exists(BLENDER_EXE_PATH):
    BLENDER_ADDON_PATH = default_blender_addon_path(BLENDER_EXE_PATH)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Read configuration from config.ini if it exists
CONFIG_FILEPATH = os.path.join(PROJECT_ROOT, 'config.ini')

# The default release dir. Must not within the current workspace
DEFAULT_RELEASE_DIR = os.path.join(PROJECT_ROOT, "../addon_release/")

# The default test release dir. Must not within the current workspace
TEST_RELEASE_DIR = os.path.join(PROJECT_ROOT, "../addon_test/")

if os.path.isfile(CONFIG_FILEPATH):
    configParser = ConfigParser()
    configParser.read(CONFIG_FILEPATH, encoding='utf-8')

    if configParser.has_option('blender', 'exe_path'):
        BLENDER_EXE_PATH = configParser.get('blender', 'exe_path')
        # The path of the blender addon folder
        BLENDER_ADDON_PATH = default_blender_addon_path(BLENDER_EXE_PATH)

    if configParser.has_option('blender', 'addon_path') and configParser.get('blender', 'addon_path'):
        BLENDER_ADDON_PATH = configParser.get('blender', 'addon_path')

    if configParser.has_option('default', 'addon') and configParser.get('default', 'addon'):
        ACTIVE_ADDON = configParser.get('default', 'addon')

    if configParser.has_option('default', 'is_extension') and configParser.get('default', 'is_extension'):
        IS_EXTENSION = configParser.getboolean('default', 'is_extension')

    if configParser.has_option('default', 'release_dir') and configParser.get('default', 'release_dir'):
        DEFAULT_RELEASE_DIR = configParser.get('default', 'release_dir')

    if configParser.has_option('default', 'test_release_dir') and configParser.get('default', 'test_release_dir'):
        TEST_RELEASE_DIR = configParser.get('default', 'test_release_dir')

BLENDER_EXE_PATH = normalize_blender_path_by_system(BLENDER_EXE_PATH)

# If you want to override the BLENDER_ADDON_PATH (the path to install addon during testing), uncomment the following line and set the path manually.
# BLENDER_ADDON_PATH = ""

# Could not find the blender addon path, raise error. Please set BLENDER_ADDON_PATH manually.
if os.path.exists(BLENDER_EXE_PATH) and (not BLENDER_ADDON_PATH or not os.path.exists(BLENDER_ADDON_PATH)):
    raise ValueError("Blender addon path not found: " + BLENDER_ADDON_PATH, "Please set the correct path in config.ini")
