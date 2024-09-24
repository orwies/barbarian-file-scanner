from plugin import Plugin
import os


class LargeFilePlugin(Plugin):
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.findings = {}

    def analyze(self, file_path):
        file_size = os.stat(file_path).st_size
        if file_size > self.size_limit:
            self.findings[file_path] = file_size

    def report(self):
        for file_path, file_size in self.findings.items():
            print(f"Large file detected: {file_path} (Size: {file_size} bytes)")
