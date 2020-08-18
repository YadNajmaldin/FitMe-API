import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

fit = Blueprint('fits', 'fit')


@fit.route('/', methods=["GET"])
def get_all_fits():
    try:
        fits = [model_to_dict(fit) for fit in models.Fit.select()]
        # print(dogs)
        return jsonify(data=fits, status={'code': 200, 'message': 'Success'})
    except:
        return jsonify(data={}, status={'code': 500, 'message': 'Error getting resources'})

    
@fit.route('/', methods=["POST"])
def create_fits():
    body = request.get_json()
    print(body)
    new_fit = models.Fit.create(**body)
    fit_data = model_to_dict(new_fit)
    return jsonify(data=fit_data, status={'code': 200, 'message': 'Success'})

@fit.route('/<id>', methods=["GET"])
def get_one_fit(id):
    print(id, 'this is the id')
    fit = models.Fit.get_by_id(id)
    fit_dict = model_to_dict(fit)
    return jsonify(data=fit_dict, status={"code": 200, "message": "Success"})


@fit.route('/<id>', methods=['PUT'])
def update_fit(id):
    payload = request.get_json()
    update_query = models.Fit.update(**payload).where(models.Fit.id == id)

    update_query.execute()

    update_fit = models.Fit.get_by_id(id)

    return jsonify(data=model_to_dict(update_fit), message="Successfully update dog with id {}".format(id), status={'code': 200, 'message': 'Success'})


@fit.route('/<id>', methods=['DELETE'])
def delete_fit(id):
    delete_query = models.Fit.delete().where(models.Fit.id == id)
    delete_query.execute() # you need this for delete and update
    return jsonify(
        data={},
        message="Successfully deleted dog with id {}".format(id),
        status={'code': 200, 'message': 'Success'}
    )