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
	${INSTALL_PROGRAM} ${WRKSRC}/usr/bin/jotta-cli ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/usr/bin/jottad ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
