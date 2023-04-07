import io
from urllib import request

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# 引入中文字符集
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))

PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]


def print_exam(exam, singles, multiples, blanks, subjectives):
    doc = SimpleDocTemplate('media/pdf/' + exam.title + '.pdf', pagesize=A4)
    # 添加段落
    story = [Spacer(1, 2)]

    body_style = ParagraphStyle(
        name="bodyStyle",
        leftIndent=0,
        fontName='SimSun',
        fontSize=12,
        textColor=colors.black,
        spaceAfter=5,
    )
    title_style = ParagraphStyle(
        name="titleStyle",
        fontName='SimSun',
        fontSize=15,
        leftIndent=-30,
        spaceBefore=10,
        spaceAfter=7,
    )

    def draw_choices(singles, multiples):
        choice_style = ParagraphStyle(
            name="choiceStyle",
            fontName='SimSun',
            leftIndent=20,
            fontSize=12,
            textColor=colors.black,
            spaceAfter=3,
        )
        story.append(Paragraph("一、单项选择", title_style))
        num = 1
        for choice in singles:
            story.append(Spacer(1, 20))
            story.append(Paragraph(str(num) + ". " + choice.body, body_style))
            story.append(Spacer(1, 10))
            story.append(Paragraph("A." + choice.choices_A, choice_style))
            story.append(Paragraph("B." + choice.choices_B, choice_style))
            story.append(Paragraph("C." + choice.choices_C, choice_style))
            story.append(Paragraph("D." + choice.choices_D, choice_style))
            num = num + 1

        story.append(Paragraph("二、多项选择", title_style))
        num = 1
        for choice in multiples:
            story.append(Spacer(1, 20))
            story.append(Paragraph(str(num) + ". " + choice.body, body_style))
            story.append(Spacer(1, 10))
            story.append(Paragraph("A." + choice.choices_A, choice_style))
            story.append(Paragraph("B." + choice.choices_B, choice_style))
            story.append(Paragraph("C." + choice.choices_C, choice_style))
            story.append(Paragraph("D." + choice.choices_D, choice_style))
            num = num + 1

    def draw_blanks(blanks):
        story.append(Paragraph("二、填空题", title_style))
        num = 1
        for blank in blanks:
            story.append(Spacer(1, 20))
            story.append(Paragraph(str(num) + ". " + blank.body, body_style))
            num = num + 1

    def draw_subjectives(subjectives):
        story.append(Paragraph("三、客观题", title_style))
        num = 1
        for subjective in subjectives:
            story.append(Spacer(1, 20))
            story.append(Paragraph(str(num) + ". " + subjective.body, body_style))
            num = num + 1

    def my_first_page(c: canvas.Canvas, doc):
        c.saveState()
        c.setFont('SimSun', 30)
        c.drawCentredString(300, PAGE_HEIGHT - 50, exam.title)
        c.line(30, PAGE_HEIGHT - 70, PAGE_WIDTH - 30, PAGE_HEIGHT - 70)
        c.restoreState()
        draw_choices(singles, multiples)
        draw_blanks(blanks)
        draw_subjectives(subjectives)

    doc.build(story, onFirstPage=my_first_page)
    return doc.filename
