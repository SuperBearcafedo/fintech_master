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
from reportlab.lib import colors  # 颜色模块
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Drawing  # 绘图工具
from reportlab.lib.units import cm  # 单位：cm


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

    def createPdfTitle(title):
        style = getSampleStyleSheet()
        ct = style['Heading1']
        ct.fontSize = 18
        ct.textColor = colors.green
        ct.alignment = 1
        ct.bold = True
        return Paragraph(title,ct)

    def createPdf_little_title(title):
        style = getSampleStyleSheet()
        ct = style['Normal']
        ct.fontSize = 15
        ct.leading = 30
        ct.textColor = colors.red
        return Paragraph(title,ct)
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

    def createPdfChart(data:list,ax:list,items:list):
        drawing = Drawing(500,250)
        bc = VerticalBarChart()
        bc.x = 45  # 整个图表的x坐标
        bc.y = 45  # 整个图表的y坐标
        bc.height = 200  # 图表的高度
        bc.width = 350  # 图表的宽度
        bc.data = data
        bc.strokeColor = colors.black  # 顶部和右边轴线的颜色
        bc.valueAxis.valueMin = 5000  # 设置y坐标的最小值
        bc.valueAxis.valueMax = 26000  # 设置y坐标的最大值
        bc.valueAxis.valueStep = 2000  # 设置y坐标的步长
        bc.categoryAxis.labels.dx = 2
        bc.categoryAxis.labels.dy = -8
        bc.categoryAxis.labels.angle = 20
        bc.categoryAxis.categoryNames = ax

        # 图示
        leg = Legend()
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = 475  # 图例的x坐标
        leg.y = 240
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = items
        drawing.add(leg)
        drawing.add(bc)
        return drawing

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

    #添加标题
    content.append(pdf.createPdfTitle('We are the champion'))
    #添加小标题
    content.append(pdf.createPdfTitle(''))
    content.append(pdf.createPdf_little_title('good idea'))
    #添加段落
    content.append(pdf.createPdfParagph('Python'))

    #添加表格:先初始化再
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    content.append(pdf.createPdfForm(data))

    #生成图表
    content.append(pdf.createPdfTitle(''))
    content.append(pdf.createPdf_little_title('employment situation'))
    data =[(25400, 12900, 20100, 20300, 20300, 17400), (15800, 9700, 12982, 9283, 13900, 7623)]
    ax_data = ['BeiJing', 'ChengDu', 'ShenZhen', 'ShangHai', 'HangZhou', 'NanJing']
    leg_items = [(colors.red, 'average'), (colors.green, 'numbers')]

    content.append(pdf.createPdfChart(data,ax_data,leg_items))

    #生成pdf文件
    doc = SimpleDocTemplate("last.pdf")
    doc.build(content)






