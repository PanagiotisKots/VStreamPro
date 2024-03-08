from pytube import YouTube, Search
from moviepy.editor import AudioFileClip
import os
from colorama import Fore, Style
import time
from youtubesearchpython import VideosSearch

def download_video(youtube_object):
    stream = youtube_object.streams.filter(file_extension='mp4').first()
    
    if stream:
        print(Fore.GREEN + "Downloading video...")
        stream.download()
        print("Video downloaded successfully.")
    else:
        print(Fore.RED + "No suitable video stream found.")

def download_audio(youtube_object):
    stream = youtube_object.streams.filter(file_extension='mp4').first()
    
    if stream:
        print(Fore.GREEN + "Downloading video...")
        stream.download(output_path=os.getcwd(), filename='video_temp')
        print("Video downloaded successfully.")
        
        print(Fore.YELLOW + "Extracting audio...")
        time.sleep(2)  # Just for demonstration purposes, can be removed
        video_path = 'video_temp.mp4'
        audio_path = 'audio_temp.mp3'
        video_clip = AudioFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        os.remove(video_path)
        print("Audio extracted and saved successfully.")
    else:
        print(Fore.RED + "No suitable video stream found.")

def download_multiple(urls):
    try:
        output_path = input("Enter the output directory (or press Enter for the current directory): ").strip()
        if not output_path:
            output_path = os.getcwd()

        for url in urls:
            yt = YouTube(url.strip())
            print(Fore.YELLOW + f"Title: {yt.title}")
            choice = input("Enter 'video' to download video, 'audio' to download audio: ").strip().lower()

            if choice == 'video':
                download_video(yt)
            elif choice == 'audio':
                download_audio(yt)
            else:
                print(Fore.RED + "Invalid choice. Please enter 'video' or 'audio'.")
    except Exception as e:
        print(Fore.RED + "An error occurred:", e)

def main():
    print("\n\n\n")
    logo_half_length = 40  # Length of half the logo

    # Print the first half of the logo in blue
    print(Fore.RED )
   
    print(Fore.BLUE + "$$$$$$$$$$$$$$$$$$     $$$                    $$$     $$$$$$$$$$$$$$$$$$$$$$$$$                ")
    print("$$$            $$$       $$$                $$$       ", end="")
    
    # Print the second half of the logo in red
    print(Fore.RED + "$$$$$$$$$$$$$$$$$$$$$$$$$   ")
    print("$$$            $$$        $$$             $$$                    $$$")
    print(Fore.BLUE +"$$$            $$$          $$$         $$$                      $$$")
    print("$$$            $$$            $$$     $$$                        $$$")
    print(Fore.RED +"$$$            $$$              $$$ $$$                          $$$")
    print("$$$$$$$$$$$$$$$$$$                $$$                            $$$ " )
    print(Fore.BLUE +"$$$                               $$$                            $$$")
    print("$$$                               $$$                            $$$")
    print(Fore.RED +"$$$                               $$$                            $$$")
    print("$$$                               $$$                            $$$   ")
    print(Fore.BLUE +"$$$     $$$        $$$            $$$                            $$$   ")            
    print("$$$       $$$    $$$              $$$                            $$$         ")        
    print(Fore.RED +"$$$         $$$ $$$               $$$                            $$$       ")         
    print("$$$           $$$                 $$$                            $$$               ")         
    print(Fore.BLUE +"$$$           $$$                 $$$                            $$$     " )
    print("$$$           $$$                 $$$                            $$$       ")
    
    print("\n")
    print(Fore.CYAN +"$$$ Created by:($$$ KOTSORGIOS PANAGIOTIS $$$)")
    print("$$$ Version 0.0.0.1 of PyYT Downloader $$$")
    print("$$$ Offering mass video/audio download option in high quality $$$")
    print("$$$ Allowing Searching results and name downloads of audio/video $$$")
    print("\n\n")
    
    while True:
        try:
            choice = int(input(Fore.BLUE +"Enter your choice below:\n1. Download separate videos/audios one at a time\n2. Download multiple videos/audios at the same time\n3. Search and download videos by name\n"))

            if choice == 1:
                try:
                    print(Style.RESET_ALL, end='')  # Reset color
                    url = input("Enter the YouTube video URL (or 'exit' to quit): ").strip()
                    if url.lower() == 'exit':
                        print(Fore.CYAN + "Exiting the program.")
                        break
                    
                    yt = YouTube(url)
                    
                    print(Fore.YELLOW + f"Title: {yt.title}")
                    
                    choice = input("Enter 'video' to download video, 'audio' to download audio: ").strip().lower()
                    
                    if choice == 'video':
                        download_video(yt)
                    elif choice == 'audio':
                        download_audio(yt)
                    else:
                        print(Fore.RED + "Invalid choice. Please enter 'video' or 'audio'.")
                except Exception as e:
                    print(Fore.RED + "An error occurred:", e)

            elif choice == 2:
                urls = input("Enter the YouTube video URLs separated by commas: ").strip().split(',')
                download_multiple(urls)
            elif choice == 3:
                query = input("Enter your search query: ")
                videos_search = VideosSearch(query, limit=10)
                search_results = videos_search.result()
                print("Search results:")
                for i, video in enumerate(search_results['result']):
                    print(f"{i+1}. Title: {video['title']}")
                    print(f"   URL: {video['link']}")
                    print()
                download_choices = input("Enter the video numbers you want to download (separated by commas): ").split(',')
                selected_videos = [int(choice) - 1 for choice in download_choices]
                urls_to_download = [search_results['result'][index]['link'] for index in selected_videos]
                download_multiple(urls_to_download)
            else:
                print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter 1, 2, or 3 as your choice.")

if __name__ == "__main__":
    main()
