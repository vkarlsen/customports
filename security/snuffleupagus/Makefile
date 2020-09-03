# $FreeBSD: head/security/snuffleupagus/Makefile 505483 2019-06-30 20:29:36Z swills $

PORTNAME=	snuffleupagus
DISTVERSIONPREFIX=	v
DISTVERSION=	0.5.1
PORTREVISION=	1
CATEGORIES=	security
PKGNAMEPREFIX=	${PHP_PKGNAMEPREFIX}

MAINTAINER=	franco@opnsense.org
COMMENT=	Security module for PHP 7+

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/../LICENSE

LIB_DEPENDS=	libpcre.so:devel/pcre

USES=		localbase:ldflags php:ext
USE_GITHUB=	yes
GH_ACCOUNT=	jvoisin
USE_PHP=	hash:build session:build

PLIST_FILES+=	etc/snuffleupagus.conf

CONFIGURE_ARGS=	--enabe-snuffleupagus

TEST_TARGET=	test

# Fix build with clang11
CFLAGS+=	-fcommon

WRKSRC_SUBDIR=	src

post-install:
	${ECHO} 'sp.configuration_file=/usr/local/etc/snuffleupagus.conf' \
		>> ${STAGEDIR}${PREFIX}/etc/php/ext-30-snuffleupagus.ini
	${INSTALL_DATA} ${FILESDIR}/snuffleupagus.conf \
		${STAGEDIR}${PREFIX}/etc/snuffleupagus.conf

.include <bsd.port.mk>
