"""
module holding thumbnail creation functions
"""

from PIL import Image
import os
import glob


def create_thumbs_directory(thumb_pixels=128, file_path_regex='./*.jpg', verbose=False):
    """
    Create a sub-directory with thumbnails of image files in a directory
    
    Parameters:
    thumb_pixels: integer: size in pixels of square aspect ratio thumbnails
    file_path_regex: string: string holding path regex to image files (JPG files)
    verbose: boolean: if True, outputs text showing file names processed
    
    Returns:
    count of files processed
    
    Environment: assumes that there is an existing subdirectory below the image directory,
    called /thumbnails
    """
    size = thumb_pixels, thumb_pixels
    file_count=0
    for infile in glob.glob(file_path_regex):
        file, ext = os.path.splitext(infile)
        if( verbose):
            print('Opening: ',infile )
        #end if
        im = Image.open(infile)
        im.thumbnail(size)
        fpath, name = os.path.split(file)
        im.save(fpath + '/thumbnails/' + name + '-thumbnail.jpg', "JPEG")
        file_count = file_count+1
        if( verbose):
            print('Saved thumbnail for: '+file)
        #end if
    #end for
    return file_count
#end create_thumbs_directory