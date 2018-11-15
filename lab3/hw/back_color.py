from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():

    return shapes

def generate_quiz():
    text_list = []
    color_list= []
    for shape in shapes:
        text_list.append(shape["text"])
        color_list.append(shape["color"])
    quiz_type = randint(0, 1)
    tex = choice(text_list)
    if quiz_type == 0:
        text= tex + " (meaning)" 
    else:
        text= tex + " (color)"
    color = choice(color_list)
    return [    text,
                color,
                quiz_type # 0 : meaning, 1: color
            ]

def is_inside(i, j):
    return (i[0]>j[0]) and (i[0]<j[0]+j[2]) and (i[1]>j[1]) and (i[1]<j[1]+j[3])

def mouse_press(x, y, text, color, quiz_type):
    for i in shapes:
        if quiz_type == 0:
            if text == i["text"] + " (meaning)":
                if is_inside([x, y], i["rect"]):
                    return True
                else:
                    return False 
            else:
                pass
        else:
            if color == i["color"]:
                if is_inside([x, y], i["rect"]):
                    return True
                else:
                    return False
            else:
                pass 


                     
