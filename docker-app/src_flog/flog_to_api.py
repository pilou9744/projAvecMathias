import subprocess
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os

time_between_logs = os.environ["TIME_BETWEEN_LOGS"]

while True:

    time.sleep(time_between_logs)


    log = subprocess.check_output(
        ["flog", "-n", "1", "-f", "rfc3164"],
        text=True
    ).strip()

    log = log.split("]:", 1)[1].strip()

    try :
        request = Request(
            f"http://127.0.0.1:8000/logs?{urlencode({'log': log})}",
            data=b"",
            method="POST",
        )
        urlopen(request).close()
    except :
        print("Y a un problème")
