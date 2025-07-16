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
x_b = np.array([-0.0155, -0.0294, 11.3085])  # [m]
rpy_b = [-0.1617, -0.0606, 0.5914]  # RPY

# Baseから見た先端の位置と姿勢
x_e = np.array([-0.8335, -1.2788, 5.3945])  # Baseから見た位置 [m]
rpy_e = [1.5873, 0.6040, -1.7097]  # RPY

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

rpy_g = (
    R.from_euler("xyz", [-90, 0, 0], degrees=True)
    * R.from_euler("xyz", [0, 0, 45], degrees=True)
).as_euler("xyz", degrees=False)
print(
    "ground plane pose:" + str(rpy_g[0]) + ", " + str(rpy_g[1]) + ", " + str(rpy_g[2])
)
