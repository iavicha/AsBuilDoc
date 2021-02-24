

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4


def make_act(act_model):
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    pdfmetrics.registerFont(TTFont('NotoSans', '../NotoSans-Light.ttf'))
    pdfmetrics.registerFont(TTFont('NotoSansregular', '../NotoSans-Regular.ttf'))

    file = canvas.Canvas('test_pdf.pdf', pagesize=A4)
    file.setFont('NotoSansregular', 11)
    file.setLineWidth(.7)
    file.drawString(40, 820, 'Объект капитального строительства:')
    file.setFont('NotoSans', 12)
    file.drawString(40, 806, 'Строительство жилого дома на 200 квартир по адресу г. Санкт-Петербург')
    file.line(40, 804, 580, 804)
    file.setFont('NotoSans', 8)
    file.drawString(70, 794, '(наименование проектной документации, почтовый или строительный адрес '
                             'объекта капитального строительства)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 780, "Застройщик ")
    file.setFont('NotoSans', 11)
    file.drawString(115, 780, "(технический заказчик, эксплуатирующая организация или региональный оператор)")
    file.setFont('NotoSans', 12)
    file.drawString(40, 766, 'Компания заказчик стр 1')
    file.line(40, 764, 580, 764)
    file.setFont('NotoSans', 8)
    file.drawString(100, 756, '(фамилия, имя, отчество, адрес места жительства, ОГРНИП, ИНН индивидуального '
                              'предпринимателя,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 742, 'Компания заказчик стр 2')
    file.line(40, 740, 580, 740)
    file.setFont('NotoSans', 8)
    file.drawString(140, 730, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 718, 'Компания заказчик СРО')
    file.line(40, 716, 580, 716)
    file.setFont('NotoSans', 8)
    file.drawString(60, 706, 'наименование, ОГРН, ИНН саморегулируемой организации, членом которой является - для '
                             'инд. предпринимателей и юр. лиц;')
    file.setFont('NotoSans', 12)
    file.drawString(40, 692, 'Компания заказчик стр 3')
    file.line(40, 690, 580, 690)
    file.setFont('NotoSans', 8)
    file.drawString(50, 680, 'фамилия, имя, отчество, паспортные данные, адрес места жительства, телефон/факс - для '
                             'физических лиц, не являющихся инд. предпр.)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 669, "Лицо, осуществляющее строительство ")
    file.setFont('NotoSans', 12)
    file.drawString(40, 657, 'Строитель 1')
    file.line(40, 655, 580, 655)
    file.setFont('NotoSans', 8)
    file.drawString(100, 645, '(фамилия, имя, отчество , адрес места жительства, ОГРНИП, ИНН индивидуального '
                              'предпринимателя,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 631, 'Строитель 2')
    file.line(40, 629, 580, 629)
    file.setFont('NotoSans', 8)
    file.drawString(140, 619, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 605, 'Строитель СРО')
    file.line(40, 603, 580, 603)
    file.setFont('NotoSans', 8)
    file.drawString(140, 593, 'наименование, ОГРН, ИНН саморегулируемой организации,  членом которой является )')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 580, "Лицо, осуществляющее подготовку проектной документации ")
    file.setFont('NotoSans', 12)
    file.drawString(40, 566, 'Проектировщик 1')
    file.line(40, 564, 580, 564)
    file.setFont('NotoSans', 8)
    file.drawString(100, 554, '(фамилия, имя, отчество , адрес места жительства, ОГРНИП, ИНН индивидуального '
                              'предпринимателя,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 540, 'Проектировщик 2')
    file.line(40, 538, 580, 538)
    file.setFont('NotoSans', 8)
    file.drawString(140, 528, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 514, 'Проектировщик СРО')
    file.line(40, 512, 580, 512)
    file.setFont('NotoSans', 8)
    file.drawString(140, 502, 'наименование, ОГРН, ИНН саморегулируемой организации,  членом которой является )')
    file.setFont('NotoSansregular', 11)
    file.drawString(300, 489, 'АКТ')
    file.drawString(210, 476, 'освидетельствования скрытых работ')
    file.drawString(40, 463, '№______')
    file.drawString(470, 463, '20 сентября 2021 г.')
    file.line(470, 461, 580, 461)
    file.setFont('NotoSans', 8)
    file.drawString(475, 451, '(дата составления акта)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 438, 'Представитель застройщика (технического заказчика, эксплуатирующей организации или реги-')
    file.drawString(40, 425, 'онального   оператора)  по вопросам  строительного контроля')
    file.setFont('NotoSans', 12)
    file.drawString(40, 411, 'Заказчик строка 1')
    file.line(40, 409, 580, 409)
    file.setFont('NotoSans', 8)
    file.drawString(70, 399,
                    '(должность, фамилия, инициалы, идентификационный номер в национальном реестре специалистов'
                    ' в области строительства')
    file.setFont('NotoSans', 12)
    file.drawString(40, 385, 'Заказчик строка 2')
    file.line(40, 383, 580, 383)
    file.setFont('NotoSans', 8)
    file.drawString(70, 373,
                    'реквизиты распорядительного документа, подтверждающего полномочия,с указанием наименования, '
                    'ОГРН, ИНН,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 359, 'Заказчик строка 3')
    file.line(40, 357, 580, 357)
    file.setFont('NotoSans', 8)
    file.drawString(140, 347, ' места нахождения юридического лиц  фамилии, имени, отчества,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 334, 'Заказчик строка 4')
    file.line(40, 332, 580, 332)
    file.setFont('NotoSans', 8)
    file.drawString(140, 322, 'адреса места жительства, ОГРНИП, ИНН индивидуального предпринимателя)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 309, 'Представитель лица, осуществляющего строительство')
    file.setFont('NotoSans', 12)
    file.drawString(40, 295, 'Строитель')
    file.line(40, 293, 580, 293)
    file.setFont('NotoSans', 8)
    file.drawString(100, 283, '(должность, фамилия, инициалы, реквизиты распорядительного документа, подтверждающего '
                              'полномочия)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 270, 'Представитель лица, осуществляющего строительство, по вопросам строительного '
                             'контроля')
    file.setFont('NotoSans', 12)
    file.drawString(40, 256, 'Организатор 1')
    file.line(40, 254, 580, 254)
    file.setFont('NotoSans', 8)
    file.drawString(140, 244,
                    '(должность, фамилия, инициалы, идентификационный номер в национальном реестре специалистов')
    file.setFont('NotoSans', 12)
    file.drawString(40, 230, 'Организатор 2')
    file.line(40, 228, 580, 228)
    file.setFont('NotoSans', 8)
    file.drawString(140, 218,
                    'в области строительства, реквизиты распорядительного документа, подтверждающего полномочия)')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 205, 'Представитель лица, осуществляющего подготовку проектной документации')
    file.setFont('NotoSans', 12)
    file.drawString(40, 191, 'Проектировщик 1')
    file.line(40, 189, 580, 189)
    file.setFont('NotoSans', 8)
    file.drawString(70, 179, '(должность, фамилия, инициалы, инициалы, реквизиты распорядительного документа,'
                             ' подтверждающего полномочия,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 165, 'Проектировщик 2')
    file.line(40, 163, 580, 163)
    file.setFont('NotoSans', 8)
    file.drawString(70, 153, 'с указанием наименования, ОГРН, ИНН, места нахождения, юридического лица, ')
    file.setFont('NotoSans', 12)
    file.drawString(40, 139, 'Проектировщик 3')
    file.line(40, 137, 580, 137)
    file.setFont('NotoSans', 8)
    file.drawString(140, 127, 'фамилии, имени, отчества, адреса места жительства, ОГРНИП,ИНН индивидуального '
                              'предпринимателя ,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 112, 'Проектировщик 4')
    file.line(40, 110, 580, 110)
    file.setFont('NotoSans', 8)
    file.drawString(40, 100, 'наименования, ОГРН, ИНН саморегулируемой организации, членом которой, является указанное '
                             'юридическое лицо, индивидуальный предприниматель) ')
    file.setFont('NotoSansregular', 11)
    file.drawString(40, 87, 'Представитель лица, выполнившего работы, подлежащие освидетельствованию')
    file.setFont('NotoSans', 12)
    file.drawString(40, 73, 'Прораб 1')
    file.line(40, 71, 580, 71)
    file.setFont('NotoSans', 8)
    file.drawString(70, 61, '(должность, фамилия, инициалы, реквизиты распорядительного документа, подтверждающего '
                            'полномочия,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 47, 'Прораб 2')
    file.line(40, 45, 580, 45)
    file.setFont('NotoSans', 8)
    file.drawString(70, 35, ' с указанием наименования, ОГРН, ИНН, места нахождения юридического лица,')
    file.setFont('NotoSans', 12)
    file.drawString(40, 21, 'Прораб 3')
    file.line(40, 19, 580, 19)
    file.setFont('NotoSans', 8)
    file.drawString(140, 9, 'фамилии, имени, отчества, адреса места жительства, ОГРНИП, ИНН индивидуального '
                            'предпринимателя)')
    file.save()
