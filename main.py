#--------------------------------------------------------------------------------
#Text-based CMS in Python
#Runs a loop inspired by the WordPress Loop on text files for quicker prototyping
#In the near future, will be implemented as a server which does it on request
#PradyGameDev - May 13th 2016
#--------------------------------------------------------------------------------
import os, json
class TextCMS:
	def __init__(self, metadata_file_path, stylesheet_file_path, output_file_path):
		self.mfp = os.curdir + os.sep + metadata_file_path
		self.sfp = stylesheet_file_path
		self.ofp = os.curdir + os.sep + output_file_path
		self.mf = open(self.mfp, 'r')
		self.of = open(self.ofp, 'w+')
		self.metadata, self.dict = {}, {}#to be read from a csv or json 
		#using json
		self.output = ""
		self.post=None
		self.metadata = json.loads(self.mf.read())
		for post_name in self.metadata['posts']:
			self.post = open(post_name.split('\n')[0] + ".txt",'r')
			self.dict[post_name.split('\n')[0]] = self.post.read()
		print "Metadata\n"
		print "Title: " + self.metadata["title"] + "\nAuthor: " + self.metadata["author"] + "\n"
	def header(self):
		self.output += '<html>\n<head>\n<link rel="stylesheet" type="text/css" href="' + self.sfp + '">\n<div id="header">\n<h2>\n' + self.metadata['title'] + '<br>by ' + self.metadata['author'] + '</h2>\n</div>\n'
	def content(self, name=None):
		if not name:
			for key, value in zip(self.dict.keys(), self.dict.values()):
				self.output += '<div class="post_title"><h2>' + key + '</h2>\n</div>\n'
				self.output += '<div class="post_content"><h2>' + value + '</h2>\n</div>\n'
		else:
			self.output += '<div class="post_title"><h2>' + name + '</h2>\n</div>\n'
			self.output += '<div class="post_content"><h2>' + self.dict[name] + '</h2>\n</div>\n'
	def footer(self):
		self.output += '<div id="footer">\nThis is the footer area.\n</div>'
		self.output += '\n</body>\n</html>\n'
	#Now functions to generate different page templates as WordPress has
	def onePageView(self):
		self.header()
		self.content()
		self.footer()
	def onePostView(self, name):
		self.header()
		self.content(name)
		self.footer()
	def commit(self):
		if self.output:
			self.of.write(self.output)
	def clearOutput():
		output=""
cms = TextCMS('metadata.json', 'style.css', 'posts.html')
cms.onePageView()
cms.commit()