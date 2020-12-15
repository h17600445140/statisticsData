from HTMLTable import HTMLTable

def createHtml(title, data, tester_html):
    # Title = '今日提交BUG数'

    # 标题
    # table = HTMLTable(caption=Title)
    table = HTMLTable()

    # 表头行
    # table.append_header_rows((('测试人员','今日提交BUG数','待验证BUG数'),))
    table.append_header_rows(title)

    # 数据行
    table.append_data_rows(data)

    # 标题样式
    # table.caption.set_style({
    #     'font-size': '18px',
    #     'font-weight': 'bolder'
    # })

    # 表格样式，即<table>标签样式
    table.set_style({
    'border-collapse': 'collapse',
    'word-break': 'keep-all',
    'white-space': 'nowrap',
    'font-size': '14px',
    })

    # 统一设置所有单元格样式，<td>或<th>
    table.set_cell_style({
    'border-color': '#000',
    'border-width': '1px',
    'border-style': 'solid',
    'padding': '5px',
    "text-align":"center"
    })

    # 表头样式
    table.set_header_row_style({
    'color': '#fff',
    'background-color': '#48a6fb',
    'font-size': '18px',
    })

    # 覆盖表头单元格字体样式
    table.set_header_cell_style({
    'padding': '15px',
    })

    # 调小次表头字体大小
    table[1].set_cell_style({
    'padding': '8px',
    'font-size': '15px',
    })

    # 遍历数据行，对应数据为负，标红背景颜色
    # for row in table.iter_data_rows():
    #     if row[2].value < 0:
    #         row.set_style({
    #             'background-color': '#ffdddd',
    #         })

    html = table.to_html()

    with open('./html/template.html', 'r', encoding="UTF-8") as template_rfile:
        template_file = template_rfile.read()
    html = template_file.replace("%content%", html)
    with open('./html/'+tester_html, 'w', encoding="UTF-8") as template_wfile:
        template_wfile.write(html)

if __name__ == '__main__':
    Title = (('测试人员','今日提交BUG数','待验证BUG数','今日关闭BUG数'),)
    data = [
        ['黄超', 110, "0", 10],
        ['肖城', 20, "0", 10],
        ['杨兴', 50, "0", 10]
    ]
    tester_html = 'testerHtml.html'
    createHtml(Title, data, tester_html)

