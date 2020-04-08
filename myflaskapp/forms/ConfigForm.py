# -*- coding: utf-8 -*-
"""User forms."""
import os
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length



class ConfigForm(FlaskForm):
    """Register form."""
    # # USL = StringField('USL', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # UCL = StringField('UCL', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # # T = StringField('T', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # LCL = StringField('LCL', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # LSL = StringField('LSL', validators=[DataRequired(u"不能为空"), Length(max=100)])
    IP_address = StringField('IP 地址', validators=[DataRequired(u"不能为空"), Length(max=100)])
    IP_port = StringField('IP 端口', validators=[DataRequired(u"不能为空"), Length(max=100)])
    CSV_data = StringField('CSV 数据栏', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # Room = StringField('车间名', validators=[DataRequired(u"不能为空"), Length(max=100)])
    #
    # Furnace = StringField('每炉片数', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # Pieces = StringField('每片点数', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # MIN = IntegerField('最小值', validators=[DataRequired(u"必须为数字")])
    # MAX = IntegerField('最大值', validators=[DataRequired(u"必须为数字")])
    # Set = IntegerField('默认值', validators=[DataRequired(u"必须为数字")])
    # Platform = StringField('机台名1', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # Pipe = StringField('机台名2', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # Version = StringField('版本号', validators=[DataRequired(u"不能为空"), Length(max=100)])
    TestPoint = StringField('测试点', validators=[DataRequired(u"不能为空"), Length(max=100)])

    CSV_file = StringField('CSV 文件夹', validators=[DataRequired(u"不能为空"), Length(max=100)])
    Excel_output = StringField('EXCEL输出文件夹', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # Break_points = StringField('时间端点', validators=[DataRequired(u"不能为空"), Length(max=100)])
    # only_pipe = SelectField('仅使用炉管', choices=[('0', '否'), ('1', '是')])

    submit = SubmitField('确认')

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ConfigForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(ConfigForm, self).validate()
        if not initial_validation:
            return False

        if not os.path.exists(self.CSV_file.data):
            self.CSV_file.errors.append('csv 文件夹路径不存在')
            return False

        out_path = self.Excel_output.data
        _path = out_path.split("\\")[:-1]

        _path = "\\".join(_path)
        if not os.path.exists(_path):
            self.Excel_output.errors.append('excel 文件夹路径不存在')
            return False

        return True

