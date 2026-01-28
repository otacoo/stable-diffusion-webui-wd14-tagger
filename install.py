"""Install requirements for WD14-tagger."""
import os

from launch import is_installed, run_pip  # pylint: disable=import-error

NAME = "WD14-tagger"
# Key package: if missing, assume first install and run full requirements
_PROBE_PACKAGE = "deepdanbooru"

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
if not is_installed(_PROBE_PACKAGE):
    run_pip(
        f'install -q -r "{req_file}"',
        f"{NAME} requirements",
    )
