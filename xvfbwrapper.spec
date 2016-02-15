#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xvfbwrapper
Version  : 0.2.5
Release  : 11
URL      : https://pypi.python.org/packages/source/x/xvfbwrapper/xvfbwrapper-0.2.5.tar.gz
Source0  : https://pypi.python.org/packages/source/x/xvfbwrapper/xvfbwrapper-0.2.5.tar.gz
Summary  : run headless display inside X virtual framebuffer (Xvfb)
Group    : Development/Tools
License  : MIT
Requires: xvfbwrapper-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===============
xvfbwrapper
===============
Python wrapper for running a display inside X virtual framebuffer (Xvfb).  This is useful for running acceptance tests (i.e. browser-based tests) on a headless server.

%package python
Summary: python components for the xvfbwrapper package.
Group: Default

%description python
python components for the xvfbwrapper package.


%prep
%setup -q -n xvfbwrapper-0.2.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
