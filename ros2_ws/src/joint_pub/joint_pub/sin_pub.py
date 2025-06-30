import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import time

class SineWavePublisher(Node):
    """
    2つのトピックに異なる周波数の正弦波をパブリッシュするノード
    """
    def __init__(self):
        super().__init__('sine_wave_publisher')

        # パラメータの宣言と取得
        self.declare_parameter('freq0', 0.37)  # /topic0 の正弦波の周波数 (Hz)
        self.declare_parameter('freq1', 0.23)  # /topic1 の正弦波の周波数 (Hz)
        self.declare_parameter('publish_rate0', 100.0) # /topic0 のパブリッシュレート (Hz)
        self.declare_parameter('publish_rate1', 100.0) # /topic1 のパブリッシュレート (Hz)

        self.freq0_ = self.get_parameter('freq0').get_parameter_value().double_value
        self.freq1_ = self.get_parameter('freq1').get_parameter_value().double_value
        publish_rate0 = self.get_parameter('publish_rate0').get_parameter_value().double_value
        publish_rate1 = self.get_parameter('publish_rate1').get_parameter_value().double_value

        # パブリッシャーの作成
        self.publisher0_ = self.create_publisher(Float64, '/sat_model/joint0', 10)
        self.publisher1_ = self.create_publisher(Float64, '/sat_model/joint1', 10)

        # パブリッシュ周期に応じたタイマーの作成
        self.timer0_ = self.create_timer(1.0 / publish_rate0, self.timer0_callback)
        self.timer1_ = self.create_timer(1.0 / publish_rate1, self.timer1_callback)

        self.start_time_ = time.time()
        self.get_logger().info(
            f"正弦波パブリッシャーを起動しました。\n"
            f"/topic0: 正弦波周波数 = {self.freq0_} Hz, パブリッシュレート = {publish_rate0} Hz\n"
            f"/topic1: 正弦波周波数 = {self.freq1_} Hz, パブリッシュレート = {publish_rate1} Hz"
        )

    def timer0_callback(self):
        """
        /topic0 に正弦波をパブリッシュするコールバック関数
        """
        msg = Float64()
        elapsed_time = time.time() - self.start_time_
        msg.data = math.cos(2 * math.pi * self.freq0_ * elapsed_time)
        self.publisher0_.publish(msg)

    def timer1_callback(self):
        """
        /topic1 に正弦波をパブリッシュするコールバック関数
        """
        msg = Float64()
        elapsed_time = time.time() - self.start_time_
        msg.data = math.cos(2 * math.pi * self.freq1_ * elapsed_time)
        self.publisher1_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    sine_wave_publisher = SineWavePublisher()
    try:
        rclpy.spin(sine_wave_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        # ノードの破棄
        sine_wave_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()