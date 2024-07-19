import os
from jinja2 import Template

def generate_report(scan_output, report_file):
    with open(scan_output, 'r') as file:
        scan_results = file.read()

    template = Template("""
    <html>
    <head><title>Nikto Scan Report</title></head>
    <body>
    <h1>Nikto Scan Report</h1>
    <pre>{{ scan_results }}</pre>
    </body>
    </html>
    """)

    report_content = template.render(scan_results=scan_results)
    
    with open(report_file, 'w') as file:
        file.write(report_content)

if __name__ == "__main__":
    scan_output = os.getenv('NIKTO_OUTPUT', 'scan_results.html')
    report_file = 'report.html'
    generate_report(scan_output, report_file)

