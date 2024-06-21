from lxml import html

html_content = '''
<div class="alert alert-danger loginmenu" role="alert" xpath="1">
    <span class="fa fa-exclamation-circle" aria-hidden="true"></span>
    <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>
    <span class="sr-only">Error:</span>
    Invalid Company Code
</div>
'''

tree = html.fromstring(html_content)
# XPath to select the text node containing "Invalid Company Code"
text_element = tree.xpath("//div[@class='alert alert-danger loginmenu']/text()[normalize-space()='Invalid Company "
                          "Code']")
print(text_element)
text_element = tree.xpath("//div[@class='alert alert-danger loginmenu']/text()[normalize-space()='Invalid Company "
                          "Code']")
cleaned_text = text_element[0].strip() if text_element else None
print(cleaned_text)