from barabrian_file_scanner import BarbarianFileScanner
from large_file_plugin import LargeFilePlugin


def main():
    file_scanner = BarbarianFileScanner()
    large_file_plugin = LargeFilePlugin(100)
    root = "C:\\Users\\User\\code\\python"
    file_scanner.register_plugin(large_file_plugin)
    file_scanner.scan(root)
    file_scanner.report()


if __name__ == "__main__":
    main()
