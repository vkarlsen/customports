# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	yubikey_auth
PORTVERSION=	g20170801
CATEGORIES=	mail
PKGNAMEPREFIX=	roundcube-

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Roundcube yubikey auth plugin

LICENSE=	GPLv2

BUILD_DEPENDS=	roundcube>=1.0:mail/roundcube
RUN_DEPENDS=	roundcube>=1.0:mail/roundcube

USES=		php

USE_PHP=	curl

USE_GITHUB=	yes
GH_ACCOUNT=	northox
GH_PROJECT=	roundcube-yubikey-plugin
GH_TAGNAME=	52062f1

NO_BUILD=	yes
NO_ARCH=	yes

WWWDIR=		${PREFIX}/www/roundcube/plugins/yubikey_authentication

do-install:
	${MKDIR} ${STAGEDIR}${WWWDIR}
	cd ${WRKSRC} && ${PAX} -r -w . ${STAGEDIR}${WWWDIR}
	cd ${STAGEDIR}${WWWDIR} && \
		${MV} config.inc.php config.inc.php.sample

.include <bsd.port.mk>
