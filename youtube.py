from pytube import YouTube,Playlist

def downloadVideo(link, resulation):
    print("İndiriliyor...")
    youtubeObj = YouTube(link)
    if(not resulation):
        youtubeObj = youtubeObj.streams.get_by_resolution(resulation)
    else:
        youtubeObj = youtubeObj.streams.get_highest_resolution()
    try:
        youtubeObj.download()
    except:
        print("Hata")
    print("İndirildi")

def downloadPlaylist(playlistLink,resulation):
    playlist = Playlist(playlistLink)
    print("İndiriliyor...")
    try:
        for vid in playlist.videos:
            if(not resulation):
                vid = vid.streams.get_by_resolution(resulation)
                vid.download()
            else:
                vid.streams.get_highest_resolution().download()
                
    except:
        print("Hata!")
    print("İndirildi")


while 1:
    opt = input("""
    - Video İndirmek İçin 1'e Basın
    - Playlist İndirmek İçin 2'ye Basın
    - Çıkmak İçin 'e' ye Basın
        
    Seçiminiz: """)
    if(opt == "1"):
        link = input("Videonun linki: ")
        resulation = input("Video Kalitesi 'En Yüksek Kalite İçin Sadece Entera Basın': ")
        resulation += "p"
        downloadVideo(link, resulation)
    if(opt == "2"):
        link = input("Playlist Linki: ")
        resulation = input("Video Kalitesi 'En Yüksek Kalite İçin Sadece Entera Basın': ")
        resulation += "p"
        downloadPlaylist(link, resulation)
        continue
    if(opt.lower() == "e"):
        exit()
    else:
        print("???????")
