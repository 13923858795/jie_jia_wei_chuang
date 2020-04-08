import datetime as dt
from myflaskapp.models.Config import Config


class ConfigServices:

    @classmethod
    def edit(cls, model, form):

        # model.UCL = form.UCL.data
        # model.LCL = form.LCL.data
        # model.LSL = form.LSL.data
        model.IP_address = form.IP_address.data
        model.IP_port = form.IP_port.data
        model.CSV_data = form.CSV_data.data
        model.TestPoint = form.TestPoint.data

        # model.Room = form.Room.data
        model.CSV_file = form.CSV_file.data
        model.Excel_output = form.Excel_output.data
        # model.Break_points = form.Break_points.data
        model.created_at = dt.datetime.now()
        model.only_pipe = 1
        model.save()
        return True

    @classmethod
    def create(cls, form):
        model = Config.create(
            # UCL=form.UCL.data,
            # LCL=form.LCL.data,
            # LSL=form.LSL.data,
            IP_address=form.IP_address.data,
            IP_port=form.IP_port.data,
            CSV_data=form.CSV_data.data,
            TestPoint=form.TestPoint.data,
            CSV_file=form.CSV_file.data,
            Excel_output=form.Excel_output.data,
            Break_points=form.Break_points.data,
            is_use=1,
            Room=form.Room.data
        )
        return model

    @classmethod
    def get_model(cls):
        model = Config.query.filter_by(is_use=1).first()
        return model
