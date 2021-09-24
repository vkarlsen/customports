PORTNAME=	heif-image-plugin
PORTVERSION=	0.3.3
CATEGORIES=	graphics
PKGNAMEPREFIX=	qt5-

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Qt image plugin for HEIF images, wrapping libheif

LICENSE=	LGPL3

LIB_DEPENDS=	libheif.so:graphics/libheif

USES=		cmake pkgconfig qt:5
USE_QT=		core gui

USE_GITHUB=	yes
GH_ACCOUNT=	jakar
GH_PROJECT=	qt-${PORTNAME}

do-build:
	cd ${WRKSRC} && ${MKDIR} build && cd build && cmake .. && make

.include <bsd.port.mk>
