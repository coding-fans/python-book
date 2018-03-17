#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   agentx.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import argparse


class ServiceController(object):

    '''
        服务控制器

        根据命令行参数，操作后台服务(守护进程)。
    '''

    def __init__(self, conf_path):
        # 命令行参数
        self.conf_path = conf_path

    def status(self):
        '''
            查询服务运行状态
        '''

        print('service is ...')

    def start(self):
        '''
            启动服务
        '''

        print('starting')

    def stop(self):
        '''
            停止服务
        '''

        print('stopping')

    def process(self, action):
        '''
            处理入口
        '''

        getattr(self, action)()


def main():
    '''
        主函数

        负责处理命令行参数并调用服务控制器。
    '''

    # 命令行解析
    parser = argparse.ArgumentParser(prog='agentx')

    # 配置文件选项
    parser.add_argument(
        '-c',
        '--conf',
        dest='conf_path',
        metavar='conf_path',
        default='',
        required=False,
        help='configuration file path',
    )

    # 操作选项
    parser.add_argument(
        'action',
        nargs=1,
        metavar='action',
        choices=('status', 'start', 'stop',),
        help='action to carry out: status/start/stop',
    )

    # 解析
    args = parser.parse_args()

    # 配置文件路径
    conf_path = args.conf_path
    # 执行动作
    action, = args.action


    # 处理
    service_controller = ServiceController(conf_path=conf_path)
    service_controller.process(action=action)

if __name__ == '__main__':
    main()
