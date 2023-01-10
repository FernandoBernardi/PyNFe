# -*- coding: utf-8 -*-
from pynfe.utils import etree, remover_acentos
from pynfe.utils.flags import NAMESPACE_SIG
from signxml import XMLSigner, SignatureConstructionMethod, SignatureMethod, DigestAlgorithm, CanonicalizationMethod
from pynfe.entidades import CertificadoA1


class Assinatura(object):
    """Classe abstrata responsavel por definir os metodos e logica das classes
    de assinatura digital."""

    certificado = None
    senha = None

    def __init__(self, certificado, senha, autorizador=None):
        self.certificado = certificado
        self.senha = senha
        self.autorizador = autorizador

    def assinar(self, xml):
        """Efetua a assinatura da nota"""
        pass


class AssinaturaA1(Assinatura):

    def __init__(self, certificado, senha):
        self.key, self.cert = CertificadoA1(certificado).separar_arquivo(senha)

    def assinar(self, xml, retorna_string=False):
        # busca tag que tem id(reference_uri), logo nao importa se tem namespace
        reference = xml.find(".//*[@Id]").attrib['Id']

        # retira acentos
        xml_str = remover_acentos(etree.tostring(xml, encoding="unicode", pretty_print=False))
        xml = etree.fromstring(xml_str)

        signer = XMLSigner(
            method=SignatureConstructionMethod.enveloped,
            signature_algorithm=SignatureMethod.RSA_SHA1,
            digest_algorithm=DigestAlgorithm.SHA1,
            c14n_algorithm=CanonicalizationMethod.CANONICAL_XML_1_0)

        ns = {None: signer.namespaces['ds']}
        signer.namespaces = ns

        ref_uri = ('#%s' % reference) if reference else None
        signed_root = signer.sign(
            xml, key=self.key, cert=self.cert, reference_uri=ref_uri)

        ns = {'ns': NAMESPACE_SIG}
        # coloca o certificado na tag X509Data/X509Certificate
        tagX509Data = signed_root.find('.//ns:X509Data', namespaces=ns)
        etree.SubElement(tagX509Data, 'X509Certificate').text = self.cert
        if retorna_string:
            return etree.tostring(signed_root, encoding="unicode", pretty_print=False)
        else:
            return signed_root
