
class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []

    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table width='100%' border='1' cellpadding='0' cellspacing='0' " \
                                                                 "style='table-layout:fixed;margin:0;padding:0;'>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td width='300' style='white-space:normal;word-break:break-all;overflow:hidden;'>%s</td>"%
                       data['url'])
            fout.write("<td width='10%%'>%s</td>"% data['title'].encode('utf-8'))
            fout.write("<td width='60%%'>%s</td>"% data['summary'].encode('utf-8'))
            fout.write("</td>") 
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
    
    
    



