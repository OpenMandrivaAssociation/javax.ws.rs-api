Name:		javax.ws.rs-api
Version:	2.1.1
Release:	1
Summary:	JAX-RS 2.1 API
Group:		Development/Java
License:	(EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND Apache-2.0
URL:		https://projects.eclipse.org/projects/ee4j.jaxrs
Source0:	https://repo1.maven.org/maven2/javax/ws/rs/javax.ws.rs-api/%{version}/javax.ws.rs-api-%{version}-sources.jar
Source1:	https://raw.githubusercontent.com/eclipse-ee4j/jaxrs-api/2.1.1/LICENSE.md#/javax.ws.rs-api-%{version}-LICENSE.md
Source2:	https://raw.githubusercontent.com/eclipse-ee4j/jaxrs-api/2.1.1/NOTICE.md#/javax.ws.rs-api-%{version}-NOTICE.md

BuildArch:	noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	mvn(javax.xml.bind:jaxb-api)
# jaxb-api 2.4 inherits the activation version from this parent POM.
BuildRequires:	mvn(javax.xml.bind:jaxb-api-parent:pom::)
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
JAX-RS 2.1 API. This is the last release of javax.ws.rs:javax.ws.rs-api.
The client, container, and SSE packages are the types OSGi JAX-RS 1.0
imports. Link.JaxbAdapter and Link.JaxbLink reference javax.xml.bind
from the system JAXB API. module-info.java requires java.xml.bind,
which is not in the current JDK, so this build targets Java 8 and
records java.ws.rs as an automatic module. GenericEntity is
Apache-2.0. The other sources are EPL-2.0 or GPL-2.0 with the
Classpath exception.

%prep
%setup -q -c -T
# The builders' rpmuncompress passes a sources jar to tar.
python - %{SOURCE0} <<'PY'
import sys
import zipfile
zipfile.ZipFile(sys.argv[1]).extractall(".")
PY
rm -rf META-INF
cp -p %{SOURCE1} LICENSE.md
cp -p %{SOURCE2} NOTICE.md
python - <<'PY'
from pathlib import Path
module = Path("module-info.java")
text = module.read_text(encoding="utf-8")
if "module java.ws.rs" not in text or "java.xml.bind" not in text:
    raise SystemExit("module-info changed")
module.unlink()
root = Path("src/main/java")
root.mkdir(parents=True)
Path("javax").rename(root / "javax")
javas = sorted(path.relative_to(root).as_posix() for path in root.rglob("*.java"))
expected = [
    "javax/ws/rs/ApplicationPath.java",
    "javax/ws/rs/BadRequestException.java",
    "javax/ws/rs/BeanParam.java",
    "javax/ws/rs/ClientErrorException.java",
    "javax/ws/rs/ConstrainedTo.java",
    "javax/ws/rs/Consumes.java",
    "javax/ws/rs/CookieParam.java",
    "javax/ws/rs/DELETE.java",
    "javax/ws/rs/DefaultValue.java",
    "javax/ws/rs/Encoded.java",
    "javax/ws/rs/ForbiddenException.java",
    "javax/ws/rs/FormParam.java",
    "javax/ws/rs/GET.java",
    "javax/ws/rs/HEAD.java",
    "javax/ws/rs/HeaderParam.java",
    "javax/ws/rs/HttpMethod.java",
    "javax/ws/rs/InternalServerErrorException.java",
    "javax/ws/rs/MatrixParam.java",
    "javax/ws/rs/NameBinding.java",
    "javax/ws/rs/NotAcceptableException.java",
    "javax/ws/rs/NotAllowedException.java",
    "javax/ws/rs/NotAuthorizedException.java",
    "javax/ws/rs/NotFoundException.java",
    "javax/ws/rs/NotSupportedException.java",
    "javax/ws/rs/OPTIONS.java",
    "javax/ws/rs/PATCH.java",
    "javax/ws/rs/POST.java",
    "javax/ws/rs/PUT.java",
    "javax/ws/rs/Path.java",
    "javax/ws/rs/PathParam.java",
    "javax/ws/rs/Priorities.java",
    "javax/ws/rs/ProcessingException.java",
    "javax/ws/rs/Produces.java",
    "javax/ws/rs/QueryParam.java",
    "javax/ws/rs/RedirectionException.java",
    "javax/ws/rs/RuntimeType.java",
    "javax/ws/rs/ServerErrorException.java",
    "javax/ws/rs/ServiceUnavailableException.java",
    "javax/ws/rs/WebApplicationException.java",
    "javax/ws/rs/client/AsyncInvoker.java",
    "javax/ws/rs/client/Client.java",
    "javax/ws/rs/client/ClientBuilder.java",
    "javax/ws/rs/client/ClientRequestContext.java",
    "javax/ws/rs/client/ClientRequestFilter.java",
    "javax/ws/rs/client/ClientResponseContext.java",
    "javax/ws/rs/client/ClientResponseFilter.java",
    "javax/ws/rs/client/CompletionStageRxInvoker.java",
    "javax/ws/rs/client/Entity.java",
    "javax/ws/rs/client/FactoryFinder.java",
    "javax/ws/rs/client/Invocation.java",
    "javax/ws/rs/client/InvocationCallback.java",
    "javax/ws/rs/client/ResponseProcessingException.java",
    "javax/ws/rs/client/RxInvoker.java",
    "javax/ws/rs/client/RxInvokerProvider.java",
    "javax/ws/rs/client/SyncInvoker.java",
    "javax/ws/rs/client/WebTarget.java",
    "javax/ws/rs/client/package-info.java",
    "javax/ws/rs/container/AsyncResponse.java",
    "javax/ws/rs/container/CompletionCallback.java",
    "javax/ws/rs/container/ConnectionCallback.java",
    "javax/ws/rs/container/ContainerRequestContext.java",
    "javax/ws/rs/container/ContainerRequestFilter.java",
    "javax/ws/rs/container/ContainerResponseContext.java",
    "javax/ws/rs/container/ContainerResponseFilter.java",
    "javax/ws/rs/container/DynamicFeature.java",
    "javax/ws/rs/container/PreMatching.java",
    "javax/ws/rs/container/ResourceContext.java",
    "javax/ws/rs/container/ResourceInfo.java",
    "javax/ws/rs/container/Suspended.java",
    "javax/ws/rs/container/TimeoutHandler.java",
    "javax/ws/rs/container/package-info.java",
    "javax/ws/rs/core/AbstractMultivaluedMap.java",
    "javax/ws/rs/core/Application.java",
    "javax/ws/rs/core/CacheControl.java",
    "javax/ws/rs/core/Configurable.java",
    "javax/ws/rs/core/Configuration.java",
    "javax/ws/rs/core/Context.java",
    "javax/ws/rs/core/Cookie.java",
    "javax/ws/rs/core/EntityTag.java",
    "javax/ws/rs/core/Feature.java",
    "javax/ws/rs/core/FeatureContext.java",
    "javax/ws/rs/core/Form.java",
    "javax/ws/rs/core/GenericEntity.java",
    "javax/ws/rs/core/GenericType.java",
    "javax/ws/rs/core/HttpHeaders.java",
    "javax/ws/rs/core/Link.java",
    "javax/ws/rs/core/MediaType.java",
    "javax/ws/rs/core/MultivaluedHashMap.java",
    "javax/ws/rs/core/MultivaluedMap.java",
    "javax/ws/rs/core/NewCookie.java",
    "javax/ws/rs/core/NoContentException.java",
    "javax/ws/rs/core/PathSegment.java",
    "javax/ws/rs/core/Request.java",
    "javax/ws/rs/core/Response.java",
    "javax/ws/rs/core/SecurityContext.java",
    "javax/ws/rs/core/StreamingOutput.java",
    "javax/ws/rs/core/UriBuilder.java",
    "javax/ws/rs/core/UriBuilderException.java",
    "javax/ws/rs/core/UriInfo.java",
    "javax/ws/rs/core/Variant.java",
    "javax/ws/rs/core/package-info.java",
    "javax/ws/rs/ext/ContextResolver.java",
    "javax/ws/rs/ext/ExceptionMapper.java",
    "javax/ws/rs/ext/FactoryFinder.java",
    "javax/ws/rs/ext/InterceptorContext.java",
    "javax/ws/rs/ext/MessageBodyReader.java",
    "javax/ws/rs/ext/MessageBodyWriter.java",
    "javax/ws/rs/ext/ParamConverter.java",
    "javax/ws/rs/ext/ParamConverterProvider.java",
    "javax/ws/rs/ext/Provider.java",
    "javax/ws/rs/ext/Providers.java",
    "javax/ws/rs/ext/ReaderInterceptor.java",
    "javax/ws/rs/ext/ReaderInterceptorContext.java",
    "javax/ws/rs/ext/RuntimeDelegate.java",
    "javax/ws/rs/ext/WriterInterceptor.java",
    "javax/ws/rs/ext/WriterInterceptorContext.java",
    "javax/ws/rs/ext/package-info.java",
    "javax/ws/rs/package-info.java",
    "javax/ws/rs/sse/FactoryFinder.java",
    "javax/ws/rs/sse/InboundSseEvent.java",
    "javax/ws/rs/sse/OutboundSseEvent.java",
    "javax/ws/rs/sse/Sse.java",
    "javax/ws/rs/sse/SseBroadcaster.java",
    "javax/ws/rs/sse/SseEvent.java",
    "javax/ws/rs/sse/SseEventSink.java",
    "javax/ws/rs/sse/SseEventSource.java",
    "javax/ws/rs/sse/package-info.java",
]
if javas != expected:
    raise SystemExit("java files changed")
if list(Path(".").rglob("module-info.java")) or list(Path(".").rglob("*.class")):
    raise SystemExit("unexpected input")
license_text = Path("LICENSE.md").read_text(encoding="utf-8")
if "Eclipse Public License" not in license_text or "CLASSPATH EXCEPTION" not in license_text:
    raise SystemExit("LICENSE is not the EPL-2.0 and Classpath pair")
notice = Path("NOTICE.md").read_text(encoding="utf-8")
if "EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0" not in notice:
    raise SystemExit("NOTICE license changed")
header = (root / "javax/ws/rs/core/Response.java").read_text(encoding="utf-8")
if "SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0" not in header:
    raise SystemExit("source license header changed")
generic = (root / "javax/ws/rs/core/GenericEntity.java").read_text(encoding="utf-8")
if "Apache License, Version 2.0" not in generic:
    raise SystemExit("GenericEntity license changed")

Path("pom.xml").write_text('''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>javax.ws.rs</groupId>
  <artifactId>javax.ws.rs-api</artifactId>
  <version>%{version}</version>
  <packaging>jar</packaging>
  <name>JAX-RS API</name>
  <description>JAX-RS %{version}, packaged without a parent POM.</description>
  <url>https://projects.eclipse.org/projects/ee4j.jaxrs</url>
  <licenses>
    <license>
      <name>EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0</name>
      <url>https://www.eclipse.org/legal/epl-2.0</url>
    </license>
    <license>
      <name>Apache-2.0</name>
      <url>https://www.apache.org/licenses/LICENSE-2.0</url>
    </license>
  </licenses>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.release>8</maven.compiler.release>
  </properties>
  <dependencies>
    <dependency>
      <groupId>javax.xml.bind</groupId>
      <artifactId>jaxb-api</artifactId>
      <version>2.4.0.b180830.0359</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.12.1</version>
        <configuration>
          <release>8</release>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.3.0</version>
        <configuration>
          <archive>
            <manifestEntries>
              <Automatic-Module-Name>java.ws.rs</Automatic-Module-Name>
              <Specification-Version>2.1</Specification-Version>
              <Implementation-Version>%{version}</Implementation-Version>
            </manifestEntries>
          </archive>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
''', encoding="utf-8")
pom = Path("pom.xml").read_text(encoding="utf-8")
for needle in (
    "<artifactId>javax.ws.rs-api</artifactId>",
    "<artifactId>jaxb-api</artifactId>",
    "<version>%{version}</version>",
    "<version>2.4.0.b180830.0359</version>",
    "<release>8</release>",
    "java.ws.rs",
    "</project.build.sourceEncoding>",
):
    if needle not in pom:
        raise SystemExit("pom missing " + needle)
if pom.count("<version>2.1.1</version>") != 1 or pom.count("<version>2.4.0.b180830.0359</version>") != 1 or pom.count("<scope>provided</scope>") != 0:
    raise SystemExit("pom versions changed")
for needle in (
    "junit",
    "SNAPSHOT",
    "<source>",
    "<target>",
    "<parent>",
    "felix",
    "maven-bundle-plugin",
    "<version>2.1</version>",
    "projectbuild.sourceEncoding",
    "<groupId>org.eclipse.ee4j</groupId>",
):
    if needle in pom:
        raise SystemExit("pom still contains " + needle)
PY

%build -a
java --module-path target/javax.ws.rs-api-%{version}.jar --describe-module java.ws.rs > module-describe.txt
grep -q '^java\.ws\.rs@' module-describe.txt || { cat module-describe.txt; exit 1; }
grep -q ' automatic$' module-describe.txt || { cat module-describe.txt; exit 1; }
python - <<'PY'
import zipfile
from pathlib import Path
jar = Path("target/javax.ws.rs-api-%{version}.jar")
with zipfile.ZipFile(jar) as zf:
    classes = {name for name in zf.namelist() if name.endswith(".class")}
    required = {
        "javax/ws/rs/ApplicationPath.class",
        "javax/ws/rs/BadRequestException.class",
        "javax/ws/rs/BeanParam.class",
        "javax/ws/rs/ClientErrorException.class",
        "javax/ws/rs/ConstrainedTo.class",
        "javax/ws/rs/Consumes.class",
        "javax/ws/rs/CookieParam.class",
        "javax/ws/rs/DELETE.class",
        "javax/ws/rs/DefaultValue.class",
        "javax/ws/rs/Encoded.class",
        "javax/ws/rs/ForbiddenException.class",
        "javax/ws/rs/FormParam.class",
        "javax/ws/rs/GET.class",
        "javax/ws/rs/HEAD.class",
        "javax/ws/rs/HeaderParam.class",
        "javax/ws/rs/HttpMethod.class",
        "javax/ws/rs/InternalServerErrorException.class",
        "javax/ws/rs/MatrixParam.class",
        "javax/ws/rs/NameBinding.class",
        "javax/ws/rs/NotAcceptableException.class",
        "javax/ws/rs/NotAllowedException.class",
        "javax/ws/rs/NotAuthorizedException.class",
        "javax/ws/rs/NotFoundException.class",
        "javax/ws/rs/NotSupportedException.class",
        "javax/ws/rs/OPTIONS.class",
        "javax/ws/rs/PATCH.class",
        "javax/ws/rs/POST.class",
        "javax/ws/rs/PUT.class",
        "javax/ws/rs/Path.class",
        "javax/ws/rs/PathParam.class",
        "javax/ws/rs/Priorities.class",
        "javax/ws/rs/ProcessingException.class",
        "javax/ws/rs/Produces.class",
        "javax/ws/rs/QueryParam.class",
        "javax/ws/rs/RedirectionException.class",
        "javax/ws/rs/RuntimeType.class",
        "javax/ws/rs/ServerErrorException.class",
        "javax/ws/rs/ServiceUnavailableException.class",
        "javax/ws/rs/WebApplicationException.class",
        "javax/ws/rs/client/AsyncInvoker.class",
        "javax/ws/rs/client/Client.class",
        "javax/ws/rs/client/ClientBuilder.class",
        "javax/ws/rs/client/ClientRequestContext.class",
        "javax/ws/rs/client/ClientRequestFilter.class",
        "javax/ws/rs/client/ClientResponseContext.class",
        "javax/ws/rs/client/ClientResponseFilter.class",
        "javax/ws/rs/client/CompletionStageRxInvoker.class",
        "javax/ws/rs/client/Entity.class",
        "javax/ws/rs/client/FactoryFinder.class",
        "javax/ws/rs/client/Invocation$Builder.class",
        "javax/ws/rs/client/Invocation.class",
        "javax/ws/rs/client/InvocationCallback.class",
        "javax/ws/rs/client/ResponseProcessingException.class",
        "javax/ws/rs/client/RxInvoker.class",
        "javax/ws/rs/client/RxInvokerProvider.class",
        "javax/ws/rs/client/SyncInvoker.class",
        "javax/ws/rs/client/WebTarget.class",
        "javax/ws/rs/container/AsyncResponse.class",
        "javax/ws/rs/container/CompletionCallback.class",
        "javax/ws/rs/container/ConnectionCallback.class",
        "javax/ws/rs/container/ContainerRequestContext.class",
        "javax/ws/rs/container/ContainerRequestFilter.class",
        "javax/ws/rs/container/ContainerResponseContext.class",
        "javax/ws/rs/container/ContainerResponseFilter.class",
        "javax/ws/rs/container/DynamicFeature.class",
        "javax/ws/rs/container/PreMatching.class",
        "javax/ws/rs/container/ResourceContext.class",
        "javax/ws/rs/container/ResourceInfo.class",
        "javax/ws/rs/container/Suspended.class",
        "javax/ws/rs/container/TimeoutHandler.class",
        "javax/ws/rs/core/AbstractMultivaluedMap.class",
        "javax/ws/rs/core/Application.class",
        "javax/ws/rs/core/CacheControl.class",
        "javax/ws/rs/core/Configurable.class",
        "javax/ws/rs/core/Configuration.class",
        "javax/ws/rs/core/Context.class",
        "javax/ws/rs/core/Cookie.class",
        "javax/ws/rs/core/EntityTag.class",
        "javax/ws/rs/core/Feature.class",
        "javax/ws/rs/core/FeatureContext.class",
        "javax/ws/rs/core/Form$1.class",
        "javax/ws/rs/core/Form.class",
        "javax/ws/rs/core/GenericEntity.class",
        "javax/ws/rs/core/GenericType.class",
        "javax/ws/rs/core/HttpHeaders.class",
        "javax/ws/rs/core/Link$Builder.class",
        "javax/ws/rs/core/Link$JaxbAdapter.class",
        "javax/ws/rs/core/Link$JaxbLink.class",
        "javax/ws/rs/core/Link.class",
        "javax/ws/rs/core/MediaType$1.class",
        "javax/ws/rs/core/MediaType$2.class",
        "javax/ws/rs/core/MediaType.class",
        "javax/ws/rs/core/MultivaluedHashMap.class",
        "javax/ws/rs/core/MultivaluedMap.class",
        "javax/ws/rs/core/NewCookie.class",
        "javax/ws/rs/core/NoContentException.class",
        "javax/ws/rs/core/PathSegment.class",
        "javax/ws/rs/core/Request.class",
        "javax/ws/rs/core/Response$ResponseBuilder.class",
        "javax/ws/rs/core/Response$Status$Family.class",
        "javax/ws/rs/core/Response$Status.class",
        "javax/ws/rs/core/Response$StatusType.class",
        "javax/ws/rs/core/Response.class",
        "javax/ws/rs/core/SecurityContext.class",
        "javax/ws/rs/core/StreamingOutput.class",
        "javax/ws/rs/core/UriBuilder.class",
        "javax/ws/rs/core/UriBuilderException.class",
        "javax/ws/rs/core/UriInfo.class",
        "javax/ws/rs/core/Variant$VariantListBuilder.class",
        "javax/ws/rs/core/Variant.class",
        "javax/ws/rs/ext/ContextResolver.class",
        "javax/ws/rs/ext/ExceptionMapper.class",
        "javax/ws/rs/ext/FactoryFinder.class",
        "javax/ws/rs/ext/InterceptorContext.class",
        "javax/ws/rs/ext/MessageBodyReader.class",
        "javax/ws/rs/ext/MessageBodyWriter.class",
        "javax/ws/rs/ext/ParamConverter$Lazy.class",
        "javax/ws/rs/ext/ParamConverter.class",
        "javax/ws/rs/ext/ParamConverterProvider.class",
        "javax/ws/rs/ext/Provider.class",
        "javax/ws/rs/ext/Providers.class",
        "javax/ws/rs/ext/ReaderInterceptor.class",
        "javax/ws/rs/ext/ReaderInterceptorContext.class",
        "javax/ws/rs/ext/RuntimeDelegate$HeaderDelegate.class",
        "javax/ws/rs/ext/RuntimeDelegate.class",
        "javax/ws/rs/ext/WriterInterceptor.class",
        "javax/ws/rs/ext/WriterInterceptorContext.class",
        "javax/ws/rs/sse/FactoryFinder.class",
        "javax/ws/rs/sse/InboundSseEvent.class",
        "javax/ws/rs/sse/OutboundSseEvent$Builder.class",
        "javax/ws/rs/sse/OutboundSseEvent.class",
        "javax/ws/rs/sse/Sse.class",
        "javax/ws/rs/sse/SseBroadcaster.class",
        "javax/ws/rs/sse/SseEvent.class",
        "javax/ws/rs/sse/SseEventSink.class",
        "javax/ws/rs/sse/SseEventSource$Builder.class",
        "javax/ws/rs/sse/SseEventSource.class",
    }
    allowed = {
        "javax/ws/rs/package-info.class",
        "javax/ws/rs/client/package-info.class",
        "javax/ws/rs/container/package-info.class",
        "javax/ws/rs/core/package-info.class",
        "javax/ws/rs/ext/package-info.class",
        "javax/ws/rs/sse/package-info.class",
    }
    extra = classes - required
    missing = required - classes
    if missing or extra - allowed:
        raise SystemExit("class set " + " ".join(sorted(missing | (extra - allowed))))
    adapter = zf.read("javax/ws/rs/core/Link$JaxbAdapter.class")
    if b"javax/xml/bind/annotation/adapters/XmlAdapter" not in adapter:
        raise SystemExit("JAXB adapter lost XmlAdapter")
    link = zf.read("javax/ws/rs/core/Link$JaxbLink.class")
    if b"javax/xml/bind/annotation/XmlAnyAttribute" not in link or b"javax/xml/bind/annotation/XmlAttribute" not in link:
        raise SystemExit("JAXB link lost an annotation")
    if any(b"jakarta/ws/rs/" in zf.read(name) for name in classes):
        raise SystemExit("jakarta type appeared")
    if any(name.startswith("module-info") for name in zf.namelist()):
        raise SystemExit("module-info was compiled")
PY

%files -f .mfiles
%doc LICENSE.md NOTICE.md
