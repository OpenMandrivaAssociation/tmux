Summary:	Terminal multiplexer
Name:		tmux
Version:	1.8
Release:	1
License:	BSD 
Group:		Terminals
Url:		http://tmux.sourceforge.net/ 
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(ncurses)

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup -q

%build
%configure2_5x
%make

%install
install -d %{buildroot}%{_bindir}
install -m 755 tmux %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 644 tmux.1 %{buildroot}%{_mandir}/man1

%files
%doc FAQ TODO CHANGES examples/
%{_bindir}/tmux
%{_mandir}/man1/tmux.*

