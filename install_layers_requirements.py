import glob
import shutil
import subprocess

# Constants
MODULE_NAME = "{TODO:module-name}"
PYTHON_VERSION = "3.11"
PLATFORM = "manylinux2014_aarch64"

try:
    # Cleanup previous installation
    print(f"Removing src/layers/{MODULE_NAME}-layer/python/lib")
    shutil.rmtree(f"src/layers/{MODULE_NAME}-layer/python/lib")

except FileNotFoundError:
    # Previous installation already cleaned up which fulfills the requirement, so ignore this exception
    pass

# Download and install Python dependency packages
print(
    subprocess.run(
        f"pip install -r src/layers/{MODULE_NAME}-layer/python/requirements.txt"
        f" -t src/layers/{MODULE_NAME}-layer/python/lib/python{PYTHON_VERSION}/site-packages"
        f" --platform {PLATFORM}"
        " --implementation cp"
        f" --python-version {PYTHON_VERSION}"
        " --only-binary=:all:",
        shell=True,
        stdout=subprocess.PIPE,
    ).stdout.decode()
)

# Remove unused *.dist-info directories
for path in glob.iglob(
    f"src/layers/{MODULE_NAME}-layer/python/lib/python{PYTHON_VERSION}/site-packages/**/*.dist-info",
    recursive=True,
):
    print(f"Removing {path}")
    shutil.rmtree(path)
