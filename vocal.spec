# TODO:
# - to be removed while building: libxml, libxml2, libsndfile, a lot of stupid things...
# - init scripts for every service
# - make install - should be working, but does not...
# - fs requires cpl files (?)
# - MIBy for SNMP
# - rs requires many things
Summary:	vocal - Vovida Open Communication Application Library
Summary(pl.UTF-8):	vocal - otwarta biblioteka dla aplikacji komunikacyjnych
Name:		vocal
Version:	1.5.0
Release:	0.3
License:	BSD-like (?)
Group:		Networking
Source0:	http://www.vovida.org/downloads/vocal/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	808e4866da0ed262621dd211f8f86a74
URL:		http://www.vovida.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libstdc++-static
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	libxml2-devel
BuildRequires:	openh323-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Vovida Open Communication Application Library (VOCAL) is an open
source project targeted at facilitating the adoption of VoIP in the
marketplace. VOCAL provides the development community with software
and tools needed to build new and exciting VoIP features, applications
and services. The software in VOCAL includes a SIP based Redirect
Server, Feature Server, Provisioning Server and Marshal Proxy. This is
the stable development branch of the VOCAL.

%description -l pl.UTF-8
Vovida Open Communication Application Library (VOCAL) to otwarty
projekt ukierunkowany na ułatwienie adopcji VoIP na rynku. VOCAL
udostępnia społeczności programistów oprogramowanie i narzędzia
potrzebne do tworzenia nowych i ekscytujących możliwości VoIP,
aplikacji i usług. Oprogramowanie z projektu VOCAL zawiera oparty na
SIP Redirect Server, Feature Server, Provisioning Server i Marshall
Proxy. Jest to stabilne rozwijające się odgałęzienie projektu.

%package siph323csgw
Summary:	SIP-H.323 Call Signaling Gateway
Group:		Networking

%description siph323csgw
SIP-H.323 Call Signaling Gateway.

%description siph323csgw -l pl.UTF-8
Bramka sygnalizacyjna SIP-H.323.

%package cdrserv
Summary:	CDR server
Summary(pl.UTF-8):	CDR server
Group:		Networking

%description cdrserv
CDR server.

%description cdrserv -l pl.UTF-8
CDR server.

%package heartbeat
Summary:	Heartbeat server
Summary(pl.UTF-8):	Heartbeat server
Group:		Networking

%description heartbeat
Heartbeat server.

%description heartbeat -l pl.UTF-8
Heartbeat server.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
#%{__automake}
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--with-system-libs \
	--with-openssl

# ok, but it does not build: :(
#	--with-shared-libs \

# 'make usage' to show what is possible - not everything builds at once
# Basic H.323 Gatekeeper
#%{__make} %{!?debug:CODE_OPTIMIZE=1} vocal_gk

# This makes better package:
#%{__make} CODE_OPTIMIZE=1 LDLIBS_LAST="-L%{_libdir}" all
%{__make} %{!?debug:CODE_OPTIMIZE=1} LDLIBS_LAST="-L%{_libdir} -L/usr/X11R6/lib -lxml -lsndfile" all
# SIP-H.323 Call Signaling Gateway
%{__make} %{!?debug:CODE_OPTIMIZE=1} siph323csgw
# Provisioning Server
%{__make} %{!?debug:CODE_OPTIMIZE=1} ps

%install
rm -rf $RPM_BUILD_ROOT
# We have to install it by hand - this mo......rs are doing crazy things
# while doing make install

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},/etc/vocal}

# Heartbeat:
install heartbeat/hbs/bin.opt.Linux.*/hbs $RPM_BUILD_ROOT%{_sbindir}

# cdrserv:
install cdr/cdrServer/bin.opt.Linux.*/cdrserv $RPM_BUILD_ROOT%{_sbindir}
install cdr/cdrServer/cdr.cfg $RPM_BUILD_ROOT/etc/vocal

# siph323csgw:
install translators/h323/siph323csgw/bin.opt.Linux.*/siph323csgw $RPM_BUILD_ROOT%{_sbindir}
install translators/h323/siph323csgw/siph323csgw.conf $RPM_BUILD_ROOT/etc/vocal

# Provisioning Server:
install provisioning/pserver/bin.opt.Linux.*/pserver $RPM_BUILD_ROOT%{_sbindir}
install prov/cpp/pserver/ps.cfg $RPM_BUILD_ROOT/etc/vocal

# Various:
install provisioning/conversion/bin.opt.Linux.*/* $RPM_BUILD_ROOT%{_bindir}
install proxies/fs/base/bin.opt.Linux.*/fs $RPM_BUILD_ROOT%{_sbindir}
install proxies/marshal/base/bin.opt.Linux.*/ms $RPM_BUILD_ROOT%{_sbindir}
install proxies/rs/bin.opt.Linux.*/rs $RPM_BUILD_ROOT%{_sbindir}
install rtp/bin.opt.Linux.*/codec/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/File*
%attr(755,root,root) %{_bindir}/Install*
%attr(755,root,root) %{_bindir}/Put*
%attr(755,root,root) %{_bindir}/encode
%attr(755,root,root) %{_bindir}/decode

%files siph323csgw
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/siph323csgw
%config(noreplace) /etc/vocal/siph323csgw.conf

%files cdrserv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/cdrserv
%config(noreplace) /etc/vocal/cdr.cfg

%files heartbeat
%defattr(644,root,root,755)
%doc heartbeat/hbs/README
%attr(755,root,root) %{_sbindir}/hbs

#%files fs
#%defattr(644,root,root,755)
#%doc proxies/fs/base/README
#%attr(755,root,root) %{_sbindir}/fs
