# Depends on dns/py-pkb_client, but the RUN_DEPEND can't be registered
# due to its missing from dns/Makefile
PORTNAME=	certbot-dns-porkbun
PORTVERSION=	0.11.0
DISTVERSIONPREFIX=	v
CATEGORIES=	security python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Porkbun DNS Authenticator plugin for Certbot
WWW=		https://github.com/infinityofspace/certbot_dns_porkbun

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/License

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=0:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}acme>=${ACME_VERSION},1:security/py-acme@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}certbot>=${ACME_VERSION},1:security/py-certbot@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}dns-lexicon>=3.15.1:dns/py-dns-lexicon@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}setuptools>=41.6.0:devel/py-setuptools@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist concurrent pep517

USE_GITHUB=	yes
GH_ACCOUNT=	infinityofspace
GH_PROJECT=	certbot_dns_porkbun

NO_ARCH=	yes

post-patch:
	${CP} ${FILESDIR}/pyproject.toml ${WRKSRC}

.include <bsd.port.mk>
