import os

from lxml import etree

from pynfe.data.Webservices import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NFCE = {
    'RO': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp?',
        'URL': 'http://www.nfce.sefin.ro.gov.br'
    },
    'AC': {
        'QR': 'sefaznet.ac.gov.br/nfce?',
        'URL': 'sefaznet.ac.gov.br/nfce/consulta',
        'HTTPS': 'http://www.',
        'HOMOLOGACAO': 'http://hml.'
    },
    'AM': {
        # csc_homologacao = '0123456789'
        # token_homologacao = '000001'
        'STATUS': 'nfe.sefaz.am.gov.br/services2/services/NfeStatusServico4',
        'AUTORIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao4',
        'RECIBO': 'nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao4',
        'CHAVE': 'nfe.sefaz.am.gov.br/services2/services/NfeConsulta4',
        'INUTILIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao4',
        'EVENTOS': 'nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento4',
        'QR': 'sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?',
        'URL': 'sefaz.am.gov.br/nfceweb/formConsulta.do',
        'HTTPS': 'http://sistemas.',
        'HOMOLOGACAO': 'http://homnfce.'
    },
    'RR': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': '/nfce/servlet/qrcode?',
        'URL': '/nfce/servlet/wp_consulta_nfce',
        'HTTPS': 'https://www.sefaz.rr.gov.br',
        'HOMOLOGACAO': 'http://200.174.88.103:8080'
    },
    'PA': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'view/consultas/nfce/nfceForm.seam?',
        'URL': 'view/consultas/nfce/consultanfce.seam',
        'HTTPS': 'https://appnfc.sefa.pa.gov.br/portal/',
        'HOMOLOGACAO': 'https://appnfc.sefa.pa.gov.br/portal-homologacao/'
    },
    'AP': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': '/nfcep.php?',
        'URL': 'https://www.sefaz.ap.gov.br/sate/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1261',
        'HTTPS': '	https://www.sefaz.ap.gov.br/nfce',
        'HOMOLOGACAO': 'https://www.sefaz.ap.gov.br/nfcehml'
    },
    'TO': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://www.sefaz.to.gov.br/nfce/qrcode?',
        'URL': 'http://www.sefaz.to.gov.br/nfce/consulta'
    },
    'MA': {
        'QR': 'nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp?',
        'HTTPS': '',
        'HOMOLOGACAO': '',
        'URL': 'http://www.sefaz.ma.gov.br/nfce/consulta'
    },
    'PI': {
        'QR': 'http://www.sefaz.pi.gov.br/nfce/qrcode?',
        'HTTPS': '',
        'HOMOLOGACAO': '',
        'URL': 'http://www.sefaz.pi.gov.br/nfce/consulta'
    },
    'CE': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html?',
        'URL': 'http://nfceh.sefaz.ce.gov.br/pages/consultaNota.jsf'
    },
    'RN': {
        'QR': 'http://nfce.set.rn.gov.br/consultarNFCe.aspx?',
        'HTTPS': '',
        'HOMOLOGACAO': '',
        'URL': 'http://www.set.rn.gov.br/nfce/consulta'
    },
    'PB': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://www.sefaz.pb.gov.br/nfce?',
        'URL': 'https://www.receita.pb.gov.br/nfce/consulta'
    },
    'PE': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'sefaz.pe.gov.br/nfce-web/consultarNFCe',
        'HTTPS': 'http://nfce.',
        'HOMOLOGACAO': 'http://nfcehomolog.',
        'URL': 'sefaz.pe.gov.br/nfce/consulta'
    },
    'AL': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp?',
        'URL': 'http://www.sefaz.al.gov.br/nfce/consulta'
    },
    'SE': {
        'QR': 'http://www.nfce.se.gov.br/nfce/qrcode?',
        'HTTPS': '',
        'HOMOLOGACAO': '',
        'URL': 'http://www.nfce.se.gov.br/nfce/consulta'
    },
    'BA': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?',
        'HTTPS': 'http://nfe.',
        'HOMOLOGACAO': 'http://hnfe.',
        'URL': 'http://hinternet.sefaz.ba.gov.br/nfce/consulta'
    },
    'MG': {
        'STATUS': 'fazenda.mg.gov.br/nfce/services/NFeStatusServico4',
        'AUTORIZACAO': 'fazenda.mg.gov.br/nfce/services/NFeAutorizacao4',
        'RECIBO': 'fazenda.mg.gov.br/nfce/services/NFeRetAutorizacao4',
        'CHAVE': 'fazenda.mg.gov.br/nfce/services/NFeConsultaProtocolo4',
        'INUTILIZACAO': 'fazenda.mg.gov.br/nfce/services/NFeInutilizacao4',
        'EVENTOS': 'fazenda.mg.gov.br/nfce/services/NFeRecepcaoEvento4',
        'CADASTRO': 'fazenda.mg.gov.br/nfce/services/CadConsultaCadastro4',
        'QR': 'https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml',
        'HTTPS': 'https://nfce.',
        'HOMOLOGACAO': 'https://hnfce.',
        'URL': 'fazenda.mg.gov.br/portalnfce'
    },
    'ES': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'sefaz.es.gov.br/ConsultaNFCe/qrcode.aspx?	',
        'HTTPS': 'http://nfe.',
        'HOMOLOGACAO': 'http://homologacao.',
        'URL': 'www.sefaz.es.gov.br/nfce/consulta'
    },
    'RJ': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?',
        'URL': 'www.fazenda.rj.gov.br/nfce/consulta'
    },
    'SP': {
        'STATUS': 'nfce.fazenda.sp.gov.br/ws/NFeStatusServico4.asmx',
        'AUTORIZACAO': 'nfce.fazenda.sp.gov.br/ws/NFeAutorizacao4.asmx',
        'RECIBO': 'nfce.fazenda.sp.gov.br/ws/NFeRetAutorizacao4.asmx',
        'CHAVE': 'nfce.fazenda.sp.gov.br/ws/NFeConsultaProtocolo4.asmx',
        'INUTILIZACAO': 'nfce.fazenda.sp.gov.br/ws/NFeInutilizacao4.asmx',
        'EVENTOS': 'nfce.fazenda.sp.gov.br/ws/NFeRecepcaoEvento4.asmx',
        'QR': 'nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?',
        'URL': 'nfce.fazenda.sp.gov.br/consulta',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'PR': {
        'STATUS': 'nfce.sefa.pr.gov.br/nfce/NFeStatusServico4?wsdl',
        'AUTORIZACAO': 'nfce.sefa.pr.gov.br/nfce/NFeAutorizacao4?wsdl',
        'RECIBO': 'nfce.sefa.pr.gov.br/nfce/NFeRetAutorizacao4?wsdl',
        'CHAVE': 'nfce.sefa.pr.gov.br/nfce/NFeConsultaProtocolo4?wsdl',
        'INUTILIZACAO': 'nfce.sefa.pr.gov.br/nfce/NFeInutilizacao4?wsdl',
        'EVENTOS': 'nfce.sefa.pr.gov.br/nfce/NFeRecepcaoEvento4?wsdl',
        'CADASTRO': 'nfce.sefa.pr.gov.br/nfce/CadConsultaCadastro4?wsdl',
        'QR': 'http://www.fazenda.pr.gov.br/nfce/qrcode?',
        'URL': 'http://www.fazenda.pr.gov.br/nfce/consulta',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'SC': {
        'STATUS': '',
        'AUTORIZACAO': '',
        'RECIBO': '',
        'CHAVE': '',
        'INUTILIZACAO': '',
        'EVENTOS': '',
        'QR': 'sat.sef.sc.gov.br/nfce/consulta?',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://hom.',
        'URL': 'sat.sef.sc.gov.br/nfce/consulta'
    },
    'RS': {
        'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
        'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
        'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
        'QR': 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?',
        'URL': 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx',
        'HTTPS': 'https://nfce.',
        'HOMOLOGACAO': 'https://nfce-homologacao.'
    },
    'MS': {
        'STATUS': 'sefaz.ms.gov.br/ws/NFeStatusServico4?wsdl',
        'AUTORIZACAO': 'sefaz.ms.gov.br/ws/NFeAutorizacao4?wsdl',
        'RECIBO': 'sefaz.ms.gov.br/ws/NFeRetAutorizacao4?wsdl',
        'CHAVE': 'sefaz.ms.gov.br/ws/NFeConsultaProtocolo4?wsdl',
        'INUTILIZACAO': 'sefaz.ms.gov.br/ws/NFeInutilizacao4?wsdl',
        'EVENTOS': 'sefaz.ms.gov.br/ws/NFeRetAutorizacao4',
        'QR': 'http://www.dfe.ms.gov.br/nfce/qrcode',
        'URL': 'http://www.dfe.ms.gov.br/nfce/consulta',
        'HTTPS': 'https://nfce.',
        'HOMOLOGACAO': 'https://hom.nfce.'
    },
    'MT': {
        'QR': 'sefaz.mt.gov.br/nfce/consultanfce?',
        'HTTPS': 'https://nfce.',
        'HOMOLOGACAO': 'http://homologacao.',
        'STATUS': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeStatusServico4?wsdl',
        'AUTORIZACAO': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeAutorizacao4?wsdl',
        'RECIBO': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeRetAutorizacao4?wsdl',
        'CHAVE': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeConsultaProtocolo4?wsdl',
        'INUTILIZACAO': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeInutilizacao4?wsdl',
        'EVENTOS': 'nfce.sefaz.mt.gov.br/nfcews/services/NFeRetAutorizacao4',
        'URL': 'sefaz.mt.gov.br/nfce/consultanfce',
    },
    'GO': {
        'STATUS': 'sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl',
        'AUTORIZACAO': 'sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl',
        'RECIBO': 'sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl',
        'CHAVE': 'sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl',
        'INUTILIZACAO': 'sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl',
        'EVENTOS': 'sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl',
        'QR': 'sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?',
        'CADASTRO': 'sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://homolog.',
        'URL': 'sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe'
    },
    'DF': {
        'QR': 'http://www.fazenda.df.gov.br/nfce/qrcode?',
        'URL': 'www.fazenda.df.gov.br/nfce/consulta'
    },
    # RO, AC, RR, PA, AP, TO, MA, PI, RN, PB, AL, SE, BA, ES, RJ, GO, DF
    'SVRS': {
        'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
        'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
        'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
        'QR': '',
        'HTTPS': 'https://nfce.',
        'HOMOLOGACAO': 'https://nfce-homologacao.'
    },
}

# Nfe
# homologação => http://hom.nfe.fazenda.gov.br/PORTAL/WebServices.aspx
# produção    => https://www.nfe.fazenda.gov.br/portal/webServices.aspx
NFE = {
    # Alguns serviços são disponibilizados apenas pelo ambiente nacional
    'AN': {
        'EVENTOS': 'nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',  # versao: 4.00
        'DISTRIBUICAO': 'nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx',
        'HTTPS': 'https://www',
        'HOMOLOGACAO': 'https://hom1'
    },
    'AM': {
        'STATUS': 'nfe.sefaz.am.gov.br/services2/services/NfeStatusServico4',
        'AUTORIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao4',
        'RECIBO': 'nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao4',
        'CHAVE': 'nfe.sefaz.am.gov.br/services2/services/NfeConsulta4',
        'INUTILIZACAO': 'nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao4',
        'EVENTOS': 'nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento4',
        'CADASTRO': 'nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://hom'
    },
    'MA': {
        'CADASTRO': 'https://sistemas.sefaz.ma.gov.br/wscadastro/CadConsultaCadastro2?wsdl'
    },
    'PE': {
        'STATUS': 'sefaz.pe.gov.br/nfe-service/services/NFeStatusServico4',
        'AUTORIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NFeAutorizacao4',
        'RECIBO': 'sefaz.pe.gov.br/nfe-service/services/NFeRetAutorizacao4',
        'CHAVE': 'sefaz.pe.gov.br/nfe-service/services/NFeConsultaProtocolo4',
        'INUTILIZACAO': 'sefaz.pe.gov.br/nfe-service/services/NFeInutilizacao4',
        'EVENTOS': 'sefaz.pe.gov.br/nfe-service/services/NFeRecepcaoEvento4',
        'CADASTRO': 'sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro4?wsdl',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://nfehomolog.'
    },
    'BA': {
        'STATUS': 'nfe.sefaz.ba.gov.br/webservices/NFeStatusServico4/NFeStatusServico4.asmx',
        'AUTORIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx',
        'RECIBO': 'nfe.sefaz.ba.gov.br/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
        'CHAVE': 'nfe.sefaz.ba.gov.br/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        'INUTILIZACAO': 'nfe.sefaz.ba.gov.br/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx',
        'EVENTOS': 'nfe.sefaz.ba.gov.br/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        'CADASTRO': 'nfe.sefaz.ba.gov.br/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://h'
    },
    'MG': {
        'STATUS': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeStatusServico4',
        'AUTORIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeAutorizacao4',
        'RECIBO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeRetAutorizacao4',
        'CHAVE': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeConsultaProtocolo4',
        'INUTILIZACAO': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeInutilizacao4',
        'EVENTOS': 'nfe.fazenda.mg.gov.br/nfe2/services/NFeRecepcaoEvento4',
        'CADASTRO': 'nfe.fazenda.mg.gov.br/nfe2/services/CadConsultaCadastro4',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://h'
    },
    'SP': {
        'STATUS': 'nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx',
        'AUTORIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx',
        'RECIBO': 'nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx',
        'CHAVE': 'nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx',
        'INUTILIZACAO': 'nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx',
        'EVENTOS': 'nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx',
        'CADASTRO': 'nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'PR': {
        'STATUS': 'nfe.sefa.pr.gov.br/nfe/NFeStatusServico4',  # CONSULTA STATUS DO SERVICO
        'AUTORIZACAO': 'nfe.sefa.pr.gov.br/nfe/NFeAutorizacao4',  # AUTORIZACAO
        'RECIBO': 'nfe.sefa.pr.gov.br/nfe/NFeRetAutorizacao4',  # CONSULTA RECIBO
        'CHAVE': 'nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4',  # CONSULTA CHAVE DE ACESSO
        'INUTILIZACAO': 'nfe.sefa.pr.gov.br/nfe/NFeInutilizacao4',  # INUTILIZAÇAO
        'EVENTOS': 'nfe.sefa.pr.gov.br/nfe/NFeRecepcaoEvento4',  # REGISTRO DE EVENTOS
        'CADASTRO': 'nfe.sefa.pr.gov.br/nfe/CadConsultaCadastro4',  # CONSULTA CADASTRO
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    # https://www.sefaz.rs.gov.br/site/MontaDuvidas.aspx?al=l_rel_end_ws_nfe
    'RS': {
        'STATUS': 'sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
        'AUTORIZACAO': 'sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        'RECIBO': 'sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        'CHAVE': 'sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
        'INUTILIZACAO': 'sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        'EVENTOS': 'sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
        'CADASTRO': 'https://cad.sefazrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        'DOWNLOAD': 'sefazrs.rs.gov.br/ws/nfeDownloadNF/nfeDownloadNF.asmx',
        'DESTINADAS': 'sefazrs.rs.gov.br/ws/nfeConsultaDest/nfeConsultaDest.asmx',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://nfe-homologacao.'
    },
    'MS': {
        'STATUS': 'nfe.sefaz.ms.gov.br/ws/NFeStatusServico4',
        'AUTORIZACAO': 'nfe.sefaz.ms.gov.br/ws/NFeAutorizacao4',
        'RECIBO': 'nfe.sefaz.ms.gov.br/ws/NFeRetAutorizacao4',
        'CHAVE': 'nfe.sefaz.ms.gov.br/ws/NFeConsultaProtocolo4',
        'INUTILIZACAO': 'nfe.sefaz.ms.gov.br/ws/NFeInutilizacao4',
        'EVENTOS': 'nfe.sefaz.ms.gov.br/ws/NFeRecepcaoEvento4',
        'CADASTRO': 'nfe.sefaz.ms.gov.br/ws/CadConsultaCadastro4',
        'HTTPS': 'https://',
        'HOMOLOGACAO': 'https://hom.'
    },
    'MT': {
        'STATUS': 'sefaz.mt.gov.br/nfews/v2/services/NfeStatusServico4?wsdl',
        'AUTORIZACAO': 'sefaz.mt.gov.br/nfews/v2/services/NfeAutorizacao4?wsdl',
        'RECIBO': 'sefaz.mt.gov.br/nfews/v2/services/NfeRetAutorizacao4?wsdl',
        'CHAVE': 'sefaz.mt.gov.br/nfews/v2/services/NfeConsulta4?wsdl',
        'INUTILIZACAO': 'sefaz.mt.gov.br/nfews/v2/services/NfeInutilizacao4?wsdl',
        'EVENTOS': 'sefaz.mt.gov.br/nfews/v2/services/RecepcaoEvento4?wsdl',
        'CADASTRO': 'sefaz.mt.gov.br/nfews/v2/services/CadConsultaCadastro4?wsdl',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'GO': {
        'STATUS': 'sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl',
        'AUTORIZACAO': 'sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl',
        'RECIBO': 'sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl',
        'CHAVE': 'sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl',
        'INUTILIZACAO': 'sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl',
        'EVENTOS': 'sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl',
        'CADASTRO': 'sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://homolog.'
    },
    'SVAN': {
        'STATUS': 'sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx',
        'AUTORIZACAO': 'sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx',
        'RECIBO': 'sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx',
        'CHAVE': 'sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx',
        'INUTILIZACAO': 'sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx',
        'EVENTOS': 'sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx',
        'DOWNLOAD': 'sefazvirtual.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx',
        'HTTPS': 'https://www.',
        'HOMOLOGACAO': 'https://hom.'
    },
    'SVRS': {
        'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx',
        'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx',
        'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx',
        'CADASTRO': 'https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://nfe-homologacao.'
    },
    'SVC-AN': {
        'STATUS': 'svc.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx',
        'AUTORIZACAO': 'svc.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx',
        'RECIBO': 'svc.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx',
        'CHAVE': 'svc.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx',
        'EVENTOS': 'svc.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx',
        'HTTPS': 'https://www.',
        'HOMOLOGACAO': 'https://hom.'
    },
    'SVC-RS': {
        'STATUS': 'svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx',
        'AUTORIZACAO': 'svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx',
        'RECIBO': 'svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx',
        'CHAVE': 'svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx',
        'INUTILIZACAO': 'svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        'EVENTOS': 'svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://nfe-homologacao.'
    },
}

# Nfs-e
NFSE = {
    #
    'BETHA': {
        'AUTORIZACAO': 'GerarNfse',
        'CANCELAR': 'CancelarNfse',
        'CONSULTA_RPS': 'consultarNfsePorRps',
        'CONSULTA_FAIXA': 'ConsultarNfseFaixa',
        'CONSULTA_SERVICO': 'ConsultarNfseServicoPrestado',
        'CONSULTA_SERVICO_TOMADO': 'ConsultarNfseServicoTomado',
        'SUBSTITUIR': 'SubstituirNfse',
        'HTTPS': 'http://e-gov.betha.com.br/e-nota-contribuinte-ws/nfseWS?wsdl',
        'HOMOLOGACAO': 'http://e-gov.betha.com.br/e-nota-contribuinte-test-ws/nfseWS?wsdl'
    },
    #
    'GINFES': {
        'AUTORIZACAO': 'GerarNfse',
        'CANCELAR': 'CancelarNfse',
        'CONSULTA_RPS': 'ConsultarNfsePorRps',
        'CONSULTA_FAIXA': 'ConsultarNfseFaixa',
        'CONSULTA_SERVICO': 'ConsultarNfseServicoPrestado',
        'CONSULTA_SERVICO_TOMADO': 'ConsultarNfseServicoTomado',
        'SUBSTITUIR': 'SubstituirNfse',
        'HTTPS': 'https://producao.ginfes.com.br/ServiceGinfesImpl?wsdl',
        'HOMOLOGACAO': 'https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl'
    }
}

# MDF-e
MDFE = {
    # unico autorizador de MDF-e
    'SVRS': {
        'RECEPCAO': 'MDFeRecepcao/MDFeRecepcao.asmx',
        'RECEPCAO_SINC': 'MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx',
        'RET_RECEPCAO': 'mdferetrecepcao/MDFeRetRecepcao.asmx',
        'EVENTOS': 'mdferecepcaoevento/MDFeRecepcaoEvento.asmx',
        'CONSULTA': 'mdfeconsulta/MDFeConsulta.asmx',
        'STATUS': 'mdfestatusservico/MDFeStatusServico.asmx',
        'NAO_ENCERRADOS': 'mdfeconsnaoenc/MDFeConsNaoEnc.asmx',
        'HTTPS': 'https://mdfe.svrs.rs.gov.br/ws/',
        'HOMOLOGACAO': 'https://mdfe-homologacao.svrs.rs.gov.br/ws/',
        'QRCODE': 'https://dfe-portal.svrs.rs.gov.br/mdfe/qrCode'
    }
}

CTE = {
    'AN': {
        'DISTRIBUICAO': 'cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx',
        'HTTPS': 'https://www1',
        'HOMOLOGACAO': 'https://hom1'
    },
    'MT': {
        'STATUS': 'sefaz.mt.gov.br/ctews/services/CteStatusServico',
        'HTTPS': 'https://cte.',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'MS': {
        'STATUS': 'cte.ms.gov.br/ws/CteStatusServico',
        'HTTPS': 'https://producao.',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'MG': {
        'STATUS': 'fazenda.mg.gov.br/cte/services/CteStatusServico',
        'HTTPS': 'https://cte.',
        'HOMOLOGACAO': 'https://hcte.'
    },
    'PR': {
        'STATUS': 'fazenda.pr.gov.br/cte/CteStatusServico?wsdl',
        'HTTPS': 'https://cte.',
        'HOMOLOGACAO': 'https://homologacao.'
    },
    'RS': {
        'STATUS': 'svrs.rs.gov.br/ws/ctestatusservico/CteStatusServico.asmx',
        'HTTPS': 'https://cte.',
        'HOMOLOGACAO': 'https://cte-homologacao.'
    },
    'SP': {
        'STATUS': 'fazenda.sp.gov.br/cteWEB/services/cteStatusServico.asmx',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://homologacao.nfe.'
    },
    'SVRS': {
        'STATUS': 'svrs.rs.gov.br/ws/ctestatusservico/CteStatusServico.asmx',
        'HTTPS': 'https://cte.',
        'HOMOLOGACAO': 'https://cte-homologacao.'
    },
    'SVSP': {
        'STATUS': 'fazenda.sp.gov.br/cteWEB/services/CteStatusServico.asmx',
        'HTTPS': 'https://nfe.',
        'HOMOLOGACAO': 'https://homologacao.nfe.'
    },
}


def get_default_webservice_nfce(uf: str, key: str, default_server: str = 'SVRS') -> str:
    """
    Obtem o webservice padrão para o estado informado
    """
    uf = uf.upper()
    key = key.upper()
    try:
        if uf in NFCE and key in NFCE[uf] and NFCE[uf][key] != '':
            return NFCE[uf][key]
        return NFCE[default_server][key]
    except KeyError:
        return NFCE[default_server][key]


def obter_webservice(uf: str, tipo_ambiente: str, modelo: str) -> dict:
    """
    Obtem as informações do webservice para o estado informado
    """
    uf = uf.upper()
    modelo = modelo.lower()
    base_path_web_services = os.path.join(BASE_DIR, 'pynfe', 'data', 'Webservices')
    if tipo_ambiente == '1':
        tipo_ambiente = 'Producao'
    elif tipo_ambiente == '2':
        tipo_ambiente = 'Homologacao'
    else:
        raise ValueError('Tipo de ambiente inválido')
    if modelo == 'nfce':
        path_modelo = os.path.join(base_path_web_services, 'NFCe.xml')
    elif modelo == 'nfe':
        path_modelo = os.path.join(base_path_web_services, 'NFe.xml')
    else:
        raise NotImplementedError()
    root = etree.parse(path_modelo).getroot()
    for uf_tag in root.findall('UF'):
        if uf_tag.get('UF') == uf:
            return {
                'STATUS': uf_tag.find(f'{tipo_ambiente}/StatusServico').text,
                'QR': uf_tag.find(f'{tipo_ambiente}/UrlQRCode').text,
                'URL': uf_tag.find(f'{tipo_ambiente}/UrlConsultaChaveAcesso').text,
                'AUTORIZACAO': uf_tag.find(f'{tipo_ambiente}/Autorizacao').text,
                'INUTILIZACAO': uf_tag.find(f'{tipo_ambiente}/Inutilizacao').text,
                'EVENTOS': uf_tag.find(f'{tipo_ambiente}/RecepcaoEvento').text,
                'RECIBO': uf_tag.find(f'{tipo_ambiente}/RetAutorizacao').text,
                'CHAVE': uf_tag.find(f'{tipo_ambiente}/Consulta').text,
            }
    raise ValueError(f'WEBSERVICE {uf} {tipo_ambiente} não encontrada!')
