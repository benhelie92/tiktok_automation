import requests

headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json'
}

payload = {
    "source_info": {
        "source": "FILE_UPLOAD",  # Utilisez "PULL_FROM_URL" pour charger depuis une URL
        "video_size": 123456789,  # Taille de la vidéo en octets
        "chunk_size": 1048576,    # Taille des chunks en octets
        "total_chunk_count": 120  # Nombre total de chunks
    }
}

response = requests.post(
    'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/',
    headers=headers,
    json=payload
)

print(response.json())
