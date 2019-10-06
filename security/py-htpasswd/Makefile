# $FreeBSD$

PORTNAME=	htpasswd
PORTVERSION=	2008.03.05
PORTREVISION=	3
CATEGORIES=	security python
MASTER_SITES=	# none
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTFILES=	# none

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Replacement for htpasswd

USES=		python shebangfix

PLIST_FILES=	bin/htpasswd

NO_BUILD=	yes
NO_WRKSUBDIR=	yes

SHEBANG_FILES=	htpasswd

do-extract:
	${CP} ${FILESDIR}/htpasswd ${WRKSRC}

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/htpasswd ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
