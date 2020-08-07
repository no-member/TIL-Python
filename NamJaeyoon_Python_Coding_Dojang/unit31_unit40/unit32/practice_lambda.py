files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda file_name: file_name.find('.jpg') != -1 or file_name.find('.png') != -1, files)))
