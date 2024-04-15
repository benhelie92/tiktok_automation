from klap import generate_clip

def main():
    INPUT_VIDEO_URL = "https://www.youtube.com/watch?v=Zr1D3FYcV3Y"  # Exemple d'URL YouTube
    try:
        clip_video_url = generate_clip(INPUT_VIDEO_URL)
        print(f"Generated clip URL: {clip_video_url}")
        # Ici, vous pouvez ajouter la logique pour publier le clip sur TikTok ou toute autre plateforme.
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
