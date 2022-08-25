from scripts.youtube import Youtube
from scripts.tools import TOOLS

# ingresar el tipo de descarga
print('\nPlataforma para descargar. ')
platformList = [[0, 'Youtube']]
TOOLS.printTabulate(platformList, ['ID', 'PLATAFORMA'])
platform = input('\nIngresa el id de la plataforma : ')
# Verfica que el valor ingresado sea valido
platform = TOOLS.validationID(platformList, platform, 'Ingresa un id valido: ')


# Entra a las operaciones de la plataforma
if (platform == '0'):

    # Imprime las opciones de descarga en una tabla
    print('\n-------------- Opciones --------------')
    optionsYoutube = [[0, 'Video'],
                      [1, 'Audio'],
                      [2, 'Playlist VIDEO'],
                      [3, 'Playlist AUDIO'],
                      [4, 'Desde archivo']]

    TOOLS.printTabulate(optionsYoutube, ['ID', 'OPCION'])

    # Selecciona la opcion y verifica que sea valida
    optionYoutube = input('\nIngresa el id de la opcion: ')
    optionYoutube = TOOLS.validationID(
        optionsYoutube, optionYoutube, 'Ingresa un id valido: ')

    # Descarga video
    if optionYoutube == '0':
        url = input('\nIngresa la url del video: ')

        try:
            # Obtener todos los datos de el video, imprimirlo en una tabla
            dataVideo = Youtube.dataVideo(url)
            TOOLS.printDataVideo(dataVideo)

            # Selecciona el video a descargar
            quality = input('\nIngresa el id de la opcion: ')
            quality = TOOLS.validationID(
                dataVideo, quality, 'Ingresa un id valido: ')

            # Obten los valores de el video
            videoData = TOOLS.getObject(dataVideo, quality)
            # Descarga el video
            Youtube.downloadVideo(url, videoData[1])
        except:
            print('Error inesperado.')

    # Descarga el audio
    elif optionYoutube == '1':
        url = input('\nIngresa la url del video: ')

        try:
            # Obtener los datos e imprimir la tabla
            dataAudio = Youtube.dataAudio(url)
            TOOLS.printTabulate(dataAudio, ['ID', 'ITAG', 'TIPO', 'CALIDAD'])

            # Seleccionar el audio
            id = input('\nIngresa el id de la opcion: ')
            id = TOOLS.validationID(dataAudio, id, 'Ingresa un id valido: ')

            # Obten los valores de el audio
            audioOption = TOOLS.getObject(dataAudio, id)
            # Descarga el audio
            Youtube.downloadAudio(url, audioOption[1])
        except:
            print('Error inesperado')

    # Descarga desde una playlist
    elif optionYoutube == '2':
        url = input('\nIngresa la url: ')
        Youtube.downloadPlaylistVideos(url)

    # Descarga desde una playlist los audios
    elif optionYoutube == '3':
        url = input('\nIngresa la url: ')
        Youtube.downloadPlaylistAudio(url)

    # Descarga desde un archivo txt.
    elif optionYoutube == '4':
        path = input('\nCual es la direccion de tu archivo txt? ')
        videos = Youtube.getVideosInFile(path)

        # Tabla de opciones
        optionsDownload = [[0, 'Video'], [1, 'Audio']]
        TOOLS.printTabulate(optionsDownload, ['ID', 'OPCIONES'])

        option = input('Selecciona que tipo de descarga sera: ')

        # Verificar que sea valido
        TOOLS.validationID(optionsDownload, option, 'Ingresa una id valida')

        # Descarga video
        if option == '0':
            Youtube.downloadVideos(videos)
        else:
            Youtube.downloadAudios(videos)

elif (platform == '1'):
    print('-------------- Opciones --------------')
    optionsWeb = [[0, 'Imagenes'], [1, 'Videos']]
