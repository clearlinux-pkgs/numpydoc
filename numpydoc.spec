#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpydoc
Version  : 1.1.0
Release  : 30
URL      : https://files.pythonhosted.org/packages/3d/fb/a70f636102045fc646656f2221c7fcdf92f7a9d71ba7c9875a949a58b3e8/numpydoc-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/fb/a70f636102045fc646656f2221c7fcdf92f7a9d71ba7c9875a949a58b3e8/numpydoc-1.1.0.tar.gz
Summary  : Sphinx extension to support docstrings in Numpy format
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
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
Provides: pypi(numpydoc)
Requires: pypi(jinja2)
Requires: pypi(sphinx)

%description python3
python3 components for the numpydoc package.


%prep
%setup -q -n numpydoc-1.1.0
cd %{_builddir}/numpydoc-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593712414
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpydoc
cp %{_builddir}/numpydoc-1.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpydoc/df4f727b25238b8a4be050714fe3f1cb06b17f75
cp %{_builddir}/numpydoc-1.1.0/doc/scipy-sphinx-theme/LICENSE.txt %{buildroot}/usr/share/package-licenses/numpydoc/fd2e79f66abba5b94347c2df9ca6cf3584b0c517
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpydoc/df4f727b25238b8a4be050714fe3f1cb06b17f75
/usr/share/package-licenses/numpydoc/fd2e79f66abba5b94347c2df9ca6cf3584b0c517

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
