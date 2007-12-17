%define	name	alleyoop
%define version 0.9.3
%define release %mkrel 1
%define	Summary	Graphical frontend to Valgrind memory checker

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://alleyoop.sourceforge.net/

Source0:	%{name}-%{version}.tar.bz2
Patch0:		alleyoop-0.8.2-fix-build.patch.bz2

BuildRequires:	binutils-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	valgrind
# it checks for editors
# (saispo) not needed
#BuildRequires:	emacs xemacs vim-X11
Requires(pre):	GConf2 >= 2.3.3
Requires:	valgrind

%description
Alleyoop is a graphical frontend to the Valgrind memory checker for
GNOME.

%prep
%setup -q

%build
# to guarantee that gvim can be found
export PATH="$PATH:/usr/X11R6/bin"

%configure2_5x --enable-vgstrpool=yes
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %{makeinstall_std}

mkdir -p %{buildroot}%{_menudir}

cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%name): needs="x11" \
        section="More Applications/Development/Tools" \
        title="Alleyoop memory checker" \
        longtitle="%{Summary}" \
        command="%{_bindir}/%{name}" \
        icon="development_tools_section.png" \
        startup_notify="true" \
        multiple_files="true" \
        xdg="true"
EOF


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alleyoop
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=development_tools_section
Terminal=false
Type=Application
Categories=Development;Debugger;

EOF

%find_lang %{name}

%post
%update_menus
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_menudir}/%{name}
%{_datadir}/applications/*
