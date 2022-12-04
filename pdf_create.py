# -*- coding: utf-8 -*-
import os
import sys
import traceback

from docx.styles import style

import base_import
import docx
from docx import Document
from docx.shared import Length, Pt, RGBColor, Inches
from docx.oxml.ns import qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_UNDERLINE
from datetime import datetime


#  此处需要添加PDF report的代码
import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet

#新建段落格式类
class ParagraphStyle():
    defaults = {
        'fontName':'_baseFontName',#字体名称
        'fontSize':10,#字体大小
        'leading':12,#行间距
        'leftIndent':0,#左缩进
        'rightIndent':0,#右缩进
        'firstLineIndent':0,#首行缩进
        'alignment':'TA_LEFT',#对齐方式
        'spaceBefore':0,#段前间隙
        'spaceAfter':0,#段后间隙
        'bulletFontName':'_baseFontName',#列表名称
        'bulletFontSize':10,#列表字体大小
        'bulletIndent':0,#列表缩进
        'bulletColor':'black',#列表颜色
        'textColor': 'black',#字体颜色
        'backColor':None,#背景色
        'wordWrap':None,#
        'borderWidth': 0,#边框粗细
        'borderPadding': 0,#边框间距
        'borderColor': None,#边框颜色
        'borderRadius': None,
        'allowWidows': 1,
        'allowOrphans': 0,
        'textTransform': None,  # uppercase lowercase (captitalize not yet) or None or absent
        'endDots': None,
        'splitLongWords': 1,

    }
class pdf:
    def __init__(self, create_path, add_file_name, title_name, chapter_name):
        self.document_object = Document()  # 创建文件对象
        self.create_path = create_path
        self.add_file_name = add_file_name
        self.tn = title_name
        self.cn = chapter_name

    def createPdfParagph(text:str):
        # # 获取普通样式
        # ct = styles['Normal']
        # ct.fontName = 'SimSun'
        # ct.fontSize = 12
        # ct.wordWrap = 'CJK'  # 设置自动换行
        # ct.alignment = 0  # 左对齐
        # ct.firstLineIndent = 32  # 第一行开头空格
        # ct.leading = 25
        # return Paragraph

        # 获取所有样式表
        style = getSampleStyleSheet()
        titleStyele = style['Title']

        # 将段落添加到内容中
        return Paragraph(text, titleStyele)

    def createPdfImg(img):
        styles = getSampleStyleSheet()
        style = styles['Normal']
        #图片插入:插入需要指定长宽，自适应做的不好，将固定路径改为变量获取
        img = Image(picture_path, width=370, height=210)
        return img

    def createPdfForm(data):
        data = Table(data)
        data.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
             ('BOX', (0, 0), (-1, -1), 2, colors.black),
             ('LINEBELOW', (0, 0), (-1, 0), 2, colors.yellow),
             ('LINEAFTER', (0, 0), (0, -1), 2, colors.blue),
             ('ALIGN', (1, 1), (-1, -1), 'RIGHT')]
        ))
        # 补充：
        # FONTNAME：字体名称
        # FONTSIZE：字体大小
        # LEADING：行间距
        # TEXTCOLOR：字体颜色
        # ALIGNMENT：水平对齐方式（可选值："LEFT"，”RIGHT“，”CENTER“）
        # LEFTPADDING：左边填充
        # RIGHTPADDING：右边填充
        # BOTTOMPADDING：底部填充
        # TOPPADDING：顶部填充
        # BACKGROUND：背景色
        # VALIGN：垂直对齐方式（可选值："TOP"，“MIDDLE”，“BOTTOM”）
        # GRID：表格颜色，被指定的行列中的所有子行和子列都被设置成相应颜色
        # INNERGRID：表格颜色，仅仅修改指定的子行和子列的相应颜色（不包括边框）
        # BOX：边框颜色，被指定的边框的颜色
        # LINEBELOW：指定块底部的行颜色
        # LINEAFTER：指定块右边的行颜色。
        return data


if __name__ == "__main__":
    create_path = os.path.join(os.getcwd(), "project_file")
    add_file_name = "summarybook.pdf"
    title_name = "第一章/First Chapter"
    chapter_name = "深度学习Python从入门到实践111"

    pdf(create_path, add_file_name, title_name, chapter_name)
    # 创建一个空列表
    content = list()

    #添加图片--引用类中方法createPdf
    current_pdf_path = os.getcwd()
    print("current_path " + current_pdf_path)
    picture_path = os.path.join(current_pdf_path, "pictures", "mofang.jpg")
    content.append(pdf.createPdfImg(picture_path))

    # 添加段落
    content.append(pdf.createPdfParagph('Python'))

    #添加表格:先初始化再
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    content.append(pdf.createPdfForm(data))

    #生成pdf文件
    doc = SimpleDocTemplate("last.pdf")
    doc.build(content)






