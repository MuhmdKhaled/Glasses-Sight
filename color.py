import cv2
import numpy as np
import webcolors

# Custom dictionary
CSS3_HEX_TO_NAMES = {
    '#F0F8FF': 'aliceblue', '#FAEBD7': 'antiquewhite', '#00FFFF': 'aqua',
    '#7FFFD4': 'aquamarine', '#F0FFFF': 'azure', '#F5F5DC': 'beige',
    '#FFE4C4': 'bisque', '#000000': 'black', '#FFEBCD': 'blanchedalmond',
    '#0000FF': 'blue', '#8A2BE2': 'blueviolet', '#A52A2A': 'brown',
    '#DEB887': 'burlywood', '#5F9EA0': 'cadetblue', '#7FFF00': 'chartreuse',
    '#D2691E': 'chocolate', '#FF7F50': 'coral', '#6495ED': 'cornflowerblue',
    '#FFF8DC': 'cornsilk', '#DC143C': 'crimson', '#00FFFF': 'cyan',
    '#00008B': 'darkblue', '#008B8B': 'darkcyan', '#B8860B': 'darkgoldenrod',
    '#A9A9A9': 'darkgray', '#006400': 'darkgreen', '#BDB76B': 'darkkhaki',
    '#8B008B': 'darkmagenta', '#556B2F': 'darkolivegreen', '#FF8C00': 'darkorange',
    '#9932CC': 'darkorchid', '#8B0000': 'darkred', '#E9967A': 'darksalmon',
    '#8FBC8F': 'darkseagreen', '#483D8B': 'darkslateblue', '#2F4F4F': 'darkslategray',
    '#00CED1': 'darkturquoise', '#9400D3': 'darkviolet', '#FF1493': 'deeppink',
    '#00BFFF': 'deepskyblue', '#696969': 'dimgray', '#1E90FF': 'dodgerblue',
    '#B22222': 'firebrick', '#FFFAF0': 'floralwhite', '#228B22': 'forestgreen',
    '#FF00FF': 'fuchsia', '#DCDCDC': 'gainsboro', '#F8F8FF': 'ghostwhite',
    '#FFD700': 'gold', '#DAA520': 'goldenrod', '#808080': 'gray', '#008000': 'green',
    '#ADFF2F': 'greenyellow', '#F0FFF0': 'honeydew', '#FF69B4': 'hotpink',
    '#CD5C5C': 'indianred', '#4B0082': 'indigo', '#FFFFF0': 'ivory',
    '#F0E68C': 'khaki', '#E6E6FA': 'lavender', '#FFF0F5': 'lavenderblush',
    '#7CFC00': 'lawngreen', '#FFFACD': 'lemonchiffon', '#ADD8E6': 'lightblue',
    '#F08080': 'lightcoral', '#E0FFFF': 'lightcyan', '#FAFAD2': 'lightgoldenrodyellow',
    '#D3D3D3': 'lightgray', '#90EE90': 'lightgreen', '#FFB6C1': 'lightpink',
    '#FFA07A': 'lightsalmon', '#20B2AA': 'lightseagreen', '#87CEFA': 'lightskyblue',
    '#778899': 'lightslategray', '#B0C4DE': 'lightsteelblue', '#FFFFE0': 'lightyellow',
    '#00FF00': 'lime', '#32CD32': 'limegreen', '#FAF0E6': 'linen',
    '#FF00FF': 'magenta', '#800000': 'maroon', '#66CDAA': 'mediumaquamarine',
    '#0000CD': 'mediumblue', '#BA55D3': 'mediumorchid', '#9370DB': 'mediumpurple',
    '#3CB371': 'mediumseagreen', '#7B68EE': 'mediumslateblue', '#00FA9A': 'mediumspringgreen',
    '#48D1CC': 'mediumturquoise', '#C71585': 'mediumvioletred', '#191970': 'midnightblue',
    '#F5FFFA': 'mintcream', '#FFE4E1': 'mistyrose', '#FFE4B5': 'moccasin',
    '#FFDEAD': 'navajowhite', '#000080': 'navy', '#FDF5E6': 'oldlace',
    '#808000': 'olive', '#6B8E23': 'olivedrab', '#FFA500': 'orange',
    '#FF4500': 'orangered', '#DA70D6': 'orchid', '#EEE8AA': 'palegoldenrod',
    '#98FB98': 'palegreen', '#AFEEEE': 'paleturquoise', '#DB7093': 'palevioletred',
    '#FFEFD5': 'papayawhip', '#FFDAB9': 'peachpuff', '#CD853F': 'peru',
    '#FFC0CB': 'pink', '#DDA0DD': 'plum', '#B0E0E6': 'powderblue',
    '#800080': 'purple', '#FF0000': 'red', '#BC8F8F': 'rosybrown',
    '#4169E1': 'royalblue', '#8B4513': 'saddlebrown', '#FA8072': 'salmon',
    '#F4A460': 'sandybrown', '#2E8B57': 'seagreen', '#FFF5EE': 'seashell',
    '#A0522D': 'sienna', '#C0C0C0': 'silver', '#87CEEB': 'skyblue',
    '#6A5ACD': 'slateblue', '#708090': 'slategray', '#FFFAFA': 'snow',
    '#00FF7F': 'springgreen', '#4682B4': 'steelblue', '#D2B48C': 'tan',
    '#008080': 'teal', '#D8BFD8': 'thistle', '#FF6347': 'tomato',
    '#40E0D0': 'turquoise', '#EE82EE': 'violet', '#F5DEB3': 'wheat',
    '#FFFFFF': 'white', '#F5F5F5': 'whitesmoke', '#FFFF00': 'yellow',
    '#9ACD32': 'yellowgreen'
}

def closest_color(requested_color):
    min_colors = {}
    for key, name in CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(requested_color):
    try:
        closest_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
    return closest_name

image_path = r'C:\Users\ascom\Desktop\project updates\images.png'
image = cv2.imread(image_path)


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixels = image_rgb.reshape((-1, 3))

pixels = np.float32(pixels)

# Define criteria, number of clusters(K) and apply K-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 5
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)

dominant_color = centers[np.argmax(np.bincount(labels.flatten()))]

color_name = get_color_name(tuple(dominant_color))

print(f"Dominant color is : {color_name}")
