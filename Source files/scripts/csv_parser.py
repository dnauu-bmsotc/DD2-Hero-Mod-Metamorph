import csv, sys
from pathlib import Path

folder = "C:\Program Files (x86)\Steam\steamapps\common\Darkest Dungeon® II\Darkest Dungeon II_Data\StreamingAssets\Excel"
tag_fields_file = ".\csv_parser_tag_fields.txt"
keywords_fields_file = ".\csv_parser_keyword_fields.txt"
combined_fields_file = ".\csv_parser_combined_fields.txt"
overrides_file = ".\csv_parser_overrides.txt"

output_file = ".\csv_parser_result.md"

long_list_threshold = 16

def parse_files(folder):
    csv_filepaths = Path(folder).rglob("*.csv")
    return [el for fp in csv_filepaths for el in parse_file(fp)]

def parse_file(filepath):
    with open(filepath.resolve(), "r", encoding="utf-8-sig") as f:
        return list(parse_rows(csv.reader(f)))

def parse_rows(rows):
    current_element = None
    for row in remove_empty(rows):
        first_word = row[0]
        if first_word == "element_start":
            current_element = {
                "id": row[1],
                "type": row[2],
                "data": [],
            }
        elif first_word == "element_end":
            yield current_element
        else:
            values = list(remove_empty(row[1:]))
            current_element["data"].append((first_word, values))

def remove_empty(list):
    return filter(lambda x: x is not None and str(x).strip() != "", list)

def filter_elements_by_type(elements, element_type):
    return filter(lambda x: x["type"] == element_type, elements)

def find_all_fields_for_a_type(elements, element_type):
    matching_elements = filter_elements_by_type(elements, element_type)
    fields = set(f[0] for el in matching_elements for f in el["data"])
    return sorted(remove_empty(fields))

# def element_has_a_field(element, field_name):
#     return any(line[0] == field_name for line in element["data"])

def get_element_data_lines_by_field(element, field_name):
    return list(filter(lambda x: x[0] == field_name, element["data"]))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def number_if_is_number(s):
    try:
        return float(s)
    except ValueError:
        return False
    
def find_all_lines_by_element_type_and_field_name(elements, element_type, field_name) -> set:
    matching_elements = filter_elements_by_type(elements, element_type)
    matching_lines = [line for el in matching_elements for line in get_element_data_lines_by_field(el, field_name)]
    return matching_lines
    
def find_all_values_for_a_field(elements, element_type, field_name) -> set:
    matching_lines = find_all_lines_by_element_type_and_field_name(elements, element_type, field_name)
    return set(v for line in matching_lines for v in line[1])

def find_all_values_for_a_field_pos(elements, element_type, field_name, pos) -> set:
    matching_lines = find_all_lines_by_element_type_and_field_name(elements, element_type, field_name)
    return set(line[1][pos] for line in matching_lines if pos < len(line[1]))

def does_field_allow_multiple_values(elements, element_type, field_name) -> bool:
    matching_lines = find_all_lines_by_element_type_and_field_name(elements, element_type, field_name)
    for l in matching_lines:
        if len(l[1]) > 1:
            return True
    return False

def find_all_types(elements) -> set:
    return set(elem['type'] for elem in elements)

def is_type_present_in_all_id_groups(elements, element_type):
    groups = dict()
    for e in elements:
        if e["id"] in groups:
            groups[e["id"]].append(e)
        else:
            groups[e["id"]] = [e]
    for g in groups:
        present = False
        for ge in groups[g]:
            if ge["type"] == element_type:
                present = True
                break
        if not present:
            return False
    return True

def find_all_types_by_ids(elements, ids) -> set:
    matching_elements = [elem for elem in elements if elem['id'] in ids]
    types = set(elem['type'] for elem in matching_elements)
    return set(t for t in types if is_type_present_in_all_id_groups(matching_elements, t))

def find_all_ids(elements) -> set:
    return set(map(lambda el: el["id"], elements))

def values_have_a_float_value(values) -> bool:
    return any(is_number(v) and not v.lstrip('-+').isdigit() for v in values)

def values_have_an_int_value(values) -> bool:
    return any(v.lstrip('-+').isdigit() for v in values)

def values_have_a_bool_value(values) -> bool:
    return any((v == "True") or (v == "False") for v in values)

def values_have_a_bool_value_true(values) -> bool:
    return any((v == "True") for v in values)

def values_have_a_bool_value_false(values) -> bool:
    return any((v == "False") for v in values)

def find_unidentified_values(values, ids):
    def cond(x):
        return (not is_number(x)) and (x != "True") and (x != "False")
    return list(filter(cond, values.difference(ids)))

def to_absolute_path(path):
    path = Path(path)
    if not path.is_absolute():
        path = Path(__file__).parent / path
    return path

def get_list_from_file(filepath):
    with open(to_absolute_path(filepath), 'r') as file:
        return [line.strip() for line in file]

def find_combined_example(elements, element_type, field_name):
    for e in filter_elements_by_type(elements, element_type):
        for line in e["data"]:
            if line[0] == field_name:
                return line
            
def find_override(overrides, element_type, field_name, cell):
    override_sig = f"{element_type},{field_name},{cell},"
    for override in overrides:
        if override_sig in override:
            return override[len(override_sig):]
    return ""

def separate_values_by_plus(values):
    return set(newvals for oldval in values for newvals in oldval.split("+"))


with open(to_absolute_path(output_file), "w", encoding="utf-8") as f:
    original_stdout = sys.stdout
    sys.stdout = f
    try:
        elements = parse_files(folder)
        types = find_all_types(elements)
        ids = find_all_ids(elements)
        tag_fields = set(get_list_from_file(tag_fields_file))
        keywords_fields = set(get_list_from_file(keywords_fields_file))
        overrides = get_list_from_file(overrides_file)

        for t in sorted(list(types)):
        # for t in ["BattleConfigurationTable"]:
            print(f"<details>")
            print(f"<summary>{t}</summary>")
            print(f"")

            # print("| Field | Value Types | Values | Multiple Values | Comment |")
            # print("| :---- | :---------- | :----- | :-------------- | :------ |")
            print("| Field | Values | Multiple Values | Comment |")
            print("| :---- | :----- | :-------------- | :------ |")

            fields = find_all_fields_for_a_type(elements, t)
            for f in fields:
                all_values = find_all_values_for_a_field(elements, t, f)

                print(f"|{f}|", end="")

                accepts_tags = f in tag_fields # accepts only tags
                accepts_kw = f in keywords_fields # accepts only keywords
                accepts_float = values_have_a_float_value(all_values) and not accepts_tags and not accepts_kw
                accepts_int = values_have_an_int_value(all_values) and not accepts_tags and not accepts_kw
                accepts_bool = values_have_a_bool_value(all_values) and not accepts_tags and not accepts_kw
                accepts_id = not ids.isdisjoint(all_values) and not accepts_tags and not accepts_kw
                
                keywords = find_unidentified_values(all_values, ids)

                accepts = ""
                if accepts_float:
                    accepts += "Float "
                if accepts_int and not accepts_float:
                    accepts += "Integer "
                if accepts_bool:
                    accepts += "Bool "
                if accepts_id:
                    referenced = find_all_values_for_a_field(elements, t, f)
                    types = list(find_all_types_by_ids(elements, referenced))
                    if len(types) == 1:
                        accepts += f"{types[0]}&nbsp;ID "
                    else:
                        accepts += f"!!!{types} "
                if len(keywords) > 0:
                    accepts += "Keyword "
                    if accepts_kw:
                        keywords = all_values
                if accepts_tags:
                    accepts = "Tag"
                    keywords = all_values
                    keywords = set()

                accepts = accepts.strip().replace(" ", "/")

                is_a_combined_field = sum([accepts_float or accepts_int, accepts_bool, len(find_unidentified_values(all_values, [])) > 0]) > 1
                if is_a_combined_field:
                    accepts = f"Combined"

                type_override = find_override(overrides, t, f, "Value Types")
                if False:
                    if not type_override:
                        print(f"{accepts}|", end="")
                    else:
                        print(f"{type_override}|", end="")

                kws = ""

                if accepts_float:
                    numbers = list(remove_empty(map(number_if_is_number, all_values)))
                    kws += f"{min(numbers):.2f}...{max(numbers):.2f} "
                    
                if accepts_int and not accepts_float:
                    numbers = list(remove_empty(map(number_if_is_number, all_values)))
                    kws += f"{min(numbers):.0f}...{max(numbers):.0f} "
                    
                if accepts_bool:
                    kws += "Boolean "
                    
                if accepts_tags:
                    kws += "Tags "

                if accepts_id:
                    pass

                if len(keywords) > 0:
                    kws_addition = ""
                    for kw in sorted(keywords):
                        kws_addition += kw + " "
                    if len(keywords) < long_list_threshold:
                        kws += kws_addition
                    else:
                        kws += f"<details><summary>Click&#8201;to&#8201;expand</summary>{kws_addition}</details>"
                    
                kws = kws.strip().replace(" ", "<br>")

                if is_a_combined_field:
                    example = find_combined_example(elements, t, f)
                    kws = f"Example: `{example[0]},{','.join(example[1])},`"
                    for i in range(len(example)):
                        values = find_all_values_for_a_field_pos(elements, t, f, i)
                        values = find_unidentified_values(values, [])
                        if len(values):
                            kws += f"<br>Slot {i + 1} values:<br>"
                            kws_addition = '<br>'.join(sorted(list(values)))
                            if len(values) < long_list_threshold:
                                kws += kws_addition
                            else:
                                kws += f"<details><summary>Click&#8201;to&#8201;expand</summary>{kws_addition}</details>"

                if types and (len(types) == 1) and (kws == ""):
                    kws += f"{types[0]}&nbsp;ID "

                if kws == "":
                    kws = "<sub>parse fail</sub>"
                
                values_override = find_override(overrides, t, f, "Values")
                if not values_override:
                    print(f"{kws}", end="")
                else:
                    print(f"{values_override}", end="")

                print("|", end="")
                multiple = does_field_allow_multiple_values(elements, t, f)
                multiple_override = find_override(overrides, t, f, "Multiple Values")
                if not multiple_override:
                    print("Yes" if multiple else "No", end="")
                else:
                    print(f"{multiple_override}", end="")
                
                print("|", end="")

                print(f"{find_override(overrides, t, f, 'Comment')}", end="")

                print("|")
                
            print(f"")
            print(f"</details>")
            print(f"")
        
    finally:
        sys.stdout = original_stdout
