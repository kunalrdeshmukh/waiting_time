import matplotlib. pyplot as plt


x_min = 0.0
x_max = 0.0

mean = 0.0
std = 0.0


def consume(waiting,consumption_rate,_plt_points,cur_time):
    if consumption_rate >= len(waiting):
        for i in waiting:
            _plt_points.append(((cur_time - i),i))
        return [],_plt_points
    else :
        for i in range(consumption_rate):
            t = waiting.pop(0)
            _plt_points.append(((cur_time - t),t))
        return waiting,_plt_points

def add(waiting,addition_rate,cur_time):
    for i in range(addition_rate):
        waiting.append(cur_time)
    return waiting 


def run(waiting,addition_rate,consumption_rate,run_time):
    _plt_points = []
    for i in range(run_time):
        if i > 20 :
            addition_rate = 5
        if i > 70 : 
            addition_rate = 7
        if i > 90 :
            addition_rate  = 3
        waiting = add(waiting,addition_rate,i)
        waiting,_plt_points = consume(waiting,consumption_rate,_plt_points,i)
    _x,_y = [],[]
    for ele in _plt_points:
        _x.append(ele[0])
        _y.append(ele[1])
    plt.plot(_y,_x)
    plt.xlabel("Vehicle arrived at")
    plt.ylabel("no of mins in line")
    plt.show()


if __name__ == "__main__":
    waiting = []
    addition_rate = 3
    consumption_rate = 4
    run_time =200
    run(waiting,addition_rate,consumption_rate,run_time)