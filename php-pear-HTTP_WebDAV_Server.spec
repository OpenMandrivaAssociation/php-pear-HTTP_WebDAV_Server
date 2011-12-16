%define		_class		HTTP
%define		_subclass	WebDAV
%define		upstream_name	%{_class}_%{_subclass}_Server

%define		rel		2
%define		pre		RC6
%if %pre
%define		release		%{mkrel 0.%pre.%rel}
%define		distname	%{upstream_name}-%{version}%{pre}.tgz
%define		pathname	%{upstream_name}-%{version}%{pre}
%else
%define		release		%{mkrel %rel}
%define		distname	%{upstream_name}-%{version}.tgz
%define		pathname	%{upstream_name}-%{version}
%endif

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	%{release}
Summary:	WebDAV Server Baseclass
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_WebDAV_Server/
Source0:	http://download.pear.php.net/package/%{distname}
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear-HTTP >= 1.0
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

%prep
%setup -q -c
mv package.xml %{pathname}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{pathname}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/HTTP_WebDAV_Server/AUTHORS
rm -rf %{buildroot}%{_datadir}/pear/data/HTTP_WebDAV_Server/COPYING
rm -rf %{buildroot}%{_datadir}/pear/data/HTTP_WebDAV_Server/EXPERIMENTAL
rm -rf %{buildroot}%{_datadir}/pear/data/HTTP_WebDAV_Server/TODO

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{pathname}/AUTHORS
%doc %{pathname}/COPYING
%doc %{pathname}/EXPERIMENTAL
%doc %{pathname}/TODO
%doc %{pathname}/README
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
