#第7回python勉強会
#自作関数

def sum_2(*values):
    """
　　目的：合計値の計算
    input：int or float
    output：sum of values
    """
    save = 0
    for value in values:
        save += value
    return save




