import requests

def test_service_health():
    # 这里默认测试运行环境能访问服务，可以用 port-forward 或 clusterIP + proxy
    # 本地跑时自行配置访问地址
    resp = requests.get("http://localhost:8000")  # 需要提前做端口转发或用NodePort
    assert resp.status_code == 200
