#!/usr/bin/env python
# coding:utf8
from fastapi import FastAPI
from apidoc import *
from utils import *
import uvicorn
import logging
import config
import multiprocessing

app = FastAPI(debug=True, docs_url='/api/docs', openapi_url='/api/openapi.json', redoc_url='/api/redoc')


@app.post("/api/getscore", name="获取分数", description="获取分数", response_model=generalresp)
async def getscore(item: getscore):
    logging.debug('post receive:/api/getscore json:%s' % item.studentid)
    mysql_tool = MySQLTool(config.mysqlhost, config.mysqluser, config.mysqlpass, config.mysqldb)
    mysql_tool.connect()
    resp = mysql_tool.execute_query('select * from t_score where studentnumber="{}";'.format(item.studentid))
    mysql_tool.close()
    return BaseUtils.sendjson(200, 'success', resp)


@app.get("/api/test", name='接口测试', response_model=generalresp)
async def helloworld():
    return BaseUtils.sendjson(200, 'success', 'Hello World')


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=config.listenport, host=config.hostip, workers=multiprocessing.cpu_count())
