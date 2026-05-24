PORTNAME=	pkb_client
PORTVERSION=	2.3.1
DISTVERSIONPREFIX=	v
CATEGORIES=	dns python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	vidar@karlsen.tech
COMMENT=	Porkbun API client
WWW=		https://github.com/infinityofspace/pkb_client

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
#GH_PROJECT=	certbot_dns_porkbun

NO_ARCH=	yes

.include <bsd.port.mk>
