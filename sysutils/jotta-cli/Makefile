PORTNAME=		jotta-cli
DISTVERSION=		0.11.44593
DISTVERSIONSUFFIX=	_freebsd_amd64
CATEGORIES=		sysutils
MASTER_SITES=		https://repo.jotta.us/archives/freebsd/amd64/

MAINTAINER=		vidar@karlsen.tech
COMMENT=		Jottacloud Command-line Tool

NO_BUILD=		yes
NO_WRKSUBDIR=		yes

PLIST_FILES=		bin/jotta-cli \
			bin/jottad

do-install:
	${CP} ${WRKSRC}/usr/bin/* ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
