# Created by: Vidar Karlsen <vidar@karlsen.tech>
# $FreeBSD$

PORTNAME=	ub-split-map
PORTVERSION=	0.1.1
CATEGORIES=	dns python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Unbound module to dynamically map external IPs to internal

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS+=	unbound:dns/unbound python2:lang/python2

USES=		python:2

USE_PYTHON=	distutils autoplist

NO_BUILD=	yes
NO_ARCH=	yes

.include <bsd.port.mk>
