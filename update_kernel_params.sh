#!/bin/bash

# 更新内核启动参数
update_kernel_params() {
    # 你想要添加或修改的内核参数
    KERNEL_PARAMS="quiet splash"

    # 编辑 GRUB 配置文件
    if grep -q "GRUB_CMDLINE_LINUX" /etc/default/grub; then
        sudo sed -i "s/^GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX=\"$KERNEL_PARAMS\"/" /etc/default/grub
    else
        echo "GRUB_CMDLINE_LINUX=\"$KERNEL_PARAMS\"" | sudo tee -a /etc/default/grub
    fi

    # 重新生成 GRUB 配置
    sudo grub2-mkconfig -o /boot/grub2/grub.cfg
}

# 设置 /proc 参数
set_proc_params() {
    # 示例：设置 /proc/sys/net/ipv4/ip_forward 为 1
    echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

    # 你可以添加更多的 /proc 参数设置
    # echo value | sudo tee /proc/sys/path/to/parameter
}

# 主函数
main() {
    update_kernel_params
    set_proc_params
}

main
