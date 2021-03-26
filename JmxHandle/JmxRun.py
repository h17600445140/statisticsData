# -*- coding: utf-8 -*-
import os, sys, re
import logging

# 初始化log
logging.basicConfig(level=logging.INFO, format=' %(levelname)s - %(asctime)s - %(pathname)s - %(filename)s[:%(lineno)d] - %(message)s')
logger = logging.getLogger('JmxHandle')


def setupJmx(jmx_prefix, threads_num, rampup_time, duration, remark, setHost=False):

    current_dir = os.getcwd()
    template_jmx = os.path.join(current_dir, 'JmxTemplate', jmx_prefix + '.jmx')

    if not os.path.exists(template_jmx):
        logger.error(template_jmx + ' path not Exist')
        return None

    # 新JmxName
    new_jmx_remark = "{}_tn{}_rt{}_d{}_{}".format(jmx_prefix, threads_num, rampup_time, duration, remark)
    new_jmx_name = new_jmx_remark + '.jmx'

    # JmxResultName
    result_dir = os.path.join(current_dir, new_jmx_remark, 'result')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    with open(template_jmx, 'r', encoding='UTF-8') as temp_stream:
        lines = temp_stream.readlines()
        with open(os.path.join(current_dir, new_jmx_remark, new_jmx_name), 'w', encoding='UTF-8') as new_stream:
            for line in lines:
                new_line = line.replace('$threads_num$', threads_num).replace('$rampup_time$', rampup_time).replace(
                    '$duration$', duration)
                if setHost:
                    new_line = re.sub('<stringProp name="HTTPSampler.domain">(.*)</stringProp>',
                                      '<stringProp name="HTTPSampler.domain">${__P(url,)}</stringProp>',new_line)
                new_stream.write(new_line)

    logger.info('Jmx文件 JmxResult目录生成完成！')

    return new_jmx_remark


def runJmeterByCmd(new_jmx_remark, hostname='', ip=''):

    def isJmeterInstalled():
        sign = False
        # 注意Window用where，Linux用which
        lines = os.popen('which jmeter')
        for l in lines:
            logger.info('Jmeter 运行路径：{}'.format(l))
            sign = True
            if sign == True:
                break
        return sign

    if hostname:
        execute_cmd = 'jmeter -Jurl={1} -n -t ./{0}/{0}.jmx -l ./{0}/{0}.jtl -j ./{0}/{0}.log -e -o ./{0}/result/'.\
            format(new_jmx_remark, hostname)
    else:
        execute_cmd = 'jmeter -n -t ./{0}/{0}.jmx -l ./{0}/{0}.jtl -j ./{0}/{0}.log -e -o ./{0}/result/'.\
            format(new_jmx_remark)

    logger.info('执行命令为：{}'.format(execute_cmd))

    if isJmeterInstalled():
        os.system(execute_cmd)

if __name__ == '__main__':
    if len(sys.argv[1:]) == 5:
        param = sys.argv[1:]
        # 注意，setupJmx中setHost=False，runJmeterByCmd中hostname不填

        # new_jmx_remark = setupJmx(param[0], param[1], param[2], param[3], param[4], True)
        # runJmeterByCmd(new_jmx_remark, 'www.baidu.com')

        new_jmx_remark = setupJmx(param[0], param[1], param[2], param[3], param[4])
        runJmeterByCmd(new_jmx_remark)
    else:
        print('参数输入错误，请输入正确的参数')







