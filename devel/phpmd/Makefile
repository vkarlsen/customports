# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	phpmd
PORTVERSION=	2.6.0
CATEGORIES=	devel
MASTER_SITES=	http://static.phpmd.org/php/${PORTVERSION}/
DISTNAME=	${PORTNAME}
EXTRACT_SUFX=	.phar

MAINTAINER=	vidar@karlsen.tech
COMMENT=	PHP Mess Detector

LICENSE=	BSD3CLAUSE

RUN_DEPENDS=	${PEAR_PKGNAMEPREFIX}pdepend-PHP_Depend>0:devel/pear-PHP_Depend@${PHP_FLAVOR}

USES=		php:build,cli pear:env shebangfix
USE_PHP=	phar
SHEBANG_FILES=	${WRKSRC}/${PORTNAME}.phar

NO_BUILD=	yes
NO_ARCH=	yes

PLIST_FILES=	bin/phpmd

do-extract:
	@${MKDIR} ${WRKSRC}/
	${CP} ${_DISTDIR}/${PORTNAME}.phar ${WRKSRC}/

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/${PORTNAME}.phar \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}

.include <bsd.port.mk>
