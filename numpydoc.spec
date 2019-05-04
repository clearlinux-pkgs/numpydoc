#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpydoc
Version  : 0.9.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/6a/f3/7cfe4c616e4b9fe05540256cc9c6661c052c8a4cec2915732793b36e1843/numpydoc-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6a/f3/7cfe4c616e4b9fe05540256cc9c6661c052c8a4cec2915732793b36e1843/numpydoc-0.9.1.tar.gz
Summary  : Sphinx extension to support docstrings in Numpy format
Group    : Development/Tools
License  : BSD-2-Clause
Requires: numpydoc-license = %{version}-%{release}
Requires: numpydoc-python = %{version}-%{release}
Requires: numpydoc-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Sphinx
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : pytest

%description
.. image:: https://travis-ci.org/numpy/numpydoc.png?branch=master
:target: https://travis-ci.org/numpy/numpydoc/

%package license
Summary: license components for the numpydoc package.
Group: Default

%description license
license components for the numpydoc package.


%package python
Summary: python components for the numpydoc package.
Group: Default
Requires: numpydoc-python3 = %{version}-%{release}

%description python
python components for the numpydoc package.


%package python3
Summary: python3 components for the numpydoc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the numpydoc package.


%prep
%setup -q -n numpydoc-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556990116
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpydoc
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/numpydoc/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpydoc/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
