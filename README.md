#   TUTORIAL FROM KINOVA [README](https://github.com/Kinovarobotics/ros2_kortex/blob/main/README.md)
This README provides info how to get kinova with husky sim for set-up.

1.  Make sure you have Docker and VSCode installed properly.
1.  Make sure your Docker can be run by normal user - check this in VSCode terminal - if needed use this [Tutorial](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
1.  Download Extensions for your VSCode: ms-vscode-remote.remote-containers
1.  Open folder cloned from this git repo in 
    VSCode
> [!WARNING]
> To clone this repo properly (it uses submodules) run below command:
> 
>```
>git clone --recurse-submodules -j8 https:/github.com/Krasa35/husky_kinova.git
>```
1.  Make sure if your Display is connected properly... (should be okay on native linux - if not look in `devcontainer.json`)
1.  Press CTRL+SHIFT+P
1.  Choose Dev Container: Rebuild and open in container
1.  Make sure you compiled `colcon build` and sourced all packages `. /home/ws/install/setup.sh`
1.  To run Simulation with predefined `robot.yaml` file make directory that main package reads from, and copy predefined configuration file there
    ```
    mkdir /home/ros2/clearpath
    cp _resources/robot.yaml /home/ros2/clearpath/robot.yaml
    ```
1.  To start simulation run, something is not okay with rviz - if you change arg to true, it will not work
    ```
    ros2 launch clearpath_gz simulation.launch.py rviz:=false
    ```
1.  To control the robot from right pane please ensure sim is started - run button on bottom left corner and correct topic is selected, thus namespace is declared in `robot.yaml` file we need to set it to `/a200_0000/cmd_vel` not `/cmd_vel`