# Author : SenYan
# Data : 2019/6/25 11:51
api_parameters = {"name": "body", "in": "body", "required": True, "schema":
    {"$ref":
         {"type": "object", "properties":
             {"camera_ids":
                  {"type": "array"
                      , "items": {"$ref": {"type": "object", "properties": {
                      "region_id": {"type": "integer", "format": "int32", "description": "摄像头所属区域id, 0\
号id系统保留, 范围: [1, 16383]."}, "camera_idx": {"type": "integer", "format": "int32", "description": "摄像头在区域region_id内的下标, 0号id\
系统保留, 范围: [1, 127]."}}, "description": "系统摄像头唯一标识, 一般由业务系统统一分配和管理."}}, "description": "摄像头过滤标识, 目前暂只\
支持1路, camera_ids不能多于1个id."},
              "period": {"$ref": {"type": "object", "properties": {"start": {"type": "string", "format": "date-time",
                                                                             "description": "开始时间, 区间包含."},
                                                                   "end": {"type": "string", "format": "date-time",
                                                                           "description": "结束时间, 区间不包含."}
                                                                   },
                                  "description": "TimeRange表示一段时间区间 [start, end) , 时间戳为UTC时间.\n时间戳JSON表示形式为RFC 3339格式, 如: \"1972-01-01T10:00:20.021Z\"."},
                         "descr\iption": "检索时间范围."},
              "page_size": {"type": "integer", "format": "int32", "description": "分页大小, 范围：[10, 100]."},
              "marker": {"type": "string", "format": "byte",
                         "description": "分页标志, 由ListFeaturesResponse返回, 第一页传空. 默认为空."},
              "reversed": {"type": "boolean", "format": "boolean", "description": "为False时按时间顺序输出, 为True时按时间倒序输出."}
              }
          }
     }
                  }

body = api_parameters.get("body")
import random
import time
import pysnooper


class BodyIgnore:
    def __init__(self):
        self.str_base = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h',
                         'g', 'f', 'e', 'd', 'c', 'b', 'a']
        self.str_email = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h',
                          'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # @pysnooper.snoop(depth=2)
    def key_ignore_value(self, input_json, base_data, api_parameter_key=None, api_parameter_value=None):
        """递归解析json格式下的数据"""
        if isinstance(input_json, dict):
            if "name" in input_json.keys():
                if input_json.get("name") == "email":
                    api_parameter_key = "email"
                    api_parameter_value = ''.join(random.sample(self.str_email, 9) + "@" + ".com")
                    base_data.update({api_parameter_key: api_parameter_value})
                    return base_data
                else:
                    if input_json.get("in") == "body":
                        api_parameter_values = input_json.get("schema")
                        api_parameter_key = input_json.get("name")
                        api_parameter_value = {}
                        base_data.update({api_parameter_key: api_parameter_value})
                        print(base_data)
                        if api_parameter_values:
                            self.key_ignore_value(api_parameter_values, base_data, api_parameter_key=api_parameter_key,
                                                  api_parameter_value=base_data[api_parameter_key])
                    else:
                        if input_json.get("type") == "string":
                            if input_json.get("format") == "date-time":
                                def strTimeProp(start, end, prop, frmt):
                                    stime = time.mktime(time.strptime(start, frmt))
                                    etime = time.mktime(time.strptime(end, frmt))
                                    ptime = stime + prop * (etime - stime)
                                    return int(ptime)

                                def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
                                    return time.strftime(frmt, time.localtime(
                                        strTimeProp(start, end, random.random(), frmt)))

                                start = '2019-01-01 00:00:00'
                                end = '2019-07-10 00:00:00'
                                api_parameter_key = input_json.get("name")
                                api_parameter_value = randomDate(start, end)
                                base_data.update({api_parameter_key: api_parameter_value})
                                print("58", base_data)
                            elif input_json.get("format") == "int32" or input_json.get("format") == "int64":
                                api_parameter_key = input_json.get("name")
                                api_parameter_value = random.randint(1, 500)
                                base_data.update({api_parameter_key: api_parameter_value})
                                print("63", base_data)
                            else:
                                api_parameter_key = input_json.get("name")
                                api_parameter_value = ''.join(random.sample(self.str_base, 6))
                                base_data.update({api_parameter_key: api_parameter_value})
                                print("68", base_data)
                        elif input_json.get("type") == "number" or input_json.get("type") == "integer":
                            api_parameter_key = input_json.get("name")
                            api_parameter_value = random.randint(1, 500)
                            base_data.update({api_parameter_key: api_parameter_value})
                            print("73", base_data)
                        elif input_json.get("type") == "boolean":
                            api_parameter_key = input_json.get("name")
                            api_parameter_value = random.choice([True, None])
                            base_data.update({api_parameter_key: api_parameter_value})
                            print("78", base_data)
                        elif input_json.get("type") == "array":
                            api_parameter_values = input_json.get("items")
                            api_parameter_key = input_json.get("name")
                            base_data.update({api_parameter_key: {}})
                            if api_parameter_values:
                                self.key_ignore_value(api_parameter_values, base_data,
                                                      api_parameter_key=api_parameter_key,
                                                      api_parameter_value=base_data[api_parameter_key])
                        elif input_json.get("type") == "file":
                            api_parameter_key = input_json.get("name")
                            api_parameter_value = "file"
                            base_data.update({api_parameter_key: api_parameter_value})
                            print("89", base_data)

            else:
                if "$ref" in input_json.keys():
                    api_parameter_values = input_json.get("$ref")
                    base_data.update({api_parameter_key: {}})
                    if api_parameter_values:
                        self.key_ignore_value(api_parameter_values, base_data, api_parameter_key=api_parameter_key,
                                              api_parameter_value=base_data[api_parameter_key])
                else:
                    if input_json.get("type") == "object" and "properties" in input_json.keys():
                        api_parameter_values = input_json.get("properties")
                        api_parameter_key = api_parameter_key
                        api_parameter_value = api_parameter_value
                        if isinstance(api_parameter_values, dict):
                            for key, value in api_parameter_values.items():
                                if isinstance(value, dict):
                                    if "type" in value.keys():
                                        if value.get("type") == "string":
                                            if value.get("format") == "date-time":
                                                def strTimeProp(start, end, prop, frmt):
                                                    stime = time.mktime(time.strptime(start, frmt))
                                                    etime = time.mktime(time.strptime(end, frmt))
                                                    ptime = stime + prop * (etime - stime)
                                                    return int(ptime)

                                                def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
                                                    return time.strftime(frmt, time.localtime(
                                                        strTimeProp(start, end, random.random(), frmt)))

                                                start = '2019-01-01 00:00:00'
                                                end = '2019-07-10 00:00:00'
                                                value_key = key
                                                value_value = randomDate(start, end)
                                                api_parameter_value.update({value_key: value_value})
                                                base_data.update({api_parameter_key, api_parameter_value})
                                                print("124", base_data)
                                            elif input_json.get("format") == "int32" or input_json.get(
                                                    "format") == "int64":
                                                value_key = key
                                                value_value = random.randint(1, 500)
                                                api_parameter_value.update({value_key: value_value})
                                                base_data.update({api_parameter_key, api_parameter_value})
                                                print("131", base_data)
                                            else:
                                                value_key = key
                                                value_value = ''.join(random.sample(self.str_base, 6))
                                                api_parameter_value.update({value_key: value_value})
                                                base_data.update({api_parameter_key: api_parameter_value})
                                                print("137", base_data)

                                        elif input_json.get("type") == "number" or input_json.get("type") == "integer":
                                            value_key = key
                                            value_value = random.randint(1, 500)
                                            api_parameter_value.update({value_key: value_value})
                                            base_data.update({api_parameter_key: api_parameter_value})
                                            print("144", base_data)

                                        elif input_json.get("type") == "boolean":
                                            value_key = key
                                            value_value = random.choice([True, None])
                                            api_parameter_value.update({value_key: value_value})
                                            base_data.update({api_parameter_key: api_parameter_value})
                                            print("153", base_data)
                                        elif input_json.get("type") == "array":
                                            value_key = key
                                            value_value = {}
                                            api_parameter_values = input_json.get("items")
                                            api_parameter_value.update({value_key: value_value})
                                            base_data.update({api_parameter_key: api_parameter_value})
                                            if api_parameter_values:
                                                self.key_ignore_value(api_parameter_values, base_data,
                                                                      api_parameter_key=api_parameter_key,
                                                                      api_parameter_value=base_data[api_parameter_key])
                                        elif input_json.get("type") == "file":
                                            value_key = key
                                            value_value = "file"
                                            api_parameter_value.update({value_key: value_value})
                                            base_data.update({api_parameter_key: api_parameter_value})
                                            print("165", base_data)
                                        else:
                                            pass
                                    else:
                                        pass
        elif isinstance(input_json, list):
            for json_array in input_json:
                self.key_ignore_value(json_array, base_data)
        elif isinstance(input_json, str):
            return input_json
        return {"input_json": input_json, "base_data": base_data}


a = BodyIgnore()
b = a.key_ignore_value(api_parameters, {})
print(b.get("base_data"))
