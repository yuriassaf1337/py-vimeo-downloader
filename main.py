import yt_dlp

# set here the link to the site where the vimeo link is embedded
DEFAULT_REFERER = 'https://ucsonline.senior.com.br/'

def download_vimeo_video(embed_url):
    ydl_opts = {
        'format': 'bv*+ba/best',    
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4', # vimeo splits audio and video, we need to merge them
        'http_headers': {
            'Referer': DEFAULT_REFERER
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as y:
        try:
            print(f"\ndownloading: {embed_url}\n")

            y.download([embed_url])
            
            print("\n✅ download complete")
        except Exception as e:
            print(f"\n❌ error: {e}")

if __name__ == "__main__":
    embed_url = input("Enter Vimeo embed URL (player.vimeo.com): ").strip()

    download_vimeo_video(embed_url)
