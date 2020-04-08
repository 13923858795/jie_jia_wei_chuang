# -*- coding: utf-8 -*-
"""Create an application instance."""

from myflaskapp.app import create_app


def run_web():
    print("web----------------- 进程启动")
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=80)





run_web()