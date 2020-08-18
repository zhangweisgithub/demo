# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from jinja2 import Template

key = {'setup': {'bucket_name': 'ddwY3ZITmP8yi4K3PKUT8BmIfaX2kXihgn9miBfVuDSthXe', 'db_type': 'alert',
                 'feature': '[object Object]', 'feature_topic': 'stream.features.face_24901',
                 'feature_version': '24901', 'gat1400_host': '172.20.25.201',
                 'gat1400_platform_source_type': 'FP_GAT1400_PLATFORM', 'gat1400_port': '9070',
                 'gat1400_server_id': '44200000005030000005', 'headers_token_key': '"token"',
                 'hk_camera_ip': '10.9.76.13', 'host': '172.20.26.175:30443',
                 'iis_component_config_path': '/etc/kubernetes/apps/engine-image-ingress-service/default',
                 'object_type_body': 'OBJECT_FACE', 'password': 'V1p3r1@#$%',
                 'pre_db_id': 'e6d3a103-d29f-4ea2-8a90-da8925426000', 'pre_name': 'viper_pre',
                 'rand_file_name': 'material/Viper/API/pxm/photos/clear_company/source/STTT_1_314931_alarm.jpg',
                 'repo_name': 'vats', 'sdk_version': '24802', 'set_id': 6114,
                 'static_feature_id': 'e6d3a103d29f4ea28a90da89254260010000000000003b58', 'struct_object_type': 'face',
                 'user': 'root', 'viper_snapshot_host': 'http://172.20.26.139:31070', 'protocol': 'HTTPS',
                 'headers': '',
                 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyb290IiwibmJmIjoxNTk1MzIyMzA1LCJleHAiOjE1OTUzMjk1MDV9.nibsasBU6lnm61mfsfFITYIwBYS30fh7SIezJDUTyo0',
                 'expires': 7200,
                 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyb290IiwibmJmIjoxNTk1MzIyMzA1LCJleHAiOjE1OTUzMjk1MDV9.nibsasBU6lnm61mfsfFITYIwBYS30fh7SIezJDUTyo0',
                 'scripts_abspath': '/platform/backend-api/scripts/vats',
                 'cert_file': '/platform/backend-api/scripts/vats/viper_interface/ca.pem'}}


def recursive_jinja_parse(value):
    """
    内嵌在rend_dict_value的函数，模板替换功能
    :param value:
    :param args:
    :return:
    """
    regx = r"`<[^`]+>`"
    units = re.findall(regx, value)
    for each in units:
        each = str(each)
        try:
            tpl = Template(each, variable_start_string="`<", variable_end_string=">`")
            val = tpl.render(**key)
        except:
            print("error")
            pass
        value = value.replace(each, val)
    if re.findall(regx, value):
        value = recursive_jinja_parse(value)
    return value


if __name__ == '__main__':
    key = {'setup': {'bucket_name': 'ddwY3ZITmP8yi4K3PKUT8BmIfaX2kXihgn9miBfVuDSthXe', 'db_type': 'alert',
                     'feature': '[object Object]', 'feature_topic': 'stream.features.face_24901',
                     'feature_version': '24901', 'gat1400_host': '172.20.25.201',
                     'gat1400_platform_source_type': 'FP_GAT1400_PLATFORM', 'gat1400_port': '9070',
                     'gat1400_server_id': '44200000005030000005', 'headers_token_key': '"token"',
                     'hk_camera_ip': '10.9.76.13', 'host': '172.20.26.175:30443',
                     'iis_component_config_path': '/etc/kubernetes/apps/engine-image-ingress-service/default',
                     'object_type_body': 'OBJECT_FACE', 'password': 'V1p3r1@#$%',
                     'pre_db_id': 'e6d3a103-d29f-4ea2-8a90-da8925426000', 'pre_name': 'viper_pre',
                     'rand_file_name': 'material/Viper/API/pxm/photos/clear_company/source/STTT_1_314931_alarm.jpg',
                     'repo_name': 'vats', 'sdk_version': '24802', 'set_id': 6114,
                     'static_feature_id': 'e6d3a103d29f4ea28a90da89254260010000000000003b58',
                     'struct_object_type': 'face', 'user': 'root', 'viper_snapshot_host': 'http://172.20.26.139:31070',
                     'protocol': 'HTTPS', 'headers': '',
                     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyb290IiwibmJmIjoxNTk1MzIyMzA1LCJleHAiOjE1OTUzMjk1MDV9.nibsasBU6lnm61mfsfFITYIwBYS30fh7SIezJDUTyo0',
                     'expires': 7200,
                     'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyb290IiwibmJmIjoxNTk1MzIyMzA1LCJleHAiOjE1OTUzMjk1MDV9.nibsasBU6lnm61mfsfFITYIwBYS30fh7SIezJDUTyo0',
                     'scripts_abspath': '/platform/backend-api/scripts/vats',
                     'cert_file': '/platform/backend-api/scripts/vats/viper_interface/ca.pem'}}
    each = "`<setup.user>`"
    # tpl = Template(each, variable_start_string="`<", variable_end_string=">`")
    # val = tpl.render({})
    # print(val)
    recursive = recursive_jinja_parse(each)
    print(recursive)
