# $FreeBSD: head/security/snuffleupagus/Makefile 562288 2021-01-22 10:09:04Z jhale $

PORTNAME=	snuffleupagus
DISTVERSIONPREFIX=	v
DISTVERSION=	0.8.2
PORTREVISION=	1
CATEGORIES=	security
PKGNAMEPREFIX=	${PHP_PKGNAMEPREFIX}

MAINTAINER=	franco@opnsense.org
COMMENT=	Security module for PHP

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/../LICENSE

LIB_DEPENDS=	libpcre.so:devel/pcre

USES=		localbase:ldflags php:ext
USE_GITHUB=	yes
GH_ACCOUNT=	jvoisin
USE_PHP=	hash:build session:build

PLIST_FILES+=	etc/snuffleupagus.conf

CONFIGURE_ARGS=	--enable-snuffleupagus

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
