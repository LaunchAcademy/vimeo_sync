import pdb
import os
import sys
import vimeo

import dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

class VimeoSync:
    def __init__(self, filename, title):
        self.filename = filename
        self.title = title
        self.loadCredentials()

    def loadCredentials(self):
        self.token = os.environ.get("VIMEO_FULL_ACCESS_TOKEN")
        self.key = os.environ.get("VIMEO_CLIENT_ID")
        self.secret = os.environ.get("VIMEO_CLIENT_SECRET")
        self.video_password = os.environ.get("VIDEO_PASSWORD")

    def patch_data(self):
        data = { "name": self.title }
        if self.video_password:
            data["privacy"] = { "view": "password" }
            data["password"] = self.video_password
        return data

    def upload(self):
        v = vimeo.VimeoClient(
            token = self.token,
            key = self.key,
            secret = self.secret
        )
        video_path = v.upload(self.filename)
        pdb.set_trace()
        response = v.patch(video_path, self.patch_data())
        return response.ok


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide a filename and a title as arguments.")
        print("ex: python vimeo_uploader.py filename.mp4 'My Video'")
        sys.exit()
    else:
        VimeoSync(sys.argv[1], sys.argv[2]).upload()
