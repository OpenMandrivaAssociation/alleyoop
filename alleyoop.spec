Summary:	Graphical frontend to Valgrind memory checker
Name:		alleyoop
Version:	0.9.8
Release:	3
License:	GPLv2+
Group:		Development/Other
URL:		http://alleyoop.sourceforge.net/

Source0:	https://sourceforge.net/projects/alleyoop/files/alleyoop/alleyoop-0.9.8/%{name}-%{version}.tar.gz

BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	libglade2.0-devel
BuildRequires:	valgrind
BuildRequires:	intltool
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
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %{makeinstall_std}

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

%preun
%preun_uninstall_gconf_schemas %{name}

%clean

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-2mdv2011.0
+ Revision: 609969
- rebuild

* Tue Nov 24 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.7-1mdv2010.1
+ Revision: 469788
- update to new version 0.9.7

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.5-1mdv2010.1
+ Revision: 462628
- Fix BuildRequires
- update to new version 0.9.5

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.9.4-2mdv2010.0
+ Revision: 436640
- rebuild

* Tue Feb 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.4-1mdv2009.1
+ Revision: 339243
- Update to new version 0.9.4
- Remove old and unapplied patch from svn
- Fix license
- Add URL in Source definition

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.3-1mdv2009.0
+ Revision: 218437
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 148036
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 21 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 29196
- Remove editors BuildRequires
- New release 0.9.3
- Import alleyoop



* Mon Sep 11 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.9.2-3mdv2007.0
- actually define %%{Summary}

* Mon Sep 11 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.9.2-2mdv2007.0
- fix menus (summary macro and comment breakage)

* Tue Aug 08 2006 Jerome Soyer <saispo@mandriva.org> 0.9.2-1mdv2007.0
- New release 0.9.2

* Tue Jul 11 2006 Lenny Cartier <lenny@mandriva.com> 0.9.0-2mdv2007.0
- xdg menu

* Fri Mar 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-1mdk
- new release
- patch 0: fix build on x86_64

* Fri Jul 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.2-1mdk
- 0.8.2

* Fri Dec 12 2003 Abel Cheung <deaddog@deaddog.org> 0.8.0-3mdk
- Yet another fix

* Sat Oct 25 2003 Abel Cheung <deaddog@deaddog.org> 0.8.0-2mdk
- Fix buildrequires

* Sat Oct 25 2003 Abel Cheung <deaddog@deaddog.org> 0.8.0-1mdk
- First Mandrake package

