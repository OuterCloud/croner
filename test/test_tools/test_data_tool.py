import csv

class T_data_reader(object):
	def __init__(self, file_path):
		setattr(self, 'file_content_lines', [])
		csv_reader = csv.reader(open(file_path, encoding='utf-8'))
		for row in csv_reader:
			self.file_content_lines.append(row)
		fields = self.file_content_lines[0]
		setattr(self, 't_data_count', len(self.file_content_lines)-1)
		# Traverse t data.
		for i in range(len(self.file_content_lines)-1):
			t_data = {}
			for j in range(len(fields)):
				t_data[fields[j]] = self.file_content_lines[i+1][j]
			setattr(self, 't_data_'+str(i+1), t_data)

	def get_t_data_count(self):
	 	return self.t_data_count
		
def get_t_data(file_path):
	t_data_reader = T_data_reader(file_path)
	t_data_count = t_data_reader.get_t_data_count()
	t_data = []
	for i in range(t_data_count):
		t_data.append(getattr(t_data_reader,"t_data_"+str(i+1)))
	return t_data