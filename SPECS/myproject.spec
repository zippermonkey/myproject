Name:           myproject
Version:        1.0
Release:        1%{?dist}
Summary:        A brief description of your project

License:        GPL
URL:            http://example.com/myproject
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires(post): systemd
Requires(preun): systemd

%description
A longer description of your project.

%prep
%setup -q

%build
# No build steps required for scripts

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system

# 安装脚本
install -m 755 %{_builddir}/%{name}-%{version}/update_kernel_params.sh $RPM_BUILD_ROOT/usr/local/bin/update_kernel_params.sh
# 安装 systemd 服务文件
install -m 644 update-proc-params.service $RPM_BUILD_ROOT/etc/systemd/system/update-proc-params.service

%post
# 重新加载 systemd 配置并启用服务
systemctl daemon-reload
systemctl enable update-proc-params.service
systemctl start update-proc-params.service

%preun
if [ $1 -eq 0 ]; then
    # 停止并禁用服务
    systemctl stop update-proc-params.service
    systemctl disable update-proc-params.service
fi

%files
/usr/local/bin/update_kernel_params.sh
/etc/systemd/system/update-proc-params.service

%changelog
* Thu Jun 24 2021 Your Name <you@example.com> - 1.0-1
- Initial package
