from business import Painter
from converters import convert_from_canvas, convert_to_canvas, convert_to_line, convert_to_rectangle, create_new_canvas
from constants import CANVAS_VERTICAL_SIGN, CANVAS_HORIZONTAL_SIGN
import argparse
import os
import pickle


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--command', '-c',
        help='command from script description',
        dest='command',
    )
    args = parser.parse_args()
    return args.command


if __name__ == "__main__":
    command = parse_args()
    if command.startswith('C'):
        try:
            args = command.split(' ')
            painter = Painter()
            painter.start_new_picture(
                canvas=create_new_canvas(
                    width=int(args[1]),
                    height=int(args[2])
                )
            )
            pickle.dump(painter, open('db.txt', 'wb'))
            lines = convert_from_canvas(painter)
            with open('picture.txt', 'w') as picture:
                picture.write(lines)
        except Exception:
            print('canvas creation failed!')
    elif command.startswith('B'):
        try:
            args = command.split(' ')
            x = int(args[1])
            y = int(args[2])
            colour = args[3]
            painter = pickle.load(open('db.txt', 'rb'))
            painter.fill_with_colour(colour=colour)
            pickle.dump(painter, open('db.txt', 'wb'))
        except Exception:
            print('rectangle creation failed!')
    else:
        try:
            if command.startswith('L'):
                converter = convert_to_line
            elif command.startswith('R'):
                converter = convert_to_rectangle

            if not os.path.exists('db.txt'):
                print('create canvas!')
            else:
                args = command.split(' ')
                painter = pickle.load(open('db.txt', 'rb'))
                painter.paint_figure(
                    figure=converter(
                        x1=int(args[1]),
                        y1=int(args[2]),
                        x2=int(args[3]),
                        y2=int(args[4])
                    )
                )
                pickle.dump(painter, open('db.txt', 'wb'))
                lines = convert_from_canvas(painter)
                with open('picture.txt', 'w') as picture:
                    picture.write(lines)
        except Exception:
            print('line creation failed!')
