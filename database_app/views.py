import io
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase.ttfonts import TTFont
from .models import *


def do_it_pdf():
    ...


def some_view(request, queryset):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    for i in queryset.values():
        count = (len(queryset.values('id')))

        while count != 0:
            number = ''
            d = i['id']
            act = HiddenWorksSurveyCertificate.objects.filter(id=d)
            number = act.values('number')[0]['number']
            date = str((act.values('date_of_signature')[0]['date_of_signature']))
            object_ = str(act.values('_object__name')[0]['_object__name'])
            object_adr = str(act.values('_object__address')[0]['_object__address'])
            customer_name = str(act.values('customer__name')[0]['customer__name'])
            customer_adr = str(act.values('customer__address')[0]['customer__address'])
            customer_details = str(act.values('customer__details')[0]['customer__details'])
            general_contractor_name = str(act.values('general_contractor__name')[0]['general_contractor__name'])
            general_contractor_adr = str(act.values('general_contractor__address')[0]['general_contractor__address'])
            general_contractor_details = str(act.values('general_contractor__details')[0]
                                             ['general_contractor__details'])
            designer_name = str(act.values('designer__name')[0]['designer__name'])
            designer_adr = str(act.values('designer__address')[0]['designer__address'])
            designer_detail = str(act.values('designer__details')[0]['designer__details'])
            other_people = str(act.values('other_people')[0]['other_people'])
            builder_name = str(act.values('builder__name')[0]['builder__name'])
            builder_address = str(act.values('builder__address')[0]['builder__address'])
            builder_details = str(act.values('builder__details')[0]['builder__details'])
            job_name = str(act.values('job__name')[0]['job__name'])
            job_start_date = str(act.values('job__start_date')[0]['job__start_date'])
            job_end_date = str(act.values('job__end_date')[0]['job__end_date'])
            job_next = str(act.values('job___next')[0]['job___next'])
            material_name = str(act.values('material__name')[0]['material__name'])
            material_document_name = str(act.values('material__documents__name')[0]['material__documents__name'])
            # basedir = os.path.abspath(os.path.dirname(__file__))
            # material_certificate = os.path.join(basedir, str(act.values('material__documents__file')[0]['material__documents__file']))
            # print(material_certificate)

            # Create the PDF object, using the buffer as its "file."
            file = canvas.Canvas(buffer)

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            pdfmetrics.registerFont(TTFont('NotoSans', 'database_app/NotoSans-Light.ttf'))
            pdfmetrics.registerFont(TTFont('NotoSansregular', 'database_app/NotoSans-Light.ttf'))

            file = canvas.Canvas(buffer)
            file.setFont('NotoSansregular', 11)
            file.setLineWidth(.7)
            file.drawString(40, 820, 'Объект капитального строительства:')
            file.setFont('NotoSans', 12)
            file.drawString(40, 806, object_ + ' ' + object_adr)
            file.line(40, 804, 580, 804)
            file.setFont('NotoSans', 8)
            file.drawString(70, 794, '(наименование проектной документации, почтовый или строительный адрес '
                                     'объекта капитального строительства)')
            file.setFont('NotoSansregular', 11)
            file.drawString(40, 780, "Застройщик ")
            file.setFont('NotoSans', 11)
            file.drawString(115, 780, "(технический заказчик, эксплуатирующая организация или региональный оператор)")
            file.setFont('NotoSans', 12)
            file.drawString(40, 766, customer_name + ' ' + customer_adr)
            file.line(40, 764, 580, 764)
            file.setFont('NotoSans', 8)
            file.drawString(100, 756, '(фамилия, имя, отчество, адрес места жительства, ОГРНИП, ИНН индивидуального '
                                      'предпринимателя,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 742, customer_details)
            file.line(40, 740, 580, 740)
            file.setFont('NotoSans', 8)
            file.drawString(140, 730, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 718, 'Компания заказчик СРО')
            file.line(40, 716, 580, 716)
            file.setFont('NotoSans', 8)
            file.drawString(60, 706,
                            'наименование, ОГРН, ИНН саморегулируемой организации, членом которой является - для '
                            'инд. предпринимателей и юр. лиц;')
            file.setFont('NotoSans', 12)
            file.drawString(40, 692, 'Компания заказчик стр 3')
            file.line(40, 690, 580, 690)
            file.setFont('NotoSans', 8)
            file.drawString(50, 680,
                            'фамилия, имя, отчество, паспортные данные, адрес места жительства, телефон/факс - для '
                            'физических лиц, не являющихся инд. предпр.)')
            file.setFont('NotoSansregular', 11)
            file.drawString(40, 669, "Лицо, осуществляющее строительство ")
            file.setFont('NotoSans', 12)
            file.drawString(40, 657, general_contractor_name + ' ' + general_contractor_adr)
            file.line(40, 655, 580, 655)
            file.setFont('NotoSans', 8)
            file.drawString(100, 645, '(фамилия, имя, отчество , адрес места жительства, ОГРНИП, ИНН индивидуального '
                                      'предпринимателя,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 631, general_contractor_details)
            file.line(40, 629, 580, 629)
            file.setFont('NotoSans', 8)
            file.drawString(140, 619, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 605, 'Строитель СРО')
            file.line(40, 603, 580, 603)
            file.setFont('NotoSans', 8)
            file.drawString(140, 593,
                            'наименование, ОГРН, ИНН саморегулируемой организации,  членом которой является )')
            file.setFont('NotoSansregular', 11)
            file.drawString(40, 580, "Лицо, осуществляющее подготовку проектной документации ")
            file.setFont('NotoSans', 12)
            file.drawString(40, 566, designer_name + ' ' + designer_adr)
            file.line(40, 564, 580, 564)
            file.setFont('NotoSans', 8)
            file.drawString(100, 554, '(фамилия, имя, отчество , адрес места жительства, ОГРНИП, ИНН индивидуального '
                                      'предпринимателя,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 540, designer_detail)
            file.line(40, 538, 580, 538)
            file.setFont('NotoSans', 8)
            file.drawString(140, 528, 'наименование, ОГРН, ИНН, место нахождения юридического лица, телефон/факс,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 514, 'Проектировщик СРО')
            file.line(40, 512, 580, 512)
            file.setFont('NotoSans', 8)
            file.drawString(140, 502,
                            'наименование, ОГРН, ИНН саморегулируемой организации,  членом которой является )')
            file.setFont('NotoSansregular', 11)
            file.drawString(300, 489, 'АКТ')
            file.drawString(210, 476, 'освидетельствования скрытых работ')
            file.drawString(40, 463, number)
            file.line(40, 461, 80, 461)
            file.drawString(470, 463, date)
            file.line(470, 461, 580, 461)
            file.setFont('NotoSans', 8)
            file.drawString(475, 451, '(дата составления акта)')
            file.setFont('NotoSansregular', 11)
            file.drawString(40, 438,
                            'Представитель застройщика (технического заказчика, эксплуатирующей организации или реги-')
            file.drawString(40, 425, 'онального   оператора)  по вопросам  строительного контроля')
            file.setFont('NotoSans', 12)
            file.drawString(40, 411, 'Заказчик строка 1')
            file.line(40, 409, 580, 409)
            file.setFont('NotoSans', 8)
            file.drawString(70, 399,
                            '(должность, фамилия, инициалы, идентификационный номер в национальном реестре специалистов'
                            ' в области строительства')
            file.setFont('NotoSans', 12)
            file.drawString(40, 385, customer_name + ' ' + customer_adr)
            file.line(40, 383, 580, 383)
            file.setFont('NotoSans', 8)
            file.drawString(70, 373,
                            'реквизиты распорядительного документа, подтверждающего полномочия,с указанием '
                            'наименования, '
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
            file.drawString(100, 283,
                            '(должность, фамилия, инициалы, реквизиты распорядительного документа, подтверждающего '
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
                            'в области строительства, реквизиты распорядительного документа, подтверждающего '
                            'полномочия)')
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
            file.drawString(40, 100,
                            'наименования, ОГРН, ИНН саморегулируемой организации, членом которой, является указанное '
                            'юридическое лицо, индивидуальный предприниматель) ')
            file.setFont('NotoSansregular', 11)
            file.drawString(40, 87, 'Представитель лица, выполнившего работы, подлежащие освидетельствованию')
            file.setFont('NotoSans', 12)
            file.drawString(40, 73, 'Прораб 1')
            file.line(40, 71, 580, 71)
            file.setFont('NotoSans', 8)
            file.drawString(70, 61,
                            '(должность, фамилия, инициалы, реквизиты распорядительного документа, подтверждающего '
                            'полномочия,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 47, builder_name + ' ' + builder_address)
            file.line(40, 45, 580, 45)
            file.setFont('NotoSans', 8)
            file.drawString(70, 35, ' с указанием наименования, ОГРН, ИНН, места нахождения юридического лица,')
            file.setFont('NotoSans', 12)
            file.drawString(40, 21, builder_details)
            file.line(40, 19, 580, 19)
            file.setFont('NotoSans', 8)
            file.drawString(140, 9, 'фамилии, имени, отчества, адреса места жительства, ОГРНИП, ИНН индивидуального '
                                    'предпринимателя)')

            # Close the PDF object cleanly, and we're done.
            file.showPage()

            file.setFont('NotoSansregular', 11)
            file.setLineWidth(.7)
            file.drawString(15, 820, 'а также иные представители лиц, участвующих в совидетельствовании:')
            file.setFont('NotoSans', 12)
            file.drawString(15, 806, other_people)
            file.line(15, 804, 540, 804)
            file.setFont('NotoSans', 8)
            file.drawString(15, 794, '(должность с указанием наименования организации, фамилия, инициалы,'
                                     'реквизиты распорядительного документа,')
            file.drawString(15, 784, 'подтверждающего полномочия)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 771, 'Произвели осмтор работ, выполненных')
            file.setFont('NotoSans', 12)
            file.drawString(15, 757, builder_name + ' ' + builder_address)
            file.line(15, 755, 540, 755)
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 742, 'и составили настоящий акт о нижеследующем:')
            file.drawString(15, 729, '1. К освидетельствованию предъявлены следующие работы:')
            file.setFont('NotoSans', 12)
            file.drawString(15, 715, job_name)
            file.line(15, 713, 540, 713)
            file.setFont('NotoSans', 8)
            file.drawString(240, 703, '(наименование скрытых работ)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 690, '2. Работы выполнены по проектной документации')
            file.setFont('NotoSans', 12)
            file.drawString(15, 676, 'Проект 1')
            file.line(15, 674, 540, 674)
            file.setFont('NotoSans', 8)
            file.drawString(15, 664, '(номер, другие реквизиты чертежа, наименование проектной и/или рабочей '
                                     'документации,')
            file.setFont('NotoSans', 12)
            file.drawString(15, 650, 'Проект 2')
            file.line(15, 648, 540, 648)
            file.setFont('NotoSans', 8)
            file.drawString(15, 638, 'сведения о лицах, осуществляющих подготовку раздела проектной и/или рабочей '
                                     'документации)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 625, '3. При выполнении работ применены')
            file.setFont('NotoSans', 12)
            file.drawString(15, 611, material_name + ' (' + material_document_name + ')')
            file.line(15, 609, 540, 609)
            file.setFont('NotoSans', 8)
            file.drawString(15, 599, '(наименование строительных, материалов (изделий), реквизиты сертификатов')
            file.setFont('NotoSans', 12)
            file.drawString(15, 585, 'Материал 2')
            file.line(15, 583, 540, 583)
            file.setFont('NotoSans', 8)
            file.drawString(15, 573, 'реквизиты сертификатов их качество и безопасность)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 560, '4. Предъявлены документы, подтверждающие соответствие работ предъявляемым к ним '
                                     'требованиям')
            file.setFont('NotoSans', 12)
            file.drawString(15, 546, 'Качество 1')
            file.line(15, 544, 540, 544)
            file.setFont('NotoSans', 8)
            file.drawString(15, 534, ''
                                     '(исполнительные схемы и чертежи, результаты экспертиз, обследований, лабораторных')
            file.setFont('NotoSans', 12)
            file.drawString(15, 520, 'Качество 2')
            file.line(15, 518, 540, 518)
            file.setFont('NotoSans', 8)
            file.drawString(15, 508, 'и иных испытаний выполненных работ, проведенных в процессе строительного '
                                     'контроля)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 495, 'Даты: начала работ')
            file.drawString(135, 495, job_start_date)
            file.line(135, 493, 250, 493)
            file.drawString(35, 480, 'окончания работ')
            file.drawString(135, 480, job_end_date)
            file.line(135, 478, 250, 478)
            file.drawString(15, 465,
                            '6. Работы выполнены в соответствии с')
            file.setFont('NotoSans', 12)
            file.drawString(15, 451, 'Норма 1')
            file.line(15, 449, 540, 449)
            file.setFont('NotoSans', 8)
            file.drawString(130, 439,
                            '(наименования и структурные единицы технических регламентов,')
            file.setFont('NotoSans', 12)
            file.drawString(15, 425, 'Норма 2')
            file.line(15, 423, 540, 423)
            file.setFont('NotoSans', 8)
            file.drawString(130, 413,
                            'иных нормативных правовых актов, разделы проектной и/или рабочей документации)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 400,
                            '6. Разрешается производство последующих работ')
            file.setFont('NotoSans', 12)
            file.drawString(15, 386, job_next)
            file.line(15, 384, 540, 384)
            file.setFont('NotoSans', 8)
            file.drawString(130, 374,
                            '(наименование работ, конструкций, участков сетей инженерно-технического обеспечения)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 361,
                            'Дополнительные сведения')
            file.drawString(15, 348,
                            'Акт составлен в _____ экземплярах.')
            file.drawString(15, 335, 'Приложения:')
            file.drawString(15, 322,
                            'Представитель застройщика (технического заказчика, эксплуатирующей организации или реги-')
            file.drawString(15, 309, 'онального   оператора)  по вопросам  строительного контроля')
            file.setFont('NotoSans', 12)
            file.drawString(15, 295, 'Подпись 1')
            file.line(15, 293, 540, 293)
            file.setFont('NotoSans', 8)
            file.drawString(200, 283, '(фамилия, инициалы, подпись)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 270, 'Представитель лица, осуществляющего строительство')
            file.setFont('NotoSans', 12)
            file.drawString(15, 256, 'Подпись 2')
            file.line(15, 254, 540, 254)
            file.setFont('NotoSans', 8)
            file.drawString(200, 244, '(фамилия, инициалы, подпись)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 231, 'Представитель    лица,    осуществляющего    строительство,   по   вопросам '
                                     'строительного контроля')
            file.drawString(15, 218, ' (специалист по организации строительства)')
            file.setFont('NotoSans', 12)
            file.drawString(15, 204, 'Подпись 3')
            file.line(15, 202, 540, 202)
            file.setFont('NotoSans', 8)
            file.drawString(200, 192, '(фамилия, инициалы, подпись)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 179, 'Представитель лица, осуществляющего подготовку проектной документации')
            file.setFont('NotoSans', 12)
            file.drawString(15, 165, 'Подпись 4')
            file.line(15, 163, 540, 163)
            file.setFont('NotoSans', 8)
            file.drawString(200, 153, '(фамилия, инициалы, подпись)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 140, 'Представитель лица, выполнившего работы, подлежащие освидетельствованию')
            file.setFont('NotoSans', 12)
            file.drawString(15, 126, 'Подпись 5')
            file.line(15, 124, 540, 124)
            file.setFont('NotoSans', 8)
            file.drawString(200, 114, '(фамилия, инициалы, подпись)')
            file.setFont('NotoSansregular', 11)
            file.drawString(15, 101, 'Представители иных лиц')
            file.setFont('NotoSans', 12)
            file.drawString(15, 87, 'Подпись 6')
            file.line(15, 85, 540, 85)
            file.setFont('NotoSans', 8)
            file.drawString(200, 75, '(фамилия, инициалы, подпись)')

            file.showPage()


            # file.drawImage('file:///Users/iliavetchinin/PycharmProjects/AsBuilDoc/certifikat_sootvetstviya_obrazec_big_BEcOrtp.gif', 20, 20)
            # file.showPage()
            file.save()

            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.

            buffer.seek(0)

            return FileResponse(buffer, as_attachment=False, filename=number +'_'+job_name+ '.pdf')
