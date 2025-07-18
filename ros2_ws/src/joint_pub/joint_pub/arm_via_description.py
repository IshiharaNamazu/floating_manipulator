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

arm_via = [
    [3, [0, 0, 0, 0, 0, 0]],  # [period[s], [q0, q1, q2, q3, q4, q5]]
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 定位置
    # つかむ
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 1
    [3, [radians(-70), -pi / 6, radians(150), radians(-150), 0, 0]],  # 2-1
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), 0, 0]],  # 2-2
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), radians(100), radians(60)]],  # 2
    [3, [radians(-110), -pi / 6, pi / 2, radians(35), radians(80), radians(60)]],  # 3
    # はなす
    [3, [radians(-110), -pi / 6, pi / 2, radians(35), radians(80), radians(60)]],  # 3
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), radians(100), radians(60)]],  # 2
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), 0, 0]],  # 2-2
    [3, [radians(-70), -pi / 6, radians(150), radians(-150), 0, 0]],  # 2-1
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 1
    # つかむ
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 1
    [3, [0, -pi / 3, radians(150), radians(-150), radians(100), radians(60)]],  # 2-1
    [3, [0, radians(-60), pi / 2, radians(35), radians(100), radians(60)]],  # 2-2
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), radians(100), radians(60)]],  # 2
    [3, [radians(-110), -pi / 6, pi / 2, radians(35), radians(80), radians(60)]],  # 3
    # はなす
    [3, [radians(-110), -pi / 6, pi / 2, radians(35), radians(80), radians(60)]],  # 3
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), radians(100), radians(60)]],  # 2
    [3, [radians(-70), -pi / 6, pi / 2, radians(35), 0, 0]],  # 2-2
    [3, [radians(-70), -pi / 6, radians(150), radians(-150), 0, 0]],  # 2-1
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 1
    # もどる
    [3, [0, radians(-60), radians(150), radians(-150), 0, 0]],  # 定位置
    [3, [0, 0, 0, 0, 0, 0]],  # [period[s], [q0, q1, q2, q3, q4, q5]]
]


def arm_via_add_reverse():
    """
    arm_viaの逆順を追加する関数
    """
    arm_via.extend(reversed(arm_via))


# arm_via_add_reverse()
