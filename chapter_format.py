import os
import sys

import base_import
import docx
from docx import Document
from docx.shared import Length, Pt, RGBColor, Inches
from docx.oxml.ns import qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_UNDERLINE
from datetime import datetime


def create_document_object(create_path, add_file_name):
    create_path = create_path + "\\" + add_file_name
    document_object = Document(create_path)
    return document_object


def create_title(document_object, charpter_name):

    return


if __name__ == "__main__":
    create_path = os.getcwd() + "\\" + "project_file"
    add_file_name = "summarybook.docx"
    print(create_path + "\\" + add_file_name)
    document_object = Document()  # 创建文件对象
    run_heading = document_object.add_heading("", level=1)
    run = run_heading.add_run("第一章First Chapter")  # 以追加段落格式方便后续修改
    run.font.underline = False  # 不需要添加下划线
    run_heading.paragraph_format.space_before = Pt(0)  # 设置段前
    run_heading.paragraph_format.space_after = Pt(0)  # 设置段后
    run_heading.paragraph_format.line_spacing = 1.5  # 设置行间距
    run.font.size = Pt(20)  # 设置1级标题文字的大小为“小四” 为12磅
    run.font.name = "Times New Roman"  # 设置英文字体
    run._element.rPr.rFonts.set(qn('w:eastAsia'), u"宋体")  # 设置中文字体
    run.font.color.rgb = RGBColor(0, 0, 0)  # 设置颜色

    # 创建内容
    content = document_object.add_paragraph()
    content.paragraph_format.space_before = Pt(10)  # 设置段前 0 磅
    content.paragraph_format.space_after = Pt(10)  # 设置段后 0 磅
    content.paragraph_format.line_spacing = 1.5  # 设置行间距为 1.5倍
    content.paragraph_format.first_line_indent = Inches(0) #段落首行缩进为 0.5英寸
    content.paragraph_format.first_line_indent = Inches(0)  # 相当于小四两个字符的缩进
    content_run = content.add_run("深度学习Python从入门到实践")
    content_run.bold = False  # 加粗
    content_run.font.size = Pt(16)
    content_run.font.name = "Times New Roman"  # 设置英文字体
    content_run._element.rPr.rFonts.set(qn('w:eastAsia'), u"宋体")  # 设置中文字体
    content_run.font.color.rgb = RGBColor(0, 0, 0)  # 设置颜色

    # 创建更新时间，添加时间
    header_section = document_object.sections[0]
    header_pos = header_section.header
    header_para = header_pos.paragraphs[0]
    currentDateAndTime = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    header_para.text = "该章节编写于:" + str(currentDateAndTime)

    document_object.save(create_path + "\\" + add_file_name)  # 创建文件保存地址

