#include<ros/ros.h>
#include<std_msgs/Int32.h>

int main(int argc, char * argv[]){
    ros::init(argc, argv, "cpp_publisher");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::Int32>("topic2", 1000);
    ros::Rate loop_rate(1);

    std_msgs::Int32 number;
    number.data = 0;

    while (ros::ok())
    {
        pub.publish(number);
        ros::spinOnce();
        loop_rate.sleep();
        ++number.data;
    }
    return 0;
    
}
