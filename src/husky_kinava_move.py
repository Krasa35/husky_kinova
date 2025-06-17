
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import csv
import argparse
import time


class CSVCommandPublisher(Node):
    def __init__(self, csv_file, husky_topic, kinova_topic):
        super().__init__('csv_command_publisher')
        self.csv_file = csv_file
        self.husky_topic = husky_topic
        self.kinova_topic = kinova_topic

        self.husky_pub = self.create_publisher(Twist, self.husky_topic, 10)
        self.kinova_pub = self.create_publisher(JointTrajectory, self.kinova_topic, 10)

    def publish_commands(self):
        with open(self.csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Publikacja dla Husky
                twist = Twist()
                twist.linear.x = float(row['husky_linear_x'])
                twist.angular.z = 0.0  # angular_z usunięty
                self.husky_pub.publish(twist)

                # Publikacja dla Kinovy
                pitch_deg = float(row['pitch'])  # Wartość pitch w stopniach
                pitch_rad = pitch_deg #* 3.14159 / 180.0

                traj_msg = JointTrajectory()
                traj_msg.joint_names = [
                    'arm_0_joint_1', 'arm_0_joint_2', 'arm_0_joint_3',
                    'arm_0_joint_4', 'arm_0_joint_5', 'arm_0_joint_6', 'arm_0_joint_7'
                ]
                point = JointTrajectoryPoint()
                point.positions = [0.0, pitch_rad / 2.0, -pitch_rad / 2.0, 0.0, 0.0, 0.0, 0.0]
                point.velocities = [0.0] * 7
                point.time_from_start.sec = 1
                point.time_from_start.nanosec = 0
                traj_msg.points.append(point)

                self.kinova_pub.publish(traj_msg)

                time.sleep(0.1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', required=True, help='Path to CSV file')
    parser.add_argument('--husky-topic', required=True, help='Topic to publish Husky Twist messages')
    parser.add_argument('--kinova-topic', required=True, help='Topic to publish Kinova JointTrajectory messages')
    args = parser.parse_args()

    rclpy.init()
    node = CSVCommandPublisher(args.csv, args.husky_topic, args.kinova_topic)
    node.publish_commands()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

