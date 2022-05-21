import xlrd
from groups import groups

work_file = xlrd.open_workbook('Excel_files/расписание!!!.xls', formatting_info=True)


def create_timetable_excel(start, coll, group_file):
    """Parse column from excel table"""
    skip = start
    with open(group_file, 'w', encoding='Windows 1251') as file_object:
        while True:
            try:
                if sheet.cell_value(start, 0) == '' and sheet.cell_value(start, coll) == '':
                    start += 1
                    continue
                elif sheet.cell_value(start, 0) == '' and sheet.cell_value(start, coll + 1) == '':
                    start += 1
                    continue
                if 'День' in str(sheet.cell_value(start, 0)) and skip != start:
                    file_object.write('\n-----------------------------------------------\n\n')
                try:
                    file_object.write(
                        f'{int(sheet.cell_value(start, 0))}.   {sheet.cell_value(start, coll)}  {int(sheet.cell_value(start, coll + 1))}\n')
                except ValueError:
                    file_object.write(
                        f'{int(sheet.cell_value(start, 0))}.   {sheet.cell_value(start, coll)}  {(sheet.cell_value(start, coll + 1))}\n')
            except ValueError:
                try:
                    try:
                        file_object.write(
                            f'{sheet.cell_value(start, 0)}      {sheet.cell_value(start, coll)} {int(sheet.cell_value(start, coll + 1))}\n')
                    except ValueError:
                        file_object.write(
                            f'{sheet.cell_value(start, 0)}.   {sheet.cell_value(start, coll)}  {(sheet.cell_value(start, coll + 1))}\n')
                except IndexError:
                    break
            except IndexError:
                break

            start += 1


def read_timetable(group_file):
    """Return schedule text"""
    with open(group_file, 'r', encoding='Windows 1251') as file_object:
        return file_object.read()


# Create schedule files for all group
sheet = work_file.sheet_by_index(0)
create_timetable_excel(6, 1, 'Groups/AT/AT19-11')
create_timetable_excel(6, 3, 'Groups/AT/AT20-11')
create_timetable_excel(6, 5, 'Groups/AT/AT21-11')
create_timetable_excel(6, 7, 'Groups/DO/DO19-11-1')
create_timetable_excel(6, 9, 'Groups/DO/DO19-11-2')

sheet = work_file.sheet_by_index(1)
create_timetable_excel(5, 1, 'Groups/DO/DO20-11-1')
create_timetable_excel(5, 3, 'Groups/DO/DO20-11-2')
create_timetable_excel(5, 5, 'Groups/DO/DO21-11-1')
create_timetable_excel(5, 7, 'Groups/DO/DO21-11-2')
create_timetable_excel(5, 9, 'Groups/IBAS/IBAS21-11')

sheet = work_file.sheet_by_index(2)
create_timetable_excel(6, 1, 'Groups/ISiP/ISiP19-11-1')
create_timetable_excel(6, 3, 'Groups/ISiP/ISiP19-11-2')
create_timetable_excel(6, 5, 'Groups/ISiP/ISiP20-11-1')
create_timetable_excel(6, 7, 'Groups/ISiP/ISiP20-11-2')
create_timetable_excel(6, 9, 'Groups/ISiP/ISiP20-11-3')

sheet = work_file.sheet_by_index(3)
create_timetable_excel(5, 1, 'Groups/ISiP/ISiP21-11-1')
create_timetable_excel(5, 3, 'Groups/ISiP/ISiP21-11-2')
create_timetable_excel(5, 5, 'Groups/ISiP/ISiP21-11-3')
create_timetable_excel(5, 7, 'Groups/KP/KP19-11-1')
create_timetable_excel(5, 9, 'Groups/KP/KP19-11-2')

sheet = work_file.sheet_by_index(4)
create_timetable_excel(6, 1, 'Groups/KP/KP19-11-3')
create_timetable_excel(6, 3, 'Groups/KP/KP20-11-1')
create_timetable_excel(6, 5, 'Groups/KP/KP20-11-2')
create_timetable_excel(6, 7, 'Groups/KP/KP20-11-3')
create_timetable_excel(6, 9, 'Groups/KP/KP20-11-4')

sheet = work_file.sheet_by_index(5)
create_timetable_excel(5, 1, 'Groups/KP/KP21-11-1')
create_timetable_excel(5, 3, 'Groups/KP/KP21-11-2')
create_timetable_excel(5, 5, 'Groups/KP/KP21-11-3')
create_timetable_excel(5, 7, 'Groups/OSATPIP/OSATPIP19-11-1')
create_timetable_excel(5, 9, 'Groups/OSATPIP/OSATPIP19-11-2')

sheet = work_file.sheet_by_index(6)
create_timetable_excel(5, 1, 'Groups/OSATPIP/OSATPIP20-11-1')
create_timetable_excel(5, 3, 'Groups/OSATPIP/OSATPIP20-11-2')
create_timetable_excel(5, 5, 'Groups/OSATPIP/OSATPIP21-11')
create_timetable_excel(5, 7, 'Groups/PDOTT/PDOTT19-11')
create_timetable_excel(5, 9, 'Groups/PDOTT/PDOTT20-11')

sheet = work_file.sheet_by_index(7)
create_timetable_excel(5, 1, 'Groups/PDOTT/PDOTT21-11')
create_timetable_excel(5, 3, 'Groups/SSA/SSA19-11-1')
create_timetable_excel(5, 5, 'Groups/SSA/SSA19-11-2')
create_timetable_excel(5, 7, 'Groups/SSA/SSA19-11-3')
create_timetable_excel(5, 9, 'Groups/SSA/SSA20-11-1')

sheet = work_file.sheet_by_index(8)
create_timetable_excel(6, 1, 'Groups/SSA/SSA20-11-2')
create_timetable_excel(6, 3, 'Groups/SSA/SSA20-11-3')
create_timetable_excel(6, 5, 'Groups/SSA/SSA21-11-1')
create_timetable_excel(6, 7, 'Groups/SSA/SSA21-11-2')
create_timetable_excel(6, 9, 'Groups/SSA/SSA21-11-3')
