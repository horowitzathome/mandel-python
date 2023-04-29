from flask import Blueprint, jsonify, request
from libs.mandelbrot import mandel

bp = Blueprint('mb_service', __name__)

@bp.route('/actuator/health', methods=['GET'])
def health():
    return 'health'

@bp.route('/mandel_python/mandel_text_memory/<int:max_iter>/<int:height>/<int:width>', methods=['GET'])
def get_mandelbrot(max_iter, height, width):
    mandel_result = mandel(max_iter, height, width)
    #return jsonify({"result": mandel_result.result})
    return mandel_result.result