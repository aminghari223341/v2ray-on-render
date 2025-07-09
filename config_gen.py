import json
import uuid

def generate_config(uuid_str, path="/v2ray"):
    config = {
        "inbounds": [
            {
                "port": 10000,
                "protocol": "vmess",
                "settings": {
                    "clients": [{"id": uuid_str}]
                },
                "streamSettings": {
                    "network": "ws",
                    "wsSettings": {"path": path}
                }
            }
        ],
        "outbounds": [
            {"protocol": "freedom", "settings": {}}
        ]
    }
    return config

if __name__ == "__main__":
    my_uuid = str(uuid.uuid4())
    print(f"🟢 Your UUID: {my_uuid}")
    conf = generate_config(my_uuid)
    with open("config.json", "w") as f:
        json.dump(conf, f, indent=4)