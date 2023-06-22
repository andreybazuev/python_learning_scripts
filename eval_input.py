import math


def eval_loop(inp):
    
    while inp != "готово":
        print(eval(inp))
        inp = input("введите команду: ")

    return

i = input("введите команду: ")
eval_loop(i)