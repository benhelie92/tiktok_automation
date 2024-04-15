import requests
import time

API_URL = "https://api.klap.app/v1"
API_KEY = "<your-api-key>"
INPUT_VIDEO_URL = "https://www.youtube.com/watch?v=Zr1D3FYcV3Y"

def post_request(url, body=None):
    if body is None:
        body = {}
    response = requests.post(f"{API_URL}{url}", json=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    })
    return response.json() if response.ok else response.raise_for_status()

def get_request(url):
    response = requests.get(f"{API_URL}{url}", headers={
        "Authorization": f"Bearer {API_KEY}"
    })
    return response.json()

def poll_status(url, check_key, check_value):
    while True:
        res_json = get_request(url)
        print(f"[{time.strftime('%X')}] Polling {url} while {check_key} === {check_value}...")
        if res_json[check_key] != check_value:
            break
        time.sleep(30)  # Wait for 30 seconds before polling again
    return res_json

def generate_clip(input_video_url):
    video = post_request("/videos", {
        "source_video_url": input_video_url,
        "language": "en",
        "max_duration": 60,
    })
    print(f"Video created: {video['id']}. Processing...")
    video = poll_status(f"/videos/{video['id']}", "status", "processing")
    print(f"Video processing done: {video['id']}.")

    if video["status"] == "error":
        raise Exception("Video processing failed.")

    clips = get_request(f"/videos/{video['id']}/clips")
    print(f"Got {len(clips)} clips.")
    for clip in clips:
        print(f'"{clip["name"]}" Virality Score: {clip["virality_score"]}')

    best_clip = clips[0]
    print(f"Exporting best clip: {best_clip['id']}...")

    export_res = post_request(f"/videos/{video['id']}/clips/{best_clip['id']}/exports", {
        "options": {"face_recognition": True, "crop": True, "subtitles": True},
        "preset_id": "aedb9874-db95-410f-ac0c-ee5ec29c67f7",
    })

    print(f"Export started: {export_res['id']}.")
    export_res = poll_status(f"/videos/{video['id']}/clips/{best_clip['id']}/exports/{export_res['id']}", "status", "processing")
    print(f"Export done: {export_res['id']}.")
    return export_res["src_url"]

