import subprocess
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen


while True:
    log = subprocess.check_output(["flog", "-n", "1", "-f", "rfc3164"], text=True).strip()
    request = Request(
        f"http://127.0.0.1:8000/logs?{urlencode({'log': log})}",
        data=b"",
        method="POST",
    )
    urlopen(request).close()
    time.sleep(2)
