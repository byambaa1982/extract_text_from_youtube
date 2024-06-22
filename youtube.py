from pytube import YouTube

# Function to download YouTube video
def download_youtube_video(url, output_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(output_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output path (default is current directory): ") or '.'
    download_youtube_video(video_url, output_path)
