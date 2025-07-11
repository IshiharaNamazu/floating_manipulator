import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

from .arm_via_description import arm_via


class PlayTrajectory(Node):
    def __init__(self):
        super().__init__("play_trajectory")
        self.joint_publishers_ = []
        self.via_index_ = 0
        self.via_end_time_ = self.get_clock().now() + rclpy.duration.Duration(
            seconds=arm_via[0][0]
        )
        for i in range(6):
            topic = f"/floating_manipulator/joint{i}"
            pub = self.create_publisher(Float64, topic, 10)
            self.joint_publishers_.append(pub)
        self.timer_ = self.create_timer(
            0.001, self.publish_joint_velocity_linear
        )  # 20Hz
        self.pre_log_time_ = self.get_clock().now()

    def info_throttle(self, info_str, throttle_duration_sec=1.0):
        if (
            self.pre_log_time_ + rclpy.duration.Duration(seconds=throttle_duration_sec)
            <= self.get_clock().now()
        ):
            self.pre_log_time_ = self.get_clock().now()
            self.get_logger().info(info_str)

    def publish_joint_velocity_linear(self):
        # viaの時間が経過したら次のviaへ
        if self.via_end_time_ <= self.get_clock().now():
            if self.via_index_ >= len(arm_via) - 1:  # 最後のviaに到達した場合終了
                self.via_index_ = len(arm_via)
                self.info_throttle("end of trajectory")
            else:
                self.via_index_ += 1
                self.get_logger().info("next_via_index:" + str(self.via_index_))
                self.via_end_time_ += rclpy.duration.Duration(
                    seconds=arm_via[self.via_index_][0]
                )

        msgs = []
        if (self.via_index_ == 0) or (self.via_index_ >= len(arm_via)):
            for i in range(len(arm_via[0][1])):
                msg = Float64()
                msg.data = 0.0
                msgs.append(msg)
        else:
            for i in range(len(arm_via[self.via_index_][1])):
                msg = Float64()
                msg.data = (
                    arm_via[self.via_index_][1][i] - arm_via[self.via_index_ - 1][1][i]
                ) / arm_via[self.via_index_][0]
                msgs.append(msg)

        log_str = f"index:{self.via_index_}, publish joint velocity: "
        for i, msg in enumerate(msgs):
            log_str += f"joint{i}: {msg.data:.3f}, "
        self.info_throttle(log_str)

        for i, pub in enumerate(self.joint_publishers_):
            pub.publish(msgs[i])


def main(args=None):
    rclpy.init(args=args)
    node = PlayTrajectory()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
