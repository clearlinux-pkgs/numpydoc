#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEDBEA378BF1A5EBD (ralf.gommers@gmail.com)
#
Name     : numpydoc
Version  : 0.8.0
Release  : 16
URL      : https://pypi.python.org/packages/95/a8/b4706a6270f0475541c5c1ee3373c7a3b793936ec1f517f1a1dab4f896c0/numpydoc-0.8.0.tar.gz
Source0  : https://pypi.python.org/packages/95/a8/b4706a6270f0475541c5c1ee3373c7a3b793936ec1f517f1a1dab4f896c0/numpydoc-0.8.0.tar.gz
Source99 : https://pypi.python.org/packages/95/a8/b4706a6270f0475541c5c1ee3373c7a3b793936ec1f517f1a1dab4f896c0/numpydoc-0.8.0.tar.gz.asc
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
%setup -q -n numpydoc-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551026827
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
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
