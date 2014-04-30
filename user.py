import relations

class user():
    
    screen_name = ''
    subject_list = []

    def get_screen_name(self):
        return self.screen_name

    def set_screen_name(self, sname):
        self.screen_name = sname
        return self.screen_name

    def get_subject_list(self):
        return self.subject_list

    def create_subject_list(self, data):

        data_type = str(type(data))

        if data_type == "<type 'list'>":
            for d in data:
                self.subject_list.append(relations.get_dict_relations(d))

        elif data_type == "<type 'file'>":
            for line in data:
                self.subject_list.append(relations.get_dict_relations(str(line)))
        return self.subject_list

