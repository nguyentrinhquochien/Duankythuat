import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm
import re

class SketchFromSVG:
    def __init__(self, path, scale=30, x_offset=400, y_offset=400):
        self.path = path
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.scale = scale
        self.pen = tu.Turtle()

    def hex_to_rgb(self, string):
        strlen = len(string)
        if string.startswith('#'):
            if strlen == 7:
                r, g, b = string[1:3], string[3:5], string[5:7]
            elif strlen == 4:
                r, g, b = string[1:2] * 2, string[2:3] * 2, string[3:4] * 2
            elif strlen == 3:
                r, g, b = string[0:1] * 2, string[1:2] * 2, string[2:3] * 2
            else:
                r, g, b = string[0:2], string[2:4], string[4:6]
        
        return int(r, 16) / 255, int(g, 16) / 255, int(b, 16) / 255

    def load_svg(self):
        print('loading data')
        paths, attributes, svg_att = svg2paths2(self.path)
        h = svg_att.get("height", "0")
        w = svg_att.get("width", "0")
        
        # Use a regular expression to extract numeric parts
        height_match = re.search(r'\d+', h)
        width_match = re.search(r'\d+', w)

        # Use the extracted values if found, otherwise default to 0
        self.height = int(height_match.group()) if height_match else 0
        self.width = int(width_match.group()) if width_match else 0

        res = []
        for i in tqdm(attributes):
            path = parse_path(i.get('d', ''))
            co = i.get('fill', 'black')
            col = self.hex_to_rgb(co)
            n = len(list(path)) + 2       
            pts = [
                (
                    (int((p.real / self.width) * self.scale)) - self.x_offset,
                    (int((p.imag / self.height) * self.scale)) - self.y_offset
                ) for p in (path.point(i / n) for i in range(0, n + 1))
            ]
            res.append((pts, col))
        print('svg data loaded')
        return res

    def move_to(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()

    def draw(self, retain=True):
        coordinates = self.load_svg()
        self.pen.speed(0)
        for path_col in coordinates:
            f = 1
            self.pen.color('black')
            path = path_col[0]
            col = path_col[1]
            self.pen.color(col)
            self.pen.begin_fill()
            next = 0
            for coord in path:
                x, y = coord
                y *= -1
                if f:
                    self.move_to(x, y)
                    f = 0
                else:
                    self.pen.goto(x, y)
            self.pen.end_fill()

        if retain:
            tu.done()

pen = SketchFromSVG('bxi.svg', scale=800, drawing_speed=5)
pen.draw()
