Name:           maven-war-plugin
Version:        2.3
Release:        8%{?dist}
Summary:        Maven WAR Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-war-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils
BuildRequires: java-devel >= 1:1.6.0
# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-changes-plugin
# Others
BuildRequires: xstream


Provides:       maven2-plugin-war = 0:%{version}-%{release}
Obsoletes:      maven2-plugin-war <= 0:2.0.8

%description
Builds a Web Application Archive (WAR) file from the project output and its 
dependencies.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.3-8
- Migrate away from mvn-rpmbuild (Resolves: #997493)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-6
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 28 2013 Weinan Li <weli@redhat.com> 2.3-5
- Remove unnecessary maven-doxia dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Weinan Li <weli@redhat.com> 2.3-2
- Install license files

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 5 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2-1
- Update to latest release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-4
- Do not depend on maven2.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-2
- Build with maven 3.
- Drop depmap and other non needed parts.

* Sat Nov 20 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1
- Update to new version.

* Mon Jun 14 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1-0.3.b1
- Fix unversioned symlink.

* Mon Jun 7 2010 Weinan Li <weli@redhat.com> - 2.1-0.2.b1
- Fix incoherent version in changelog

* Thu Jun 3 2010 Weinan Li <weli@redhat.com> - 2.1-0.1.b1
- Initial Package
