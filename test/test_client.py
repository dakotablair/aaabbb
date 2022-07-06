import pytest
import subprocess

from aaabbb import serve


def test_serve():
    serve()

def test_serve_cli():
    output = subprocess.run("python aaabbb/__init__.py".split(" "), capture_output=True)
    print(f"output: {output}")
