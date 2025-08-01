from pytube import YouTube

# L'URL de la vidéo à télécharger
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # "Never Gonna Give You Up"

try:
    # Création d'un objet YouTube
        yt = YouTube(url)
            
        # Afficher le titre de la vidéo
        print(f"Titre : {yt.title}")
                        
        # Afficher le nombre de vues
        print(f"Vues : {yt.views}")
                                    
        # Sélectionner le flux vidéo avec la plus haute résolution
        stream = yt.streams.get_highest_resolution()
                                                
                                                    # Télécharger la vidéo
        print("Téléchargement en cours...")
        stream.download()
        print("Téléchargement terminé !")
                                                                    
except Exception as e:
        print(f"Une erreur est survenue : {e}")