import json
from scrapli import Scrapli

DC_DEVICE_PLATFORM_MAP = {
    "leaf1": "arista_eos",
    "leaf2": "arista_eos",
    "leaf3": "cisco_nxos",
    "spine1": "arista_eos",
}

def main():
    with open("payload.json") as f:
        stuff = json.load(f)

    device = stuff["data"]["device"]["name"]
    intf = stuff["data"]["name"]
    new_descr = stuff["data"]["description"]

    print(f"device {device} interface {intf} description now {new_descr}")

    with Scrapli(host=device,auth_username="admin",auth_password="admin",auth_strict_key=False,platform=DC_DEVICE_PLATFORM_MAP[device]) as  conn:
        current_descr = conn.send_command(command=f"show run interface {intf} | inc descr")
        if current_descr.result.strip() == new_descr:
            print("currnt descr matches, nothing to do")
            return
        conn.send_configs(configs=[f"interface {intf}", f"description {new_descr}"])
        print("intf updated")


if __name__ == "__main__":
    main()
