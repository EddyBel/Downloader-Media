from asyncore import write
import pytube
from pytube import Playlist
from pytube.cli import on_progress
from scripts.tools import TOOLS


class Youtube:

    # ----------------------------Video------------------------------

    # Objeto de youtube
    def objetoYoutube(url):
        return pytube.YouTube(url, on_progress_callback=on_progress)

    # Datos del video
    def dataVideo(url, quality='general', progressive=True):
        yt = Youtube.objetoYoutube(url)
        id = 0
        # Lista de datos de video
        dataVideo = []
        # print(yt.streams)
        if quality == 'general':
            # Obtener todos los datos del video
            data = yt.streams.filter(type='video', progressive=True)
            dataTwo = yt.streams.filter(type='video', progressive=False)
            # Recorrer los datos y pasar los mencionados a un array
            for i in data:
                dataVideo.append(
                    [id, i.itag, i.type, i.resolution, i.fps, True])
                id = id + 1
            for x in dataTwo:
                dataVideo.append(
                    [id, x.itag, x.type, x.resolution, x.fps, False])
                id = id + 1
            # retornar el array
            return dataVideo
        else:
            # Obtener los datos filtrando los valores solicitados
            data = yt.streams.filter(
                type='video', res=quality, progressive=progressive)
            # print(data)
            # Verificar si la variable tiene algo
            if (len(data) == 0):
                # Si esta vacio asigna la variable a un string llamado ERROR
                dataVideo = 'ERRROR'
            else:
                # Recorrer los datos y agregarlos al nuevo array
                for i in data:
                    dataVideo.append(
                        [id, i.itag, i.type, i.resolution, i.fps, progressive])
                    id = id + 1

            return dataVideo

    # Descargar video
    def downloadVideo(url, itag, path=TOOLS.dirname()):
        yt = Youtube.objetoYoutube(url)
        streams = yt.streams.get_by_itag(itag)
        title = TOOLS.newString(yt.title)
        print('Descargando .......... %s' % title + '.mp4')
        streams.download(path, title + '.mp4')
        print('\nDescarga completa.')

    # Obtener los datos de video
    def dataAudio(url):
        yt = Youtube.objetoYoutube(url)
        audio = yt.streams.filter(type='audio')
        dataAudio = []
        id = 0
        for i in audio:
            dataAudio.append([id, i.itag, i.type, i.abr])
            id = id + 1

        return dataAudio

    # Descarga el audio
    def downloadAudio(url, itag, path=TOOLS.dirname()):
        yt = Youtube.objetoYoutube(url)
        streams = yt.streams.get_by_itag(itag)
        title = TOOLS.newString(yt.title)
        print('Descargando .......... %s' % title + '.mp3')
        streams.download(path, title + '.mp3')
        print('\nDescarga completa.')

    # -------------------------------Playlist-----------------------------

    # Objeto playlist
    def objectPlaylist(url):
        yt = Playlist(url)
        return yt

    # Descarga los videos de la playlist
    def downloadPlaylistVideos(url, path=TOOLS.dirname()):
        yt_playlist = Youtube.objectPlaylist(url)
        print('\nVideos encontrados : {videos}'.format(
            videos=len(yt_playlist)))

        count = 0

        for video in yt_playlist.videos:
            try:
                title = TOOLS.newString(video.title)
                print('\nDescargando ........ %s' % title + '.mp4')
                video.streams.get_highest_resolution().download(path, title + '.mp4')
                count = count + 1
            except:
                print('\nError al descargar %s' % video.title)
        print('\nDescarga Completa!!')
        print('\n {videosDownloaded} videos descargados.'.format(
            videosDownloaded=count))

    # Descarga los audios de la playlist

    def downloadPlaylistAudio(url, path=TOOLS.dirname()):
        yt_playlist = Youtube.objectPlaylist(url)
        print('\nVideos encontrados : {videos}'.format(
            videos=len(yt_playlist)))

        count = 0

        for video in yt_playlist.videos:
            try:
                title = TOOLS.newString(video.title)
                print('\nDescargando ........ %s' % title + '.mp3')
                video.streams.get_audio_only().download(path, title + '.mp3')
                count = count + 1
            except:
                print('\nError al descargar %s' % video.title)
        print('\nDescarga Completa!!')
        print('\n {videosDownloaded} videos descargados.'.format(
            videosDownloaded=count))

    # ----------------------Descarga desde archivo-------------------------

    # Obtener los videos del archivo
    def getVideosInFile(path='default'):
        if path == 'default':
            file = open(TOOLS.dirname() + '/resources/videos.txt')
            lines = file.readlines()
            file.close()
            listLines = []
            for line in lines:
                listLines.append(line.rstrip('\n'))
            return listLines
        else:
            file = open(path)
            lines = file.readlines()
            file.close()
            listLines = []
            for line in lines:
                listLines.append(line.rstrip('\n'))
            return listLines

    # Descarga la lista de videos

    def downloadVideos(videos, path=TOOLS.dirname()):
        print('\nVideos encontrados {videosUrl}'.format(videosUrl=len(videos)))
        count = 0
        for video in videos:
            try:
                yt = pytube.YouTube(video, on_progress_callback=on_progress)
                title = TOOLS.newString(yt.title)
                print('\nDescargando ........ %s' % title + '.mp4')
                yt.streams.get_highest_resolution().download(path, title + '.mp4')
                print('\nDescarga completa.')
                count = count + 1
            except:
                print('Error al descargar ' + yt.title)
        print('\nVideos descargados {videosDownloaded}'.format(
            videosDownloaded=count))

    # Descarga la lista de videos solo audio
    def downloadAudios(videos, path=TOOLS.dirname()):
        print('\nVideos encontrados {videosUrl}'.format(videosUrl=len(videos)))
        count = 0
        for video in videos:
            try:
                yt = pytube.YouTube(video, on_progress_callback=on_progress)
                title = TOOLS.newString(yt.title)
                print('\nDescargando ........ %s' % title + '.mp3')
                yt.streams.get_audio_only().download(path, title + '.mp3')
                print('\nDescarga completa.')
                count = count + 1
            except:
                print('Error al descargar ' + yt.title)
        print('\nVideos descargados {videosDownloaded}'.format(
            videosDownloaded=count))


if __name__ == '__main__':
    print(Youtube.objectPlaylist(
        'https://www.youtube.com/watch?v=gOdBRGvXhkM&list=RDgOdBRGvXhkM&start_radio=1&rv=gOdBRGvXhkM&t=1'))
