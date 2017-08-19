# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	ub-split-map
PORTVERSION=	0.1.1
PORTREVISION=	1
CATEGORIES=	dns python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Unbound module to dynamically map external IPs to internal

LICENSE=	GPLv2

RUN_DEPENDS+=	unbound:dns/unbound

USES=		python

USE_GITHUB=	yes
GH_ACCOUNT=	crustymonkey

USE_PYTHON=	distutils autoplist

NO_BUILD=	yes
NO_ARCH=	yes

.include <bsd.port.mk>
