import yt_dlp
import os

# referer do site da ucs para o download ser permitido
DEFAULT_REFERER = 'https://ucsonline.senior.com.br/'

def download_vimeo_video(embed_url, output_path='.', output_name_template='%(title)s.%(ext)s'):
    # criar pasta destino
    os.makedirs(output_path, exist_ok=True)
    full_output = os.path.join(output_path, output_name_template)
    
    ydl_opts = {
        'format': 'bv*+ba/best',    
        'outtmpl': full_output,
        'merge_output_format': 'mp4',
        'http_headers': {
            'Referer': DEFAULT_REFERER
        },    
    }
    # baixar video
    with yt_dlp.YoutubeDL(ydl_opts) as y:
        try:
            print(f"\ndownloading: {embed_url}\n ↪ 📁 {output_path}")

            y.download([embed_url])
            
            print("\n✅ download complete")
        except Exception as e:
            print(f"\n❌ error ↪ {embed_url}: {e}")

if __name__ == "__main__":
    lista_teste = 'lista_videos.txt'
    main_folder = ''
    sub_folder = ''

    print("\n📩 inicializando script\n")

    with open(lista_teste, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.rstrip('\n').lstrip()
            if not stripped:
                continue
            
            level = 0
            while stripped.startswith('>'):
                level += 1
                stripped = stripped[1:].lstrip()

            if level == 0:
                main_folder = stripped
                print(f"trilha: {main_folder}")
            elif level == 1:
                sub_folder = stripped
                print(f"sub trilha: {sub_folder}")
            elif level == 2:
                parts = stripped.split(' - ', 1)
                if len(parts) == 2:
                    number, url = parts[0].strip(), parts[1].strip()
                    output_path = os.path.join(main_folder, sub_folder)
                    output_name = f"{number} - %(title)s.%(ext)s"
                    print(f"Downloading video {number} to {output_path}")
                    download_vimeo_video(url, output_path, output_name)
                else:
                    print(f"link mal formatado: {stripped}")
            else:
                print(f"level mal formatado {level} line: {stripped}")
