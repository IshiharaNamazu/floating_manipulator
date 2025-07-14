import numpy as np
from scipy.spatial.transform import Rotation as R


def transform_to_world(x_b, rpy_b, x_e, rpy_e, box_pos):
    """
    フレームBに対して x_e, rpy_e にある点のワールド座標系における位置と姿勢を求める。

    Parameters:
        x_b: フレームBの位置 [x, y, z]
        rpy_b: フレームBの姿勢 [roll, pitch, yaw]（ラジアン）
        x_e: フレームBから見た点の位置 [x, y, z]
        rpy_e: フレームBから見た点の姿勢 [roll, pitch, yaw]（ラジアン）

    Returns:
        x_result: ワールド座標系での位置
        rpy_result: ワールド座標系での姿勢（ラジアン）
    """

    # 回転オブジェクトの作成
    R_b = R.from_euler("xyz", rpy_b)
    R_e = R.from_euler("xyz", rpy_e)

    # ワールド座標での姿勢：R_b * R_e
    R_result = R_b * R_e
    rpy_result = R_result.as_euler("xyz")

    # ワールド座標での位置：x_b + R_b * x_e
    x_result = x_b + R_b.apply(x_e) + (R_b * R_e).apply(box_pos)

    return x_result, rpy_result


# --- 使用例 ---
# Baseフレーム（原点から見たロボットの位置・姿勢）
x_b = np.array([-0.0074, 0.0004, 11.0968])  # [m]
rpy_b = [-0.0677, -0.0647, 0.1176]  # RPY

# Baseから見た先端の位置と姿勢
x_e = np.array([-0.6782, -1.2820, 5.7572])  # Baseから見た位置 [m]
rpy_e = [1.4683, 0.0076, -1.6307]  # RPY

box_pos = [0, 0, 0.25]  # アームの先端向きのboxの位置

# 計算
x_world, rpy_world = transform_to_world(x_b, rpy_b, x_e, rpy_e, box_pos)

print("位置（ワールド座標）:", x_world)
print("姿勢（ワールド RPY）:", rpy_world)
print("copy below")
print(
    str(x_world[0])
    + ", "
    + str(x_world[1])
    + ", "
    + str(x_world[2])
    + ", "
    + str(rpy_world[0])
    + ", "
    + str(rpy_world[1])
    + ", "
    + str(rpy_world[2])
)
