from apiclient.discovery import build
import pprint

API_KEY = "***************************************"
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_channels():
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )
    responses = youtube.search().list(
        q=["ボクシング", "村田諒太"],
        part="id,snippet",
        maxResults=100
    ).execute()

    channel_dict = dict()
    for item in responses.get("items", list()):
        try:
            snippet = item["snippet"]
        except Exception as e:
            print(e)
        else:
            channel_dict[snippet["channelId"]] = snippet["channelTitle"]
    
    return channel_dict

def get_channel_details(channel_id):
    youtube =  build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    responses = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    return responses["items"][0]

def main():
    channel_dict = get_channels()
    for channel_id, channel_title in channel_dict.items():
        channel_details = get_channel_details(channel_id)
        try:
            subscriberCount = int(channel_details["statistics"]["subscriberCount"])
        except Exception as e:
            print(e)
        else:
            if (9400 <= subscriberCount <= 9800):
                print(channel_id)
                print(channel_title)
                print(subscriberCount)

if __name__ == "__main__":
    main()