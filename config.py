from flask_uploads import UploadSet, configure_uploads, IMAGES

photos = UploadSet('photos', IMAGES)

def configure_app(app):
    configure_uploads(app, photos)