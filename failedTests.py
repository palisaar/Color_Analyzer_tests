from colorthief import ColorThief

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

color_thief = ColorThief('segmentation.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=5)

print(palette)
print(rgb_to_hex((156, 236, 220)))

#for i in palette:
    #print(i)
    #print(rgb_to_hex([i]))