import time
from node_text import TextNode, TextType
from bs4 import BeautifulSoup, Comment
from playwright.sync_api import sync_playwright

void_tags = {'img', 'br', 'hr', 'input'}

# narrow down original html to only things we care about
# returns Beautiful Soup object
def trim_html(html_text):
	skip_tags = {
		'br',
		'header',
		'hr',
		'iframe',
		'img',
		'input',
		'noscript',
		'script',
		'style',
		'svg'
	}
	soup = BeautifulSoup(html_text, 'html.parser')
	# only look at things in the body
	trimmed = soup.body
	# remove comments
	comments = soup.find_all(string=lambda text: isinstance(text, Comment))
	for comment in comments:
		comment.decompose()
	# remove tags we don't care about
	for tag in skip_tags:
		for trash_tag in trimmed.find_all(tag):
			trash_tag.decompose()
	return trimmed

# this is where the html should be split into parent and leaf nodes,
# but it still needs work to create those elements as it is recursing
# so relationships are preserved
def process_html(html_text):
	pre_blocks = []
	if not hasattr(html_text, 'contents'):
		pre_blocks.append(html_text)
	# add element if it doesn't have children
	elif not hasattr(html_text, 'children') or len(html_text.contents) == 0:
		pre_blocks.append(html_text)
	else:
		for child in html_text.children:
			child_results = process_html(child)
			pre_blocks.extend(child_results)	
	# blocks are not strings, need to handle as beautiful soup object
	# for block in pre_blocks:
	# 	print(str(block) + '\n')
	return pre_blocks

def split_html(old_nodes, )

# pulls the html from the given URL
def get_fully_rendered_html(url, timeout=30):
	with sync_playwright() as p:
		# 1. setup the browser
		browser = p.chromium.launch()
		page = browser.new_page()
		# 2. initial nagivation
		# use documentloaded to at least get the basic script running
		page.goto(url, wait_until="domcontentloaded")
		# 3. stability check (steady state logic)
		previous_length = 0
		start_time = time.time()

		while time.time() - start_time < timeout:
			current_html = page.content()
			current_length = len(current_html)

			# if html size hasn't changed in the last second and
			# it's not an empty page, we are likely done
			if current_length == previous_length and current_length > 0:
				break
			
			previous_length = current_length
			time.sleep(1)
		
		# 4. return final, stable html
		final_html = process_html(trim_html(page.content()))
		print(final_html)
		browser.close()
		return final_html

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		nodes_of_old = old_node.text.split(delimiter)
		if len(nodes_of_old) % 2 == 0:
			raise Exception(f"missing closing character: {delimiter}")
		temp_list = []
		for i in range(len(nodes_of_old)):
			if nodes_of_old[i] == "":
				continue
			if i % 2 == 0:
				temp_list.append(TextNode(nodes_of_old[i], TextType.TEXT))
			else:
				temp_list.append(TextNode(nodes_of_old[i], text_type))
		new_nodes.extend(temp_list)
	return new_nodes

# need to handle dividing nodes
# recursively so relationships are preserved

def text_to_textnodes(text):
	# bold
	formatted = split_nodes_delimiter([TextNode(text, TextType.TEXT, None)], "**", TextType.BOLD)
	# italic
	formatted = split_nodes_delimiter(formatted, "_", TextType.ITALIC)
	# code
	formatted = split_nodes_delimiter(formatted, "`", TextType.CODE)
	# image
	formatted = split_nodes_image(formatted)
	# link
	formatted = split_nodes_link(formatted)
	
	return formatted

def markdown_to_blocks(markdown):
	separated = markdown.split("\n\n")
	blocks = []
	for item in separated:
		block = item.strip()
		if block != "":
			blocks.append(block)
	return blocks
			