import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json

# Define scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


async def upload_video(video_file, title, description, tags=None, category_id="1"):
    """
    Uploads a video to YouTube Shorts.

    Args:
        video_file (str): Path to the video file.
        title (str): Title of the video.
        description (str): Description of the video.
        tags (list): List of tags for the video.
        category_id (str): YouTube category ID. "22" is typically for "People & Blogs".
    """
    # OAuth flow
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "youtube_secrets.json", SCOPES
    )
    credentials = flow.run_local_server(port=8080)

    # Create API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Define the request body for the video upload
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or [],
            "categoryId": category_id,
        },
        "status": {"privacyStatus": "public"},  # Set "unlisted" or "private" if needed
    }

    # Execute video upload
    try:
        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=googleapiclient.http.MediaFileUpload(video_file),
        )
        response = request.execute()
        print(f"Upload successful! Video ID: {response['id']}")
    except googleapiclient.errors.HttpError as e:
        print(f"An error occurred: {e}")
        print(json.loads(e.content))
