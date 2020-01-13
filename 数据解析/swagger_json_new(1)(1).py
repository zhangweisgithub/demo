# -*-coding:utf-8 -*-
import sys,random
import copy
import os,json,string
import re

import requests

json_params="""{
  "swagger": "2.0",
  "info": {
    "description": "This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.",
    "version": "1.0.0",
    "title": "Swagger Petstore",
    "termsOfService": "http://swagger.io/terms/",
    "contact": {
      "email": "apiteam@swagger.io"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }
  },
  "host": "http://xxxx",
  "basePath": "/v2",
  "tags": [
    {
      "name": "pet",
      "description": "Everything about your Pets",
      "externalDocs": {
        "description": "Find out more",
        "url": "http://swagger.io"
      }
    },
    {
      "name": "store",
      "description": "Access to Petstore orders"
    },
    {
      "name": "user",
      "description": "Operations about user",
      "externalDocs": {
        "description": "Find out more about our store",
        "url": "http://swagger.io"
      }
    }
  ],
  "schemes": [
    "https",
    "http"
  ],
  "paths": {
    "/pet": {
      "post": {
        "tags": [
          "pet"
        ],
        "summary": "Add a new pet to the store",
        "description": "",
        "operationId": "addPet",
        "consumes": [
          "application/json",
          "application/xml"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "body",
            "name": "params1",
            "description": "Pet object that needs to be added to the store",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Pet"
            }
          }
        ],
        "responses": {
          "405": {
            "description": "Invalid input"
          }
        },
        "security": [
          {
            "petstore_auth": [
              "write:pets",
              "read:pets"
            ]
          }
        ]
      }
    },
    "/pet/findByStatus": {
      "get": {
        "tags": [
          "pet"
        ],
        "summary": "Finds Pets by status",
        "description": "Multiple status values can be provided with comma separated strings",
        "operationId": "findPetsByStatus",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "params2",
            "in": "query",
            "description": "Status values that need to be considered for filter",
            "required": true,
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "available",
                "pending",
                "sold"
              ],
              "default": "available"
            },
            "collectionFormat": "multi"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Pet"
              }
            }
          },
          "400": {
            "description": "Invalid status value"
          }
        },
        "security": [
          {
            "petstore_auth": [
              "write:pets",
              "read:pets"
            ]
          }
        ]
      }
    },
    "/user": {
      "post": {
        "tags": [
          "user"
        ],
        "summary": "Create user",
        "description": "This can only be done by the logged in user.",
        "operationId": "createUser",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "body",
            "name": "params3",
            "description": "Created user object",
            "required": true,
            "schema": {
              "$ref": "#/definitions/User"
            }
          }
        ],
        "responses": {
          "default": {
            "description": "successful operation"
          }
        }
      }
    },
    "/user/login": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "Logs user into the system",
        "description": "",
        "operationId": "loginUser",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "params4",
            "in": "query",
            "description": "The user name for login",
            "required": true,
            "type": "string"
          },
          {
            "name": "params5",
            "in": "query",
            "description": "The password for login in clear text",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "string"
            },
            "headers": {
              "X-Rate-Limit": {
                "type": "integer",
                "format": "int32",
                "description": "calls per hour allowed by the user"
              },
              "X-Expires-After": {
                "type": "string",
                "format": "date-time",
                "description": "date in UTC when token expires"
              }
            }
          },
          "400": {
            "description": "Invalid username/password supplied"
          }
        }
      }
    },
    "/user/logout": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "Logs out current logged in user session",
        "description": "",
        "operationId": "logoutUser",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [],
        "responses": {
          "default": {
            "description": "successful operation"
          }
        }
      }
    },
    "/user/{username}": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "Get user by user name",
        "description": "",
        "operationId": "getUserByName",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "The name that needs to be fetched. Use user1 for testing. ",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/User"
            }
          },
          "400": {
            "description": "Invalid username supplied"
          },
          "404": {
            "description": "User not found"
          }
        }
      },
      "put": {
        "tags": [
          "user"
        ],
        "summary": "Updated user",
        "description": "This can only be done by the logged in user.",
        "operationId": "updateUser",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "name that need to be updated",
            "required": true,
            "type": "string"
          },
          {
            "in": "body",
            "name": "username2",
            "description": "Updated user object",
            "required": true,
            "schema": {
              "$ref": "#/definitions/User"
            }
          }
        ],
        "responses": {
          "400": {
            "description": "Invalid user supplied"
          },
          "404": {
            "description": "User not found"
          }
        }
      },
      "delete": {
        "tags": [
          "user"
        ],
        "summary": "Delete user",
        "description": "This can only be done by the logged in user.",
        "operationId": "deleteUser",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "The name that needs to be deleted",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "400": {
            "description": "Invalid username supplied"
          },
          "404": {
            "description": "User not found"
          }
        }
      }
    }
  },
  "securityDefinitions": {
    "petstore_auth": {
      "type": "oauth2",
      "authorizationUrl": "http://petstore.swagger.io/oauth/dialog",
      "flow": "implicit",
      "scopes": {
        "write:pets": "modify pets in your account",
        "read:pets": "read your pets"
      }
    },
    "api_key": {
      "type": "apiKey",
      "name": "api_key",
      "in": "header"
    }
  },
  "definitions": {
    "Category": {
      "type": "object",
      "properties": {
        "id1": {
          "type": "integer",
          "format": "int64"
        },
        "name1": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Category"
      }
    },
    "User": {
      "type": "object",
      "properties": {
        "id2": {
          "type": "integer",
          "format": "int64"
        },
        "username1": {
          "type": "string"
        },
        "firstName": {
          "type": "string"
        },
        "lastName": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string"
        },
        "phone": {
          "type": "string"
        },
        "userStatus": {
          "type": "integer",
          "format": "int32",
          "description": "User Status"
        }
      },
      "xml": {
        "name": "User"
      }
    },
    "Tag": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name2": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Tag"
      }
    },
    "Pet": {
      "type": "object",
      "required": [
        "name",
        "photoUrls"
      ],
      "properties": {
        "id3": {
          "type": "integer",
          "format": "int64"
        },
        "category": {
          "$ref": "#/definitions/Category"
        },
        "name3": {
          "type": "string",
          "example": "doggie"
        },
        "photoUrls": {
          "type": "array",
          "xml": {
            "name": "photoUrl",
            "wrapped": true
          },
          "items": {
            "type": "string"
          }
        },
        "tags": {
          "type": "array",
          "xml": {
            "name": "tag",
            "wrapped": true
          },
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "status": {
          "type": "string",
          "description": "pet status in the store",
          "enum": [
            "available",
            "pending",
            "sold"
          ]
        }
      },
      "xml": {
        "name": "Pet"
      }
    },
    "ApiResponse": {
      "type": "object",
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "type": {
          "type": "string"
        },
        "message": {
          "type": "string"
        }
      }
    }
  },
  "externalDocs": {
    "description": "Find out more about Swagger",
    "url": "http://swagger.io"
  }
}"""

types_of_value = ["string", "file", "integer", "boolean", "email", "datetime", "phone"]
headers={
	'Content-Type': 'text/html; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
    'Connection': 'keep-alive',
}
responses_err={
          "400": {
            "description": "Invalid username supplied"
          }
        }
responses_ok={
          "200": {
            "description": "successful operation"
          }
        }
def check_data(r):
    """检查返回的数据是否是dict"""
    if not isinstance(r, dict):
        raise Exception('swagger return json error!!')
    else:
        return True

"""替换definitions的引用（$ref）"""
def definitions_ref(value, all_values):
    temp_bak = {}
    if isinstance(value, dict):
        t_k = value.get("value")
        temp_k = {}
        temp_value = {}
        if t_k.get("type") == "object":
            t_m = t_k.get("properties")
            for each_key in t_m:
                if "$ref" in t_m.get(each_key).keys():
                    m = t_m.get(each_key).get("$ref").split("/")
                    mat = 0
                    for tar_key in all_values:
                        if m[2] == tar_key.get("key"):
                            bak = definitions_ref(tar_key, all_values)
                            mat = 1
                            temp_value[each_key] = bak
                    if mat == 0:
                        temp_value[each_key] = "Error"

                elif "items" in t_m.get(each_key).keys():
                    if t_m.get(each_key).get("items").get("$ref"):
                        m = t_m.get(each_key).get("items").get("$ref").split("/")
                        mat = 0
                        for tar_key in all_values:
                            if m[2] == tar_key.get("key"):
                                bak = definitions_ref(tar_key, all_values)
                                mat = 1
                                temps = {"items": bak, "type": "array"}
                                # print(bak)
                                temp_value[each_key] = temps
                        if mat == 0:
                            temp_value[each_key] = "Error"
                    else:
                        m = t_m.get(each_key).get("items")
                        bak = m
                        temps = {"items": bak, "type": "array"}
                        temp_value[each_key] = temps
                        # temp_value[each_key]=t_m.get(each_key)
                else:
                    temp_value[each_key] = t_m.get(each_key)
        elif t_k.get("type") == "array":
            t_m = t_k.get("items")
            if "$ref" in t_m.keys():
                m = t_m.get("$ref").split("/")
                mat = 0
                for tar_key in all_values:
                    if m[2] == tar_key.get("key"):
                        bak = definitions_ref(tar_key, all_values)
                        mat = 1
                        return bak
                if mat == 0:
                    return {"Error": "Can't match key"}
        temp_k["type"] = t_k.get("type")
        temp_k["properties"] = temp_value
        temp_bak["key"] = value.get("key")
        temp_bak["value"] = temp_k
        return temp_bak

"""去除definitons里ref替换后里面的key：xxx，value"""
def remove_surplus_key(value):
    if isinstance(value, dict):
        if "type" in value.keys():
            if value.get("type") == "object":
                bak = remove_surplus_key(value.get("properties"))
                if bak:
                    value["properties"] = bak
            elif value.get("type") == "array":
                bak = remove_surplus_key(value.get("items"))
                if bak:
                    value["items"] = bak
        else:
            if "key" in value.keys():
                return value.get("value")
            else:
                for each_key in value.keys():
                    bak = remove_surplus_key(value.get(each_key))
                    value[each_key] = bak
        return value

"""替换paths的引用（$ref）"""
def cat_paths(value, all_value):
    bck = []
    for each in value:
        temp = {}
        local = each.get("in")
        required = each.get("required")
        name = each.get("name")
        if "schema" in each.keys():
            if each.get("schema").get("$ref"):
                schema = each.get("schema").get("$ref").split("/")
                mat = 0
                for each_key in all_value:
                    if schema[2] == each_key.get("key"):
                        mat = 1
                        # print(each_key.get("value"), name)
                        temp["in"] = local
                        temp["required"] = required
                        temp[name] = each_key.get("value")
                if mat == 0:
                    temp["in"] = local
                    temp[name] = {"Error": "No match!"}
            elif each.get("schema").get("items").get("$ref"):
                schema = each.get("schema").get("items").get("$ref").split("/")
                mat = 0
                for each_key in all_value:
                    if schema[2] == each_key.get("key"):
                        mat = 1
                        # print(each_key.get("value"), name)
                        temp["in"] = local
                        temp["required"] = required
                        temp[name] = each_key.get("value")
                if mat == 0:
                    temp["in"] = local
                    temp[name] = {"Error": "No match!"}
            else:
                temp["in"] = local
                temp["required"] = required
                temp[name] = each
        else:
            temp["in"] = local
            temp["required"] = required
            temp[name] = each
        bck.append(temp)
    return bck

""" 取出paths每一层参数及对应类型"""
def load_temp(values):
    if isinstance(values, dict):
        dict_bak = {}
        temp_list = []
        if "type" in values.keys():
            temp_type = values.get("type")
            if temp_type == "object":
                bak_value = load_temp(values.get("properties"))
                return bak_value
            elif temp_type == "array":
                # 当他是array的时候，不能识别出来是array（在处理变成key，type的时候），所以目前处理方案是放置三个作为一个列表，然后进行操作。
                # print(values)
                bak_value = load_temp(values.get("items"))
                temp_list.append(bak_value)
                # temp_list.append(bak_value)
                return temp_list
            else:
                return temp_type
        else:
            for each in values.keys():
                bak_value = load_temp(values.get(each))
                dict_bak[each] = bak_value
            return dict_bak
    elif isinstance(values, list):
        list_bak = []
        for each in values:
            if isinstance(each, list):
                bak_value = load_temp(each)
                list_bak.append(bak_value)
            elif isinstance(each, dict):
                bak_value = load_temp(each)
                list_bak.append(bak_value)
            else:
                list_bak.append(each)
        return list_bak

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

"""特殊类型处理"""
def find_special_key(values):
    if isinstance(values, dict):
        for each_key in values:
            if isinstance(values.get(each_key), dict):
                find_special_key(values.get(each_key))
            if isinstance(values.get(each_key), list):
                for each_list in values.get(each_key):
                    find_special_key(each_list)
            if each_key == "phone":
                values[each_key] = "phone"
            if each_key == "email":
                values[each_key] = "email"
            if each_key == "datetime":
                values[each_key] = "datetime"
    elif isinstance(values, list):
        for each_list in values:
            find_special_key(each_list)
    return values

def return_right(types, tars):
    """0表示正确的，1表示错误的,ok的设置必须是1或统一的n，不能出现第三个数"""
    lists = []
    if types == "string":
        if tars == "ok":
            lists.append(random_char(6))
    elif types == "boolean":
        if tars == "ok":
            lists.append(0)
            lists.append(1)
    elif types == "integer":
        if tars == "ok":
            lists.append(110)
            lists.append(9223372036854775807)
    elif types == "file":
        if tars == "ok":
            lists.append('file')
    elif types == "email":
        if tars == "ok":
            lists.append('testing@sensetime.com')
    elif types == 'phone':
        if tars == "ok":
            lists.append('13800000000')
    elif types == "datetime":
        if tars == "ok":
            lists.append('2019.05.24')
    return lists

"""找出所有key和value"""
def find_key_value(values, task_key,task_value):
    if isinstance(values, dict):
        for each in values:
            bak = find_key_value(values.get(each), task_key,task_value)
            if bak == "key":
                task_key.append(each)
                task_value.append(values.get(each))
    elif isinstance(values, list):
        for each in values:
            bak = find_key_value(each, task_key,task_value)
            if bak == "key":
                task_key.append(each)
                task_value.append(each)
    else:
        if values in types_of_value:
            return "key"

"""[{},{},{},{}] 取出所有参数及对应的取值等"""
def public_key_value(values):
    list1 = []
    list_key_one = []
    list_key_many = []
    # 根据value长度把key存入列表
    for k in values.keys():
        if len(values[k]) == 1:
            list_key_one.append(k)
        else:
            list_key_many.append(k)
    # 找到长度最大的
    if list_key_many:
        max_length = values[list_key_many[0]]
    else:
        max_length = ["str"]
    # 遍历取值赋值
    for i in range(len(max_length)):
        list1_dict = {}
        for k_many in list_key_many:
            list1_dict[k_many] = values[k_many][i]
        for k_one in list_key_one:
            list1_dict[k_one] = values[k_one][0]
        list1.append(list1_dict)
    return list1

"""组合"""
def key_value(tar_key, tar_value):
    # tar_bak = []
    temp_dict = {}
    for i in range(len(tar_key)):
        temp_dict[tar_key[i]] = tar_value[i]
    # tar_bak.append(temp_dict)
    # return tar_bak
    return temp_dict

"""解析参数，然后组合,一步步把参数赋给整个values"""
def ok_sequence(values, keys_sequence, keys=None):
    if isinstance(values, dict):
        tar_key = []
        tar_velue = []
        for each_key in values:
            tar_key.append(each_key)
            bak = ok_sequence(values.get(each_key), keys_sequence, each_key)
            tar_velue.append(bak)
        return key_value(tar_key, tar_velue)
    elif isinstance(values, list):
        tar_back = []
        for each in values:
            if isinstance(each, list):
                bak = ok_sequence(each, keys_sequence)
                tar_back.append(bak)
            elif isinstance(each, dict):
                bak = ok_sequence(each, keys_sequence)
                tar_back.append(bak)
            else:
                return values
        # return list_list(tar_back)
        return tar_back
    elif isinstance(values, str):
        bak = str(keys_sequence.get(keys))
        return bak

"""针对一个get或post下有多个in的情况：[{'in': 'query', 'required': True, 'value': {'params4': 'string'}}, {'in': 'query', 'required': True, 'value': {'params5': 'string'}}]"""
def ok_in_value(values):#[{"in":"","required":"","value":[{},{}]},{"in":"","required":"","value":[{},{}]}]
    list_key_one = []
    list_key_many = []
    dict_1 = {}
    list_k2 = []
    list2 = []
    if len(values)<=1:
        for k in values:
            for i in k.get("values"):
                list_k1 = []
                dict_1["in"] = k.get("in")
                dict_1["required"] = k.get("required")
                dict_1["values"] = i
                list_k1.append(dict_1)
                list_set=copy.deepcopy(list_k1)
                list_k2.append(list_set)
        return list_k2
    else:
        for k in values:
            k_value=k.get("values")
            # 根据value长度把key存入列表
            if len(k_value) <= 1:
                list_key_one.append(k)
            else:
                list_key_many.append(k)
        if list_key_many:
            max_length = len(list_key_many[0].get("values"))
        else:
            max_length = 1
        for i in range(max_length):
            list1=[]
            for k_many in list_key_many:
                list1.append({"in":k_many.get("in"),"required":k_many.get("required"),"values":k_many.get("values")[i]})
            for k_one in list_key_one:
                list1.append({"in":k_one.get("in"),"required":k_one.get("required"),"values":k_one.get("values")[0]})
            list2.append(list1)
        return list2

"""错误用例相关函数"""
def return_wrong(types, tars):
    """0表示正确的，1表示错误的"""
    lists = []
    if types == "string":
        if tars == "0":
            lists.append(random_char(6))
        elif tars == "1":
            lists.append(123)
            lists.append("")
    elif types == "boolean":
        if tars == "0":
            lists.append(1)  #1表示True，0表示False
        elif tars == "1":
            lists.append(random_char(15))
            lists.append("")
    elif types == "integer":
        if tars == "0":
            lists.append(110)
        elif tars == "1":
            lists.append(random_char(25))
            lists.append(0.0)
            lists.append("")
    elif types == "file":
        if tars == "0":
            lists.append('file')
        elif tars == "1":
            lists.append('file')
    elif types == "email":
        if tars == "0":
            lists.append('testing@sensetime.com')
        elif tars == "1":
            lists.append(random_char(25))
            lists.append("")
    elif types == 'phone':
        if tars == "0":
            lists.append('13800000000')
        elif tars == "1":
            lists.append("123456789518991812")
            lists.append("")
    elif types == "datetime":
        if tars == "0":
            lists.append('2019.05.24')
        elif tars == "1":
            lists.append("123456789518991812")
            lists.append("")
    return lists

def error_list_value(values):#[value1,value2,value3,value4],处理变成：[[["","dgdg"],["dfdf"],["ddsfds"]],[],[],[]...]
    list_1=[]
    list_all,list_errs=[],[]
    for i in range(len(values)):
        list_1.append("0")
    for i in range(len(list_1)):
        list_set=copy.deepcopy(list_1)
        list_set[i]="1"
        list_all.append(list_set)
    for i in list_all:
        list_err=[]
        for j in range(len(values)):
            list_err.append(return_wrong(values[j],i[j]))
        list_errs.append(list_err)
    return list_errs

"""排列出所有错误key取值的可能,例如[["",dfdf","ddsfds",110],["dgdg","dfdf","ddsfds",110]...]"""
def error_value(values):#[key1,key2,key3,key4],[[["","dgdg"],["dfdf"],["ddsfds"],["110"]],[],[],[]...]
    list_t = []
    for each in values:
        for i in each:
            if len(i) > 1:
                maxlength = len(i)
        for k in range(maxlength):
            list_s = []
            for v in each:
                if len(v) == 1:
                    list_s.append(v[0])
                else:
                    list_s.append(v[k])
            list_t.append(list_s)
    return list_t

def err_sequence(values,keys_sequence):
    if isinstance(values, dict):
        tar_key = []
        tar_velue = []
        for each_key in values:
            tar_key.append(each_key)
            bak = err_sequence(values.get(each_key),keys_sequence)
            tar_velue.append(bak)
        return key_value(tar_key, tar_velue)
    elif isinstance(values, list):
        tar_back = []
        for each in values:
            if isinstance(each, list):
                bak = err_sequence(each,keys_sequence)
                tar_back.append(bak)
            elif isinstance(each, dict):
                bak = err_sequence(each,keys_sequence)
                tar_back.append(bak)
            else:
                return keys_sequence.pop(0)
                # return values
        return tar_back
    elif isinstance(values, str):
        if values in types_of_value:
            bak = keys_sequence.pop(0)
            return bak
        elif values in ["path","body","query"]:
            bak=values
            return bak
    elif values == True or values == False:
        bak=values
        return bak

class err_case(object):
    def __init__(self,values,keys_sequence):
        self.keys_sequence=keys_sequence
        self.values=values

    def err_cas(self):
        result=err_sequence(self.values,self.keys_sequence)
        return result

class swagger_case(object):
    """swagger自动生成测试用例"""
    def __init__(self, url_json):
        if isinstance(url_json,str):
            temp_json = url_json.replace("true", "True")
            temp_json = temp_json.replace("false", "False")
            self.url_json=eval(temp_json)
        else:
            s = requests.get(url_json).json()
            if check_data(s):
                r = requests.get(url_json).text
                temp_json=r.replace("true","True")
                temp_json=temp_json.replace("false","False")
                self.url_json=eval(temp_json)
        self.title = self.url_json['info']['description']
        self.interface_params = {}
        self.num = 1  # case id
        self.api_paths = ""
        self.paths=[]     #取paths的数据
        self.definitions=[]
        self.host=self.url_json.get("host")

    def get_paths(self):
        self.api_paths = self.url_json.get("paths")
        for k in self.api_paths:
            value = self.api_paths.get(k)
            for k_method in value:
                temp = {"path": k, "requests_method": k_method, "values": value.get(k_method)}
                self.paths.append(temp)
        return self.paths

    def handle_definitions_path(self):
        definitions=self.url_json.get("definitions")
        if definitions:
            test_1 = []
            for k in definitions:    #取出definitions的key、value组成新的字典
                temp = definitions.get(k)
                temp_key = {"key": k, "value": temp}
                self.definitions.append(temp_key)

            for k in self.definitions:   #替换掉definitinos里的$ref
                bak = definitions_ref(k, self.definitions)
                test_1.append(bak)
            self.definitions = test_1
            # print(test_1)
            test_2 = []
            for each in self.definitions:     #definitions移除引用ref里的key：xxxx,value:
                temp_dict = {}
                bak = remove_surplus_key(each.get("value"))
                temp_dict["key"] = each.get("key")
                temp_dict["value"] = bak
                test_2.append(temp_dict)
            self.definitions = test_2
            # return self.definitions
            test_3 = []
            for each in self.paths:          #替换path里的$ref
                requests_method = each.get("requests_method")
                paths = each.get("path")
                parameters = each.get("values").get("parameters")
                summary = each.get("values").get("summary")
                tags = each.get("values").get("tags")
                if parameters:
                    bak = cat_paths(parameters, self.definitions)
                    temp = {"paths": paths, "requests_method": requests_method, "summary": summary, "tags": tags,
                            "parameters": bak, "responses": each.get("values").get("responses")}
                    test_3.append(temp)
                else:
                    temp = {"paths": paths, "requests_method": requests_method, "summary": summary, "tags": tags,
                            "parameters": [], "responses": each.get("values").get("responses")}
                    test_3.append(temp)
            self.app_simple_path = test_3
            return self.app_simple_path
        else:
            print("error")

    """取出paths里每一层对应参数及类型"""
    def resolution_path_to_dict(self):
        all_list = []
        for each in self.app_simple_path:
            each_list = []
            temp_bck = {}
            paths = each.get("paths")
            requests_method = each.get("requests_method")
            parameters = each.get("parameters")
            summary = each.get("summary")
            tags = each.get("tags")
            # responses=each.get("responses")
            for par_each in parameters:
                temp_in = par_each.get("in")
                temp_required = par_each.get("required")
                temp_dict = {}
                temp_bck_two = {}
                for key_each in par_each:
                    if key_each == "in":
                        continue
                    elif key_each == "required":
                        continue
                    else:
                        temp_dict[key_each] = par_each.get(key_each)
                        bck = load_temp(temp_dict)   #取出paths里每一层对应参数及类型
                        temp_bck_two["in"] = temp_in
                        temp_bck_two["required"] = temp_required
                        temp_bck_two["values"] = bck
                        each_list.append(temp_bck_two)
            temp_bck["paths"] = paths
            temp_bck["requests_method"] = requests_method
            temp_bck["summary"] = summary
            temp_bck["tags"] = tags
            temp_bck["parameters"] = each_list
            # temp_bck["responses"] = responses
            all_list.append(temp_bck)
        self.app_change_body = all_list
        return self.app_change_body
        # print(self.app_change_body)

    def get_ok_params(self):
        t_bck = []
        for each in self.app_change_body:
            ok_lists = []
            value = each.get("parameters")
            find_special_key(value)
            for value_each in value:
                body_in=value_each.get("in")
                required=value_each.get("required")
                task_key,task_value,list_value = [],[],[]
                dict_1,dict_2 ={},{}
                t_m = value_each.get("values")
                # print(value_each)
                find_key_value(t_m, task_key,task_value)
                for i in task_value:
                    list_value.append(return_right(i, "ok"))
                for j in task_key:
                    dict_1[j] = list_value.pop(0)
                # print(dict_1)
                t_k = public_key_value(dict_1)
                list_bak1 = []
                for t_k_each in t_k:
                    m_k = ok_sequence(t_m,t_k_each)
                    # print(m_k)
                    list_bak1.append(m_k)
                dict_2["in"] = body_in
                dict_2["required"] = required
                dict_2["values"] = list_bak1
                ok_lists.append(dict_2)
            in_value=ok_in_value(ok_lists)
            #处理"parameters": []这种情况
            if in_value!=[]:
                for k_value in in_value:
                    temp_bck = {"paths": each.get("paths"), "requests_method": each.get("requests_method"),
                                "summary": each.get("summary"), "tags": each.get("tags"), "parameters": k_value}
                    t_bck.append(temp_bck)



    def ret_ok_case(self):
        """主函数"""
        # global body_name
        for i in self.app_change_body_ok:
            interface = {}
            k_dict = {}
            k_dict["paths"] = i.get("paths") # api地址
            k_dict["requests_method"] = i.get("requests_method")
            k_dict["summary"] = i.get("summary") #接口名称
            k_dict["tags"] = i.get("tags")
            k_dict["parameters"] = i.get("parameters")
            k_dict["responses"]=responses_ok
            cases_ok = self.retrieve_case(k_dict, interface)
            print(cases_ok)

    def retrieve_case(self, v, interface):
        api = v.get('paths')
        parameters = v.get('parameters')  # 参数
        case_name = v['summary']  # 接口名称
        tags = v['tags'][0]  # 标签名称
        requests_method=v['requests_method']
        params_dict = self.retrieve_params(parameters,api)  # 处理接口参数
        responses=v['responses']
        if params_dict !={}:
            if params_dict.get("body") =={}:
                interface['ID'] = 'test_' + str(self.num)  # case id
                interface['Tags'] = tags  # 标签名称
                interface['Name'] = case_name
                # _type = 'json'  # 参数获取方式
                interface['Method'] = requests_method  # 请求方式
                interface['URL'] = self.host + params_dict.get("api")  # 拼接完成接口url
                interface['Headers'] = params_dict.get("headers")  # 是否传header
                interface['Responses'] = responses
                self.num += 1
                return interface
            else:
                interface['ID'] = 'test_' + str(self.num)  # case id
                interface['Tags'] = tags  # 标签名称
                interface['Name'] = case_name
                # _type = 'json'  # 参数获取方式
                interface['Method'] = requests_method  # 请求方式
                interface['URL'] = self.host + params_dict.get("api")  # 拼接完成接口url
                interface['Headers'] = params_dict.get("headers")  # 是否传header
                interface['Body'] = params_dict.get("body")
                interface['Responses'] = responses
                self.num += 1
            return interface
        else:
            interface['ID'] = 'test_' + str(self.num)  # case id
            interface['Tags'] = tags  # 标签名称
            interface['Name'] = case_name
            # _type = 'json'  # 参数获取方式
            interface['Method'] = requests_method  # 请求方式
            interface['URL'] = self.host + api  # 拼接完成接口url
            interface['Headers'] = headers  # 是否传header
            # interface['body'] = {}
            interface['Responses'] = responses
            self.num += 1
            return interface

    def retrieve_params(self, parameters,api):
        """处理参数，转为dict"""
        dict_params = {}
        if parameters != []:
            re_api = api
            api_headers=headers
            api_body = {}
            for each in parameters:
                if each.get("in") == "body":
                    if each.get("required") == True:
                        api_body = each.get("values")
                    else:
                        api_body = {}
                elif each.get("in") == "headers":
                    if each.get("required") == True:
                        api_headers=each.get("values")
                    else:
                        api_headers=headers
                elif each.get("in") == "path":
                    # list_path = []
                    if each.get("required") == True:
                        paths=each.get("values")
                        # m_list = api.split("/")
                        for k,v in paths.items():
                            re_1=re.search(r'\{([^\}]+)\}',re_api).group(1)
                            if k == re_1:
                                re_api = re.sub(r'({.*})',str(v),re_api)
                    else:
                        re_api = re_api
                elif each.get("in") == "query":
                    if each.get("required") == True:
                        paths=each.get("values")
                        for k,v in paths.items():
                            re_api+="?"+str(k)+"="+str(v)
                    else:
                        re_api = re_api
                else:
                    api_headers = headers
            dict_params["body"] = api_body
            dict_params["headers"] = api_headers
            dict_params["api"] = re_api
            return dict_params
        else:
            return dict_params

    def get_error_params(self):
        t_bck = []
        for each in self.app_change_body:
            values = each.get("parameters")
            t_m = find_special_key(values)
            task_key, task_value, list_bak1 = [], [], []
            find_key_value(t_m, task_key, task_value)
            t_v = error_list_value(task_value)
            t_k =  error_value(t_v)
            for t_i in t_k:
                s = err_case(t_m,t_i)
                s1 = s.err_cas()
                # print(s1)
                ko_dict = {"paths": each.get("paths"), "requests_method": each.get("requests_method"),
                                     "summary": each.get("summary"), "tags": each.get("tags"), "parameters": s1}
                # print(ko_dict)
                t_bck.append(ko_dict)
        self.app_change_body_ko = t_bck
        return self.app_change_body_ko

    def ret_err_case(self):
        """主函数"""
        # global body_name
        for i in self.app_change_body_ko:
            interface = {}
            k_dict = {}
            k_dict["paths"] = i.get("paths") # api地址
            k_dict["requests_method"] = i.get("requests_method")
            k_dict["summary"] = i.get("summary") #接口名称
            k_dict["tags"] = i.get("tags")
            k_dict["parameters"] = i.get("parameters")
            k_dict["responses"]=responses_err
            cases_err = self.retrieve_case(k_dict, interface)
            print(cases_err)

if __name__ == '__main__':
    test_swagger=swagger_case(json_params)
    test_swagger.get_paths()
    s1=test_swagger.handle_definitions_path()
    # print(s1)
    s2=test_swagger.resolution_path_to_dict()
    # print(s2)
    s3=test_swagger.get_ok_params()
    # print(s3)
    s4=test_swagger.ret_ok_case()
    s5=test_swagger.get_error_params()
    # print(s5)
    s6=test_swagger.ret_err_case()
    print(s6)