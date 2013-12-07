%define _class		HTTP
%define _subclass	WebDAV
%define modname	%{_class}_%{_subclass}_Server

Summary:	WebDAV Server Baseclass
Name:		php-pear-%{modname}
Version:	0.99.1
Release:	21
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTTP_WebDAV_Server/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.0

%description
Mostly RFC2518 compliant helper class for WebDAV server
implementation.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

