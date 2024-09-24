from plugin import Plugin
import os


class BarbarianFileScanner:
    def __init__(self):
        self.plugins: list[Plugin] = []

    def register_plugin(self, plugin: Plugin):
        self.plugins.append(plugin)

    def apply_plugins(self, file_path: str):
        for plugin in self.plugins:
            plugin.analyze(file_path)

    def report(self):
        for plugin in self.plugins:
            plugin.report()

    def scan(self, path):
        for entry in os.scandir(path):
            if entry.is_dir():
                self.scan(entry.path)
            else:
                self.apply_plugins(entry.path)
