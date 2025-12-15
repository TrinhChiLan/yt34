import shutil

use_bundled = True

if shutil.which("ffmpeg") is None:
    print("Look for bundled ffmpeg binaries.")
else:
    print("User has already installed ffmpeg.")
    use_bundled = False