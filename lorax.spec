Name:           lorax
Version:        0.4
Release:        1%{?dist}
Summary:        Tool for creating the anaconda install images

Group:          Applications/System
License:        GPLv2+
URL:            http://git.fedorahosted.org/git/?p=lorax.git
Source0:        https://fedorahosted.org/releases/l/o/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  python-setuptools
Requires:       python2-devel
Requires:       python-mako
Requires:       gawk
Requires:       glibc-common
Requires:       cpio
Requires:       module-init-tools
Requires:       device-mapper
Requires:       findutils
Requires:       GConf2
Requires:       isomd5sum
Requires:       glibc
Requires:       util-linux-ng
Requires:       dosfstools
Requires:       genisoimage
Requires:       parted
Requires:       pyliblzma

%ifarch i386 x86_64
Requires:       syslinux
%endif

%ifarch sparc sparc64
Requires:       silo
%endif

%description
Lorax is a tool for creating the anaconda install images.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{python_sitelib}/pylorax
%{python_sitelib}/*.egg-info
%{_sbindir}/lorax
%dir %{_sysconfdir}/lorax
%config(noreplace) %{_sysconfdir}/lorax/lorax.conf
%dir %{_datadir}/lorax
%{_datadir}/lorax/*


%changelog
* Mon Mar 14 2011 Martin Gracik <mgracik@redhat.com> 0.4-1
- Add the images-xen section to treeinfo on x86_64
- Print a message when no arguments given (#684463)
- Mako template returns unicode strings (#681003)
- The check option in options causes ValueError
- Disable all ctrl-alt-arrow metacity shortcuts
- Remove the locale-archive explicitly
- Use xz when compressing the initrd
- Keep the source files for locales and get rid of the binary form
- Add /sbin to $PATH (for the tty2 terminal)
- Create /var/run/dbus directory in installtree
- Add mkdir support to template
- gpart is present only on i386 arch (#672611)
- util-linux-ng changed to util-linux

* Mon Jan 24 2011 Martin Gracik <mgracik@redhat.com> 0.3-1
- Don't remove libmount package
- Don't create mtab symlink, already exists
- Exit with error if we have no lang-table
- Fix file logging
- Overwrite the /etc/shadow file
- Use [images-xen] section for PAE and xen kernels

* Fri Jan 14 2011 Martin Gracik <mgracik@redhat.com> 0.2-2
- Fix the gnome themes
- Add biosdevname package
- Edit .bash_history file
- Add the initrd and kernel lines to .treeinfo
- Don't remove the gamin package from installtree

* Wed Dec 01 2010 Martin Gracik <mgracik@redhat.com> 0.1-1
- First packaging of the new lorax tool.
