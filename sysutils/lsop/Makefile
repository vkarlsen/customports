# Created by: Vidar Karlsen <vidar@karlsen.tech> (custom patch set)
# $FreeBSD$

PORTNAME=	lsop
PORTVERSION=	0.2
DISTVERSIONPREFIX=	v
PORTREVISION=	1
CATEGORIES=	sysutils

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Lists processes running with outdated binaries or shared libraries

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	606u

PLIST_FILES=	sbin/lsop \
		libexec/nagios/check_restart

post-patch:
	${REINPLACE_CMD} -e 's|lsop|${PREFIX}/sbin/lsop|' ${WRKSRC}/check_restart

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/lsop ${STAGEDIR}${PREFIX}/sbin
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/nagios
	${INSTALL_SCRIPT} ${WRKSRC}/check_restart ${STAGEDIR}${PREFIX}/libexec/nagios

.include <bsd.port.mk>
