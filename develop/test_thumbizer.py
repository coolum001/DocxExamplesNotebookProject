import os
import pytest

from  thumbizer import thumbizer as thumb

def test_save():
    # target file to be created
    thumb_file = '../figures/test_images/thumbnails/test_image01-thumbnail.jpg'
    
    # remove it if it already exists
    os.remove(thumb_file) if os.path.exists(thumb_file) else None
    
    # create thumbnail
    thumb.create_thumbs_directory(thumb_pixels=200, verbose=True, 
                              file_path_regex='../figures/test_images/*.jpg')
    
    assert(os.path.exists(thumb_file))
    
#end test_save