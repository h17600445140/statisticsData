#!/bin/bash

# Author:huangchao

# 压测脚本模板中设定的压测时间自定义，脚本只涉及修改thread_num，如需修改压测时间，可自行修改脚本文件

export jmx_template="baiduTest"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"

export JMETER_HOME=/usr/lib/jmeter/apache-jmeter-5.4.1

# your computer's name
export os_type=`uname`

echo "自动化压测开始"

# 压测并发数列表
thread_number_list=(10 20 30 40)

for num in "${thread_number_list[@]}"
do
    # 生成对应压测线程的jmx文件
    export jmx_filename="${jmx_template}_${num}${suffix}"
    export jtl_filename="resultJtl_${num}.jtl"
    export report_pathName="report_${num}"

    rm -f ${jmx_filename} ${jtl_filename}
    rm -rf ${report_pathName}
    
    cp ${jmx_template_filename} ${jmx_filename}
    echo "生成jmx压测脚本 ${jmx_filename}"

    if [[ "${os_type}" == "Darwin" ]]; then
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    else
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    fi

    # JMeter 静默压测
    ${JMETER_HOME}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename}

    # 生成Web压测报告
    ${JMETER_HOME}/bin/jmeter -g ${jtl_filename} -e -o ${report_pathName}

done
echo "自动化压测全部结束"
