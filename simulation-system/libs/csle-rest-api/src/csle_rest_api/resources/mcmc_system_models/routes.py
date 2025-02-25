"""
Routes and sub-resources for the /mcmc-system-models resource
"""
from typing import Tuple
import csle_common.constants.constants as constants
from csle_common.metastore.metastore_facade import MetastoreFacade
from flask import Blueprint, jsonify, request, Response
import csle_rest_api.constants.constants as api_constants
import csle_rest_api.util.rest_api_util as rest_api_util

# Creates a blueprint "sub application" of the main REST app
mcmc_system_models_bp = Blueprint(
    api_constants.MGMT_WEBAPP.MCMC_SYSTEM_MODELS_RESOURCE, __name__,
    url_prefix=f"{constants.COMMANDS.SLASH_DELIM}{api_constants.MGMT_WEBAPP.MCMC_SYSTEM_MODELS_RESOURCE}")


@mcmc_system_models_bp.route("", methods=[api_constants.MGMT_WEBAPP.HTTP_REST_GET,
                                          api_constants.MGMT_WEBAPP.HTTP_REST_DELETE])
def mcmc_system_models() -> Tuple[Response, int]:
    """
    The /mcmc-system-models resource.

    :return: A list of system-models or a list of ids of the models or deletes the models
    """
    requires_admin = False
    if request.method == api_constants.MGMT_WEBAPP.HTTP_REST_DELETE:
        requires_admin = True
    authorized = rest_api_util.check_if_user_is_authorized(request=request, requires_admin=requires_admin)
    if authorized is not None:
        return authorized

    if request.method == api_constants.MGMT_WEBAPP.HTTP_REST_GET:
        # Check if ids query parameter is True, then only return the ids and not the whole list of mcmc
        # system models
        ids = request.args.get(api_constants.MGMT_WEBAPP.IDS_QUERY_PARAM)
        if ids is not None and ids:
            return mcmc_system_models_ids()

        models = MetastoreFacade.list_mcmc_system_models()
        models_dicts = list(map(lambda x: x.to_dict(), models))
        response = jsonify(models_dicts)
        response.headers.add(api_constants.MGMT_WEBAPP.ACCESS_CONTROL_ALLOW_ORIGIN_HEADER, "*")
        return response, constants.HTTPS.OK_STATUS_CODE
    elif request.method == api_constants.MGMT_WEBAPP.HTTP_REST_DELETE:
        models = MetastoreFacade.list_mcmc_system_models()
        for model in models:
            MetastoreFacade.remove_mcmc_system_model(model)
        response = jsonify({})
        response.headers.add(api_constants.MGMT_WEBAPP.ACCESS_CONTROL_ALLOW_ORIGIN_HEADER, "*")
        return response, constants.HTTPS.OK_STATUS_CODE
    return (jsonify({api_constants.MGMT_WEBAPP.REASON_PROPERTY: "HTTP method not supported"}),
            constants.HTTPS.BAD_REQUEST_STATUS_CODE)


def mcmc_system_models_ids() -> Tuple[Response, int]:
    """
    :return: An HTTP response with all system models ids
    """
    models_ids = MetastoreFacade.list_mcmc_system_models_ids()
    response_dicts = []
    for tup in models_ids:
        response_dicts.append({
            api_constants.MGMT_WEBAPP.ID_PROPERTY: tup[0],
            api_constants.MGMT_WEBAPP.EMULATION_PROPERTY: tup[1],
            api_constants.MGMT_WEBAPP.STATISTIC_ID_PROPERTY: tup[2]
        })
    response = jsonify(response_dicts)
    response.headers.add(api_constants.MGMT_WEBAPP.ACCESS_CONTROL_ALLOW_ORIGIN_HEADER, "*")
    return response, constants.HTTPS.OK_STATUS_CODE


@mcmc_system_models_bp.route("/<model_id>", methods=[api_constants.MGMT_WEBAPP.HTTP_REST_GET,
                                                     api_constants.MGMT_WEBAPP.HTTP_REST_DELETE])
def mcmc_system_model(model_id: int) -> Tuple[Response, int]:
    """
    The /system-models/id resource.

    :param model_id: the id of the model

    :return: The given model or deletes the model
    """
    requires_admin = False
    if request.method == api_constants.MGMT_WEBAPP.HTTP_REST_DELETE:
        requires_admin = True
    authorized = rest_api_util.check_if_user_is_authorized(request=request, requires_admin=requires_admin)
    if authorized is not None:
        return authorized

    model = MetastoreFacade.get_mcmc_system_model_config(id=model_id)
    response = jsonify({})
    if model is not None:
        if request.method == api_constants.MGMT_WEBAPP.HTTP_REST_GET:
            response = jsonify(model.to_dict())
        else:
            MetastoreFacade.remove_mcmc_system_model(mcmc_system_model=model)
    response.headers.add(api_constants.MGMT_WEBAPP.ACCESS_CONTROL_ALLOW_ORIGIN_HEADER, "*")
    return response, constants.HTTPS.OK_STATUS_CODE
