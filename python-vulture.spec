%bcond_without python3

%global module_name vulture
%global common_desc \
Vulture finds unused classes, functions and variables in your code. \
This helps you cleanup and find errors in your programs. If you run it \
on both your library and test suite you can find untested code. \
Due to Python’s dynamic nature, static code analyzers like vulture \
are likely to miss some dead code. Also, code that is only called \
implicitly may be reported as unused. Nonetheless, vulture can be a \
very helpful tool for higher code quality.

Name:		python-%{module_name}
Version:	0.14
Release:	1%{?dist}
Summary:	Find Dead Code

License:	MIT
URL:		https://pypi.python.org/pypi/vulture
Source0:	https://files.pythonhosted.org/packages/source/v/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}

%package -n	python2-%{module_name}
Summary:	Find Dead Code
%{?python_provide:%python_provide python2-%{module_name}}

BuildRequires:	python2-devel
BuildRequires:	python-setuptools
# Required by tests
BuildRequires:	python2-pytest
BuildRequires:	python2-pytest-cov

Requires:	python-setuptools

%description -n	python2-%{module_name}
%{common_desc}

%if %{with python3}
%package -n	python3-%{module_name}
Summary:	Find Dead Code
%{?python_provide:%python_provide python3-%{module_name}}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
# Required by tests
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov

Requires:	python3-setuptools
%description -n	python3-%{module_name}
%{common_desc}
%endif

%prep
%autosetup -n	%{module_name}-%{version}
# Remove shebang
sed -i '1{/^#!/d}' vulture.py

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/%{module_name} %{buildroot}%{_bindir}/%{module_name}-%{python3_version}
%endif
%py2_install
mv %{buildroot}%{_bindir}/%{module_name} %{buildroot}%{_bindir}/%{module_name}-%{python2_version}

ln -s %{_bindir}/vulture-%{python3_version} %{buildroot}/%{_bindir}/vulture-3
ln -s %{_bindir}/vulture-%{python2_version} %{buildroot}/%{_bindir}/vulture-2
ln -s %{_bindir}/vulture-%{python2_version} %{buildroot}/%{_bindir}/vulture

%check
py.test-2
%if %{with python3}
py.test-3
%endif

%files -n	python2-%{module_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/%{module_name}
%{_bindir}/%{module_name}-2
%{_bindir}/%{module_name}-%{python2_version}
%{python2_sitelib}/%{module_name}.py*
%{python2_sitelib}/%{module_name}-%{version}-py?.?.egg-info

%if %{with python3}
%files -n	python3-%{module_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/%{module_name}-3
%{_bindir}/%{module_name}-%{python3_version}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{module_name}.py
%{python3_sitelib}/%{module_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue Jun 20 2017 Yatin Karel <ykarel@redhat.com> - 0.14-1
- Initial package import

