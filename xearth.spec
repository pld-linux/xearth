Summary:	Displays a lit globe in the background of your X screen
Summary(de):	Anzeige eines erleuchteten Globus im Hintergrund Ihres X-Bildschirms 
Summary(fr):	Affiche un globe terrestre illumin� dans le fond de votre �cran X
Summary(pl):	T�o w postaci animowanej kuli ziemskiej dla X Window System
Summary(tr):	X ekran�n�z�n arkaplan�nda bir d�nya g�r�nt�s�
Name:		xearth
Version:	1.0
Release:	13
Copyright:	MIT
Group:		X11/Amusements
Group(pl):	X11/Rozrywka
Source:		ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
Xearth displays a pseudo-3D globe that rotates to show the earth as it
actually is, including markers for major cities and PLD & RH :-).

%description -l de
Xearth stellt einen rotierenden pseudo-3D-Globus dar, auf dem
die wichtigsten St�dte und PLD & RH eingezeichnet sind:-).

%description -l fr
Xearth affiche un globe en pseudo-3D qui tourne et montre la terre telle
qu'elle est sur le moment, avec les principales villes et...
PLD & RH :-).

%description -l pl
Xearth wy�wietla pseudo-3D obracaj�c� si� w odst�pach czasowych kul� ziemska,
oraz punkty z zaznaczonymi najwi�kszymi aglomeracjami Ziemi. Pokazuje r�wnie�
gdzie znajduje si� PLD ;)

%description -l tr
xearth, d�nyan�n o saatte g�ne�e g�re durumunu ve �zerindeki belli ba�l�
�ehirleri grafik olarak g�sterir. �zellikle X ortam�nda arka plan olarak
kullan�lmas� tavsiye edilir. Bu durumda her be� dakikada bir arka plan resmi
kendisini g�ncelleyecektir.

%prep
%setup -q

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name} <<EOF
%{name} name "%{name}"
%{name} description "%{name}"
%{name} group Amusements
%{name} exec "%{name} -fork"
EOF

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

/etc/X11/wmconfig/%{name}
