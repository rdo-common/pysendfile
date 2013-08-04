Name:           pysendfile
Version:        2.0.0
Release:        6%{?dist}
Summary:        Python interface to the sendfile(2) system call

License:        MIT
URL:            http://code.google.com/p/pysendfile/
Source0:        http://pysendfile.googlecode.com/files/pysendfile-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%{?filter_setup:
%filter_provides_in %{python_sitearch}
%filter_setup
}

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP). 

%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%check
PYTHONPATH="$RPM_BUILD_ROOT%{python_sitearch}" %{__python} test/test_sendfile.py


%files
%doc README LICENSE
%attr(755, root, root) %{python_sitearch}/sendfile.so
%{python_sitearch}/pysendfile-%{version}-*.egg-info


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 8 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-3
- Update %%check section to a more sane method of setting PYTHONPATH

* Wed Feb 8 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-2
- Remove unnecessary cleaning of the buildroot in %%install section
- Add %%check section to run the unit tests
- Rename package from python-sendfile to pysendfile

* Tue Feb 7 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-1
- Initial package
