# TODO:
# - to be removed while building:
#	- libxml2
#	- a lot of stupid things...
Summary:	vocal
Summary(pl):	vocal
Name:		vocal
Version:	1.5.0
Release:	0.1
License:	?
Group:		Libraries
Source0:	http://www.vovida.org/downloads/vocal/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.vovida.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	openh323-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Vovida Open Communication Application Library (VOCAL) is an open
source project targeted at facilitating the adoption of VoIP in the
marketplace. VOCAL provides the development community with software
and tools needed to build new and exciting VoIP features, applications
and services. The software in VOCAL includes a SIP based Redirect
Server, Feature Server, Provisioning Server and Marshal Proxy. This is
the stable development branch of the VOCAL


%package devel
Summary:	Vocal development files
Summary(pl):	Pliki dla programistów używających Vocal
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Vocal development files.

%description devel -l pl
Pliki dla programistów używających Vocal.

%package static
Summary:	Vocal - static version
Summary(pl):	Statyczna wersja Vocal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Vocal - static version.

%description static -l pl
Statyczna wersja Vocal.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
#%{__automake}
%configure \
#	--%{?debug:en}%{!?debug:dis}able-debug

# ok, but it does not build: :(
#	--with-shared-libs \
#	--with-system-libs \

# We are making this f****ng huge pig step by step
# 'make usage' to show what is possible

# SIP-H.323 Call Signaling Gateway
#%{__make} siph323csgw
# Provisioning Server
#%{__make} ps
# Basic H.323 Gatekeeper
#%{__make} vocal_gk

%{__make} LDLIBS_LAST="-L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
#%doc AUTHORS BUGS ChangeLog NEWS README TODO
#%attr(755,root,root) %{_libdir}/lib*.la
#%attr(755,root,root) %{_libdir}/lib*.so
#%{_includedir}/*

%files static
%defattr(644,root,root,755)
#%{_libdir}/lib*.a
