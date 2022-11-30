# -*- coding: utf-8 -*-
import os
import sys
import traceback
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


if __name__ == "__main__":
    create_path = os.path.join(os.getcwd(), "project_file")
    add_file_name = "summarybook.pdf"
    title_name = "第一章/First Chapter"
    chapter_name = "深度学习Python从入门到实践111"

    # # 调用模板，创建指定名称的pdf文档
    doc = SimpleDocTemplate("Hello.pdf")
    styles = getSampleStyleSheet()  #获取模板表格
    style = styles['Normal']        #指定模板
    story = []                      #初始化列表
    # # 将段落添加到内容中
    story.append(Paragraph("this is the first Document!", style))
    doc.build(story)                #将内容输出到PDF中
    #
    stylesheet = getSampleStyleSheet()
    titleStyele = stylesheet['Title']
    storytitle = []  # 初始化列表
    # 将段落添加到内容中
    storytitle.append(Paragraph("this is the second Document!", titleStyele))
    doc.build(storytitle)  # 将内容输出到PDF中

    # # 初始化表格内容
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    # # 根据内容创建表格
    t = Table(data)
    t.setStyle(TableStyle(
        [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
         ('BOX', (0, 0), (-1, -1), 2, colors.black),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.yellow),
         ('LINEAFTER', (0, 0), (0, -1), 2, colors.blue),
         ('ALIGN', (1, 1), (-1, -1), 'RIGHT')]
    ))
    # #补充：
    # # FONTNAME：字体名称
    # # FONTSIZE：字体大小
    # # LEADING：行间距
    # # TEXTCOLOR：字体颜色
    # # ALIGNMENT：水平对齐方式（可选值："LEFT"，”RIGHT“，”CENTER“）
    # # LEFTPADDING：左边填充
    # # RIGHTPADDING：右边填充
    # # BOTTOMPADDING：底部填充
    # # TOPPADDING：顶部填充
    # # BACKGROUND：背景色
    # # VALIGN：垂直对齐方式（可选值："TOP"，“MIDDLE”，“BOTTOM”）
    # # GRID：表格颜色，被指定的行列中的所有子行和子列都被设置成相应颜色
    # # INNERGRID：表格颜色，仅仅修改指定的子行和子列的相应颜色（不包括边框）
    # # BOX：边框颜色，被指定的边框的颜色
    # # LINEBELOW：指定块底部的行颜色
    # # LINEAFTER：指定块右边的行颜色。


    # # 将表格添加到内容中
    #story.append(t)
    # # 将内容输出到PDF中
     #doc.build(story)

    doc = SimpleDocTemplate("Hello.pdf")
    styles = getSampleStyleSheet()
    style = styles['Normal']
    story = []
    #图片插入:插入需要指定长宽，自适应做的不好
    t = Image("C:\\Users\\89706\\Desktop\\mofang.jpg",width=210-doc.rightMargin-doc.leftMargin,height=293-doc.topMargin-doc.bottomMargin)
    story.append(t)
    doc.build(story)
