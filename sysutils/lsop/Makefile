# Custom patch set by Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	lsop
PORTVERSION=	0.2
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Lists processes running with outdated binaries or shared libraries

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${FILESDIR}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	606u
GH_TAGNAME=	v0.2

# WRKSRC=		${WRKDIR}/${PORTNAME}-${GH_TAGNAME}

# .include <bsd.port.pre.mk>

PLIST_FILES=	sbin/lsop \
				libexec/nagios/check_restart

post-patch:
	${REINPLACE_CMD} -e 's|lsop|${PREFIX}/sbin/lsop|' ${WRKSRC}/check_restart

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/lsop ${STAGEDIR}${PREFIX}/sbin
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/nagios
	${INSTALL_SCRIPT} ${WRKSRC}/check_restart ${STAGEDIR}${PREFIX}/libexec/nagios

.include <bsd.port.mk>
