"""
Written by Qingyang
Date: 04/02/2019
class: movieProfile
"""
import math
from circularPlate import sectorPlate

class movieProfile(object):
    """
    Details on the movie object.
    """
    def __init__(self,file_dir,female_file_dir=None,female_names=None,character_size=None):
        """
        Inputs:
            file_dir: String of file dir. Example, 'movie.csv'.
            female_file_dir: String of female_file_dir. Example, 'female_movie.csv'
            female_names: List of strings. Example ['ry','fx']
            plate: sectorPlate/circularPlate.

        data:
        episode_id, dialog_nums, start_time, end_time, source_name, target_name
        female_data:
        episode_id, dialog_nums, start_time, end_time, source_name, target_name

        person_id: Dictionary.
        appear_time: Dictionary.
        female_list: List of integers. Female person_id.
        """
        self.file_dir = file_dir
        self.female_file_dir = female_file_dir
        self.female_names = female_names

        with open(self.file_dir, 'r') as infile:
            self.data = infile.readlines()
        self.LINE_NUM = len(self.data)
        self.total_time = self.data[-1].split(',')[3]
        self.plate = sectorPlate(canvas_size=(height, width), total_time=self.total_time, person_nums=18)

        with open(self.female_file_dir, 'r') as female_infile:
            self.female_data = female_infile.readlines()
        self.FEMALE_LINE_NUM = len(self.female_data)

        self.set_constants()
        self.CHARACTER_NUM = len(self.person_id)

        self.female_list = self.set_female_list
        self.character_size = self.convert_character_size(character_size)

        self.build_file()
        if self.female_file_dir:
            self.build_female_file()

    def set_constants(self):
        appear_time_dict = {}
        person_id_dict = {}
        count = 0
        for line in self.data:
            line = line.split(',')
            source_name = line[4]
            target_names = line[5].split('+')
            start_time = line[2]
            end_time = line[3]
            if source_name not in appear_time_dict.keys():
                appear_time_dict[source_name] = start_time
                person_id_dict[source_name] = count
                count = count + 1
            for target_name in target_names:
                if target_name not in appear_time_dict.keys():
                    appear_time_dict[target_name] = start_time
                    person_id_dict[target_name] = count
                    count = count + 1
        self.appear_time = appear_time_dict
        self.person_id = person_id_dict

    @property
    def set_female_list(self):
        female_list = []
        for female_name in self.female_names:
            female_list.append(self.person_id[female_name])
        return female_list

    def convert_character_size(self,character_size):
        new_character_size = {}
        for key_name in character_size.keys():
            new_character_size[self.person_id[key_name]] = character_size[key_name]
        for ind in range(self.CHARACTER_NUM):
            if ind not in new_character_size.keys():
                new_character_size[ind] = 1.0
        return new_character_size

    def build_file(self):
        self.source_points = []
        self.target_points = []
        self.source_ids = []
        self.target_ids = []
        self.dialog_nums = []
        self.branch_points = []
        self.branch_angs = []
        for line in self.data:
            line = line.split(',')
            dialog_num = int(line[1])
            source_id = self.person_id[line[4]]
            start_time = line[2]
            end_time = line[3]
            target_names = line[5].split('+')
            source_x,source_y = self.plate.getCoordinates(start_time,source_id)

            target_ids = []
            target_points = []
            for tar_ind in range(len(target_names)):
                target_id = self.person_id[target_names[tar_ind]]
                target_x,target_y = self.plate.getCoordinates(end_time, target_id)
                target_ids.append(target_id)
                target_points.append((target_x,target_y))

            # target ids should be in ascent order
            if len(target_ids) == 2:
                if target_ids[0] > target_ids[1]:
                    target_ids = [target_id for target_id in reversed(target_ids)]
                    target_points = [target_point for target_point in reversed(target_points)]

            if target_ids[-1] > source_id:
                self.branch_points.append(target_points[-1])
                self.branch_angs.append(radians(self.plate.getCurrentAngle(end_time)))
            else:
                self.branch_points.append((source_x,source_y))
                self.branch_angs.append(radians(self.plate.getCurrentAngle(start_time)))

            self.dialog_nums.append(dialog_num)
            self.source_points.append((source_x,source_y))
            self.target_points.append(target_points)
            self.source_ids.append(source_id)
            self.target_ids.append(target_ids)

    def build_female_file(self):

        self.female_source_points = []
        self.female_target_points = []
        self.female_source_ids = []
        self.female_target_ids = []
        self.female_dialog_nums = []
        for line in self.female_data:
            line = line.split(',')
            dialog_num = int(line[1])
            source_id = self.person_id[line[4]]
            start_time = line[2]
            end_time = line[3]
            target_names = line[5].split('+')
            source_x, source_y = self.plate.getCoordinates(start_time, source_id)

            target_ids = []
            target_points = []
            for tar_ind in range(len(target_names)):
                target_id = self.person_id[target_names[tar_ind]]
                target_x, target_y = self.plate.getCoordinates(end_time, target_id)
                target_ids.append(target_id)
                target_points.append((target_x, target_y))

            if len(target_ids) == 2:
                if target_ids[0] > target_ids[1]:
                    target_ids = [target_id for target_id in reversed(target_ids)]
                    target_points = [target_point for target_point in reversed(target_points)]

            self.female_dialog_nums.append(dialog_num)
            self.female_source_points.append((source_x, source_y))
            self.female_target_points.append(target_points)
            self.female_source_ids.append(source_id)
            self.female_target_ids.append(target_ids)


    def id2size(self,id):
        return self.character_size[id]

    def drawSector(self):
        self.plate.drawSector()
