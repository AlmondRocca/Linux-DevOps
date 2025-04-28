import signal
import subprocess
import time
import pytest
import shutil
from pathlib import Path

@pytest.fixture
def setup_tmp_file():
    """Ensure /tmp directory exists and copy ./bin/currentCount to /tmp/currentCount.out."""
    tmp_dir = Path("/tmp")
    tmp_file = tmp_dir / "currentCount.out"
    source_file = Path("./bin/currentCount")

    # ensure /tmp directory exists
    tmp_dir.mkdir(parents=True, exist_ok=True)

    # copy file if it exists
    if source_file.exists():
        shutil.copy(source_file, tmp_file)
    else:
        pytest.fail(f"Source file {source_file} does not exist.")

    return tmp_file

def test_script(setup_tmp_file):
    """Test if the script correctly handles SIGTERM and writes to the file."""
    temp_file = setup_tmp_file

    # start the script as a subprocess
    process = subprocess.Popen(["python3", "./bin/currentCount"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # let it run for a few seconds
    time.sleep(2)
    
    process.send_signal(signal.SIGTERM)
    process.wait()
    
    time.sleep(1)
    
    # ensure the output file was created
    assert temp_file.exists(), "Output file was not created."