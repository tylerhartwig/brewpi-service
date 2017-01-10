from flask import jsonify

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from brewpi_service import app

from .models import ClockDevice
from .schemas import (
    clock_schema,
    clocks_schema
)


@app.route('/clocks/')
def clocks():
    """
    List Clock Devices
    """
    all_clocks = ClockDevice.query.all()
    result = clocks_schema.dump(all_clocks)
    return jsonify(result.data)

@app.route('/clocks/<id>')
def clock_detail(id):
    """
    Detail a given Clock Device
    """
    clock = ClockDevice.query.get(id)
    return clock_schema.jsonify(clock)
