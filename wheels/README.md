# How to Add Python Wheels to Blender 4.2+ Extensions

Please refer to https://docs.blender.org/manual/en/latest/advanced/extensions/python_wheels.html for background information.

To add Python wheels to your extension, you need to download the .whl files to this `wheels` folder.
Then declare the required wheel file paths in your extension's blender_manifest.toml configuration file, for example:

```toml
[extension]
name = "Sample Extension"
version = (1, 0, 0)
python_wheels = [
    "wheels/example_package-1.0.0-py3-none-any.whl"
]
```

When you package your extension, the framework will copy these wheel files into the zip file based on the toml configuration.
Therefore, you don't need to store these wheel files in your extension directory to avoid duplication.

Noticed that when testing your addon, the framework will not automatically include these wheels to avoid
overhead. You might see `