# $FreeBSD$

PORTNAME=	pgbackup
PORTVERSION=	0.1
CATEGORIES=	sysutils
MASTER_SITES=	# none
DISTFILES=	# none

MAINTAINER=	vidar@karlsen.tech
COMMENT=	PostGreSQL backup script

LICENSE=	BSD2CLAUSE

NO_BUILD=	yes
NO_ARCH=	yes

do-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/pgbackups
	${INSTALL_SCRIPT} ${FILESDIR}/pgbackup ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
