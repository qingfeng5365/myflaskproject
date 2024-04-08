#!/bin/bash

# 服务列表
services=("mygunicorn" "myuwsgi" "mygunicornunix" "myuwsgiunix")

# 循环遍历每个服务并重启
for service in "${services[@]}"; do
    echo "Restarting $service service..."
    sudo systemctl restart $service.service
done

