import rospy
from geometry_msgs.msg import PoseStamped

pose_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

pose = PoseStamped()

pose.header.frame_id = "world"
pose.header.stamp = rospy.Time.now()
pose.pose.position.x = 9.0
pose.pose.position.y = 0.0
pose.pose.position.z = 2.5

pose.pose.orientation.x = 0
pose.pose.orientation.y = 0
pose.pose.orientation.z = 0
pose.pose.orientation.w = 1

pose_pub.publish(pose)