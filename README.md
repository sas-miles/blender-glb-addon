# Blender Addon Development Framework and Packaging Tool

This project has been updated to MIT license as of December 2, 2024.

This is a lightweight Blender addon development framework and packaging tool. Main features include:

1. Create template addons with a single command for rapid development
2. Support developing multiple addons in one project, allowing you to reuse functionality between different addons. It can automatically detect dependencies between function modules and package related modules into the zip file without including unnecessary modules.

### Demo 1: Auto-update while developing
![](docs/demo1.gif)

### Demo 2: Built-in I18n solution
![](docs/demo2.gif)

### Demo 3: Load Blender Component classes (Operation, Panel, etc.) automatically
![](docs/demo3.gif)

The project has been updated to use MIT open source license since 2024.12.02.

This project provides a lightweight, easy-to-use framework for developing and packaging Blender addons. The main
features include:

1. A single command to create a template add-on, facilitating quick development.
1. Support developing multiple addons in one project, which allows you to reuse functions across
   different addons, and helps you package only necessary modules into the zip file.
1. Allows you to run and test your add-on in Blender with a single command. Support hot swap
   for code updates. You can see the updates in Blender immediately after saving the code.
1. A single command to package the add-on into an installable addon package, making it easier for users to install. The
   packaging tool automatically detects and includes dependencies needed for the add-on within your project. (Not
   including 3rd party libraries)
1. Provide utility functions for basic development, like an auto-load utility for automatic class loading and an
   internationalization (i18n)
   tool, to help new developers creating high-quality addons.
1. Support extension development in Blender 4.2 and later versions. You can choose to package your addon
   as a legacy addon or as an extension by setting the IS_EXTENSION configuration

You can check out an overview about this framework on YouTube:

- https://www.youtube.com/watch?v=eRSXO_WkY0s
- https://youtu.be/udPBrXJZT1g

The following external library will be installed automatically when you run the framework code, you can also install
them
manually:

- https://github.com/nutti/fake-bpy-module
- https://github.com/gorakhargosh/watchdog

## Basic Framework

- [main.py](main.py): Configures the Blender path, add-on installation path, default add-on, package ignore files, and
  add-on release path, among other settings.
- [test.py](test.py): A testing tool to run and test add-ons.
- [create.py](create.py): A tool to create add-ons, allowing you to quickly create an add-on based on the `sample_addon`
  template.
- [release.py](release.py): A packaging tool that packages add-ons into an installable package.
- [framework.py](framework.py): The core business logic of the framework, which automates the development process.
- [addons](addons): A directory to store add-ons, with each add-on in its own sub-directory. Use `create.py` to quickly
  create a new add-on.
- [common](common): A directory to store shared utilities.

## Framework Development Guidelines

Blender Version >= 2.93
Platform Supported: Windows, MacOs, Linux

Each add-on, while adhering to the basic structure of a Blender add-on, should include a `config.py` file to configure
the add-on's package name, ensuring it doesn't conflict with other add-ons.

This project depends on the `addons` folder; do not rename this folder.

When packaging an add-on, the framework will generate a __init__.py file in the add-on directory. By copying bl_info,
and importing the register and unregister method from your target addon's __init__.py. Usually this won't cause any
issue, but if you notice anything that might be related to this, please let us know.

### Notice for extension developers

To meet the standard
at https://docs.blender.org/manual/en/latest/advanced/extensions/addons.html#user-preferences-and-package
You need to follow the following instruction when using preferences in your extension addon. These instructions are also
applicable to the legacy addon, but not enforced.

Since addons developed by this framework usually have submodules. To access preferences, you must use the
__addon_name__ defined in the config.py file as the bl_idname of the preferences.

Define:

```python
class ExampleAddonPreferences(AddonPreferences):
    bl_idname = __addon_name__
```

Access

```python
from ..config import __addon_name__

addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
# use addon_prefs
addon_prefs.some_property
```

## Usage

1. Clone this repository.
1. Open this project in your IDE. Optional: Configure the IDE to use the same python interpreter as Blender.
1. Note: For PyCharm users, change the value idea.max.intellisense.filesize in idea.properties file ( Help | Edit Custom
   Properties.) to more than 2600 because some modules have the issue of being too big for intelliSense to work. You
   might also need to associate the __init__.pyi file as the python File Types
   in ![setting](https://i.ibb.co/QcYZytw/script.png) to get the auto code completion working.
1. Configure the name of the addon you want to create (ACTIVE_ADDON) in [main.py](main.py).
1. Run create.py to create a new addon in your IDE. The first time you run this, it will download dependencies,
   including
   watchdog and fake-bpy-module.
1. Develop your addon in the newly created addon directory.
1. Run test.py to test your addon in Blender.
1. Run release.py to package your addon into an installable package. The packaged addon path will appears in the
   terminal when packaged successfully.

## Features Provided by the Framework

1. You don't need to worry about register and unregister classes in Blender add-ons. The framework automatically loads
   and unloads classes in your add-ons. You just need to define your classes in the addon's folder. Note that the
   classes that are automatically loaded need to be placed in a directory with an `__init__.py` file to be recognized
   and loaded by the framework's auto load mechanism.
1. You can use internationalization in your add-ons. Just add translations in the standard format to the `dictionary.py`
   file in the `i18n` folder of your add-on.
1. You can define RNA properties declaratively. Just follow the examples in the `__init__.py` file to add your RNA
   properties. The framework will automatically register and unregister your RNA properties.
1. You can choose to package your addon as a legacy addon or as an extension in Blender 4.2 and later versions. Just set
   the `IS_EXTENSION` configuration to switch between the two. The framework will convert absolute import to relative
   import for you when releasing.
   Notice only `from XXX.XXX import XXX` is supported, `import XXX.XX` is not supported for converting to relative
   import.
1. You can use the `ExpandableUi` class in `common/types/framework.py` to easily extend Blender's native UI components,
   such as menus, panels, pie menus, and headers. Just inherit from this class and implement the `draw` method. You can
   specify the ID of the native UI component you want to extend using `target_id` and specify whether to append or
   prepend using `expand_mode`.
1. You can use the `reg_order` decorator in `common/types/framework.py` to specify the order of registration for your
   classes. This is useful when you need to ensure that certain classes are registered before others. For example the
   initial order of Panels will be in the order they are registered.

## Add Optional Configuration File

To avoid having to modify the configuration items in `main.py` every time you update the framework, you can create a
`config.ini` file in the root directory of your project to store your configuration information. This file will override
the configuration information in `main.py`.

Here is an example of a `config.ini` file:

```ini
[blender]
; path to the blender executable
exe_path = C:/software/general/Blender/Blender3.5/blender.exe
; exe_path = C:/software/general/Blender/Blender3.6/blender.exe

; path to the addon directory, testing addon will be temporarily installed here
; usually you don't need to configure this since it can be derived from the exe_path
addon_path = C:/software/general/Blender/Blender3.5/scripts/addons/

[default]
; name of the addon to be created, tested and released
addon = sample_addon
; Whether the addon is an extension, if True, the addon will be packaged when released.
is_extension = False
; the path to store released addon zip files. Do not release to your source code directory
release_dir = C:/path/to/release/dir
; the path to store addon files used for testing, during testing, the framework will first release the addon to here and copy it to Blender's addon directory. Do not release to your source code directory
test_release_dir = C:/path/to/test/release/dir
```

## Contributions

1. Framework Updates: If you are using this framework in your project and need to migrate to a newer version, you will
   need to manually replace the framework files to get the new features. You may fork this project and use
   `git fetch upstream` to update.
   We are looking for more user-friendly migration
   experience. In general, we aim to keep the framework lightweight and avoid making structural changes. Most future
   updates are expected to just adding new features rather than making major changes to the framework structure. So
   unless you personally made changes to the framework code locally, you will only need to replace the old files with
   the new ones in future updates.
1. Breakpoint Debugging: The framework currently does not support breakpoint debugging within the IDE. Implementing this
   feature requires some modifications to the framework code, which may increase the complexity of using the framework.
   We are looking for a lightweight solution to enable this feature. However, in general, breakpoint debugging is not
   necessary for developing add-ons. Breakpoint debugging is helpful for complex add-ons features, but logging is
   sufficient in most of the cases. For this framework, breakpoint debugging would be a nice-to-have feature, but not a
   must-have.
