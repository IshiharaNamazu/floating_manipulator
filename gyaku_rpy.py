from scipy.spatial.transform import Rotation as R
import numpy as np

# 任意のRPY
rpy = [0, 0.980, 0]  # ラジアン
rot = R.from_euler("xyz", rpy)

# 回転行列の逆 → RPYに戻す
inv_rot = rot.inv()
inv_rpy = inv_rot.as_euler("xyz")
print(inv_rpy)
