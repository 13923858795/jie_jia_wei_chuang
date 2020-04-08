# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import os
from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from myflaskapp.models.Config import Config
from myflaskapp.forms.ConfigForm import ConfigForm
from myflaskapp.utils import flash_errors
from myflaskapp.services.ConfigServices import ConfigServices
from myflaskapp.services.ExcelServices import ExcelServices

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/', methods=['GET', 'POST'])
def home():

    """Home page."""
    model = Config.query.filter_by(is_use=1).first()
    form = ConfigForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():

            if model:
                ConfigServices.edit(model, form)
            else:
                ConfigServices.create(form)
            flash('保存成功')
            return redirect(url_for('public.home'))
        else:
            flash_errors(form)

    if model:

        # form.UCL.data = model.UCL
        # form.LCL.data = model.LCL
        # form.LSL.data = model.LSL
        form.IP_address.data = model.IP_address
        form.IP_port.data = model.IP_port
        form.CSV_data.data = model.CSV_data
        # form.Room.data = model.Room
        form.TestPoint.data = model.TestPoint
        form.CSV_file.data = model.CSV_file
        form.Excel_output.data = model.Excel_output
        # form.Break_points.data = model.Break_points

        # print('1' if model.only_pipe else '0')

    return render_template('public/home.html', form=form)


@blueprint.route('/csv/<string:key_1>/<string:key_2>/<string:key_3>/<string:key_4>', methods=['GET'])
def analysis_csv(key_1, key_2, key_3, key_4):
    ExcelServices(key_1, key_2, key_3, key_4)

    return jsonify(f"{key_1}_{key_2}_{key_3}_{key_4}")




