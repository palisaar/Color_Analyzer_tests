from PIL import Image


def rgbstr_to_hex(rgb_string):
    # input should look like this: (126, 200, 100)

    # removes opening brackets
    rgb_string = rgb_string.replace('(', '')

    # removes closing brackets
    rgb_string_without_brackets = rgb_string.replace(')', '')

    # converts a string like 126, 200, 100 into a tupel
    rgb_tupel = tuple(map(int, rgb_string_without_brackets.split(', ')))

    # returns a HEX code for an rgb tupel
    return '%02x%02x%02x' % rgb_tupel


# opens an image
im = Image.open("segmentation.png")

# creates a list for the colors to be stored in
colorlist = []

for pixel in im.getdata():
    # if the color already exists in the list, it get skipped
    if rgbstr_to_hex(str(pixel)[:-6] + ")") not in colorlist:
        # adds the color to the list
        colorlist.append(rgbstr_to_hex(str(pixel)[:-6] + ")"))

print(colorlist)