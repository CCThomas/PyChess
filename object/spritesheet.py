from PIL import Image
from PIL import ImageTk


class Spritesheet:
    def __init__(self, file_name, width, height):
        spritesheet_location = "resources/images/32x32/" + file_name
        self.spritesheet = Image.open(spritesheet_location)
        self.spritesheet_width = self.spritesheet.size[0]  # .size() -> [width, height]
        self.width = width
        self.height = height
        self.number_of_sprites = int(self.spritesheet_width / self.width)

    def get_sprite(self, row_num, col_num, scale_x, scale_y):
        x = self.width * col_num
        y = self.height * row_num
        box = (x, y, x + self.width, y + self.height)
        self.image = self.spritesheet.crop(box)
        self.image_scaled = self.image.resize((scale_x, scale_y), Image.ANTIALIAS)
        return ImageTk.PhotoImage(self.image_scaled)