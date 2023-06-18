from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


def time_to_seconds(time_str):
    """Convert a string time in format 'hh:mm:ss' or 'mm:ss' into seconds."""
    parts = list(map(int, time_str.split(':')))
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    else:
        raise ValueError("Invalid time format")


def segmentador_video(nome_video_original, start_time, end_time, legenda):
    # Caminho do vídeo original
    input_video = nome_video_original

    # Carregar o vídeo
    clip = VideoFileClip(input_video)

    # Definir horário de início e fim como strings
    start_time_str = start_time
    end_time_str = end_time

    # Converter as strings de tempo para segundos
    start_time = time_to_seconds(start_time_str)
    end_time = time_to_seconds(end_time_str)

    # Segmentar o vídeo
    subclip = clip.subclip(start_time, end_time)

    # Criar legenda
    subtitle = TextClip(legenda, fontsize=24, color='white')

    # Definir a duração da legenda para coincidir com a duração do subclip
    subtitle = subtitle.set_duration(subclip.duration)

    # Posicionar a legenda na parte inferior do vídeo
    subtitle = subtitle.set_position(('center', 'bottom'))

    # Combinar o subclip de vídeo e a legenda
    final_clip = CompositeVideoClip([subclip, subtitle])

    # Nome do arquivo de saída
    nome_video_sem_extensao = nome_video_original.split(".")[0]
    output_video = f"{nome_video_sem_extensao}-{legenda}.mp4"

    # Exportar o vídeo
    final_clip.write_videofile(output_video, codec='libx264')

    clip.close()
    subclip.close()
    subtitle.close()
    final_clip.close()
