import subprocess
import time
import requests

def test_e2e_service_access():
    # 端口转发
    proc = subprocess.Popen(["kubectl", "port-forward", "svc/myapp-service", "8000:80"])
    time.sleep(3)
    try:
        resp = requests.get("http://localhost:8000")
        assert resp.status_code == 200
    finally:
        proc.terminate()
