from math import pi
from math import radians

arm_via = [
    [3, [0, 0, 0, 0, 0, 0]],  # 初期位置 [period[s], [q0, q1, q2, q3, q4, q5]]
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],
    [3, [radians(-75), -pi / 6, pi / 2, 0, radians(100), radians(60)]],
    [3, [radians(-105), -pi / 6, pi / 2, 0, radians(80), radians(60)]],
    [3, [radians(-105), -pi / 6, pi / 2, 0, radians(80), radians(60)]],
    [3, [0, 0, 0, 0, 0, 0]],  # 初期位置 [period[s], [q0, q1, q2, q3, q4, q5]]
]
