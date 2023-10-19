import json
import pathlib


if __name__ == '__main__':
    files = pathlib.Path(".").glob("split-*/.test_durations")

    combined = {}
    for file in files:
        combined.update(json.loads(file.read_text()))

    pathlib.Path('.test_durations').write_text(json.dumps(combined))
