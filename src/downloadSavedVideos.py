import instaloader

# Get instance
def downloadSavedVideos(username, max_count):
    loader = instaloader.Instaloader(download_video_thumbnails=False,save_metadata=False,compress_json=False,post_metadata_txt_pattern=None,)

    # Get login session, should do python 615_import_firefox_session.py first
    loader.load_session_from_file(username) 

    # Get 10 saved videos
    loader.download_saved_posts(max_count, fast_update=True)