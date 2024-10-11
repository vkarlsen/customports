PORTNAME=	hermodr
DISTVERSION=	g20241009
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	System monitor/alerter

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	curl>0:ftp/curl

USE_GITHUB=	yes
GH_ACCOUNT=	vkarlsen
GH_TAGNAME=	c288c44

NO_ARCH=	yes
NO_BUILD=	yes

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/bin/hermodr ${STAGEDIR}${PREFIX}/bin
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/hermodr/scouts
	${INSTALL_SCRIPT} ${WRKSRC}/libexec/hermodr/common ${STAGEDIR}${PREFIX}/libexec/hermodr
	${INSTALL_SCRIPT} ${WRKSRC}/libexec/hermodr/scouts/* ${STAGEDIR}${PREFIX}/libexec/hermodr/scouts
	${INSTALL_DATA} ${WRKSRC}/etc/hermodr.conf.sample ${STAGEDIR}${PREFIX}/etc

.include <bsd.port.mk>
